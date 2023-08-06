import logging

import requests
from jwt.exceptions import (
    ExpiredSignatureError
)
from microsoft_auth.models import MicrosoftAccount
from rest_framework import status

from Common.utils import gen_password
from Common.utils import get_tenancy_name_from_url
from Common.utils import get_tenant_config
from apps.user.models import ComplianceGroup

logger = logging.getLogger("django")


class OAuthFlow:
    baseURL = 'https://login.microsoftonline.com/{}/oauth2/v2.0/token'
    graphApiBaseURL = "https://graph.microsoft.com/v1.0/"
    client_id = None
    client_secret = None
    tenant_id = None

    redirect_uri = None
    grant_type = None
    scope = 'openid%20offline_access%20%20email%20profile'  # 'openid%20offline_access%20https%3A%2F%2Fgraph.microsoft.com%2F.default'
    code = None

    def __init__(self, tenant_id, client_id, client_secret, code=None, redirect_uri=None, state=None,
                 session_state=None, *args, **kwargs):
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        self.state = state
        self.session_state = session_state,
        self.redirect_uri = redirect_uri
        self.code = code
        self.graphApiBaseURL = self.graphApiBaseURL.format(self.tenant_id)
        pass

    def get_access_token(self):
        req_body = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'authorization_code',
            'redirect_uri': self.redirect_uri,
            'scope': "User.Read",
            'code': self.code,
        }
        response = requests.post(self.baseURL.format(self.tenant_id), data=req_body)
        return response

    def refresh_token(self, refresh_token):
        req_body = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_uri,
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token
        }
        response = requests.post(self.baseURL.format(self.tenant_id), data=req_body)
        return response

    def verify_ad_jwt(self, token):
        try:
            azure_ad_jwks_uri = 'https://login.microsoftonline.com/{}/discovery/v2.0/keys'.format(
                self.tenant_id
            )
            azure_ad_issuer = 'https://login.microsoftonline.com/{}/v2.0'.format(self.tenant_id)
            from azure_ad_verify_token import verify_jwt
            payload = verify_jwt(
                token=token,
                valid_audiences=[self.client_id],
                issuer=azure_ad_issuer,
                jwks_uri=azure_ad_jwks_uri,
            )

            return payload
        except Exception as e:
            logger.error("invalid token {}", e)
        except ExpiredSignatureError as e:
            raise e

    def get_user_from_db(self, data):
        microsoft_user = MicrosoftAccount.objects.get(
            microsoft_id=data["id"]
        )
        return microsoft_user

    def get_microsoft_user(self, request, data):
        microsoft_user = None
        try:
            microsoft_user = self.get_user_from_db(data)
        except MicrosoftAccount.DoesNotExist:
            microsoft_user = MicrosoftAccount(microsoft_id=data["id"])
            microsoft_user.save()

        if microsoft_user.user is None:
            self.verify_microsoft_user(request, microsoft_user, data)

        return microsoft_user

    def verify_microsoft_user(self, request, microsoft_user, data):
        user = microsoft_user.user
        tenancy_name = get_tenancy_name_from_url(request.get_host())
        tenant, ms_tenantic, ms_clientid, ms_clientsecret = get_tenant_config(request)
        if not tenant:
            raise Exception("Invalid Request No Tenancy Matched")
        if user is None:
            fullname = data.get("displayName")

            first_name, last_name = "", ""

            if fullname is not None:
                try:
                    # LastName, FirstName format
                    last_name, first_name = fullname.split(", ")
                except ValueError:
                    try:
                        first_name, last_name = fullname.split(" ", 1)
                    except ValueError:
                        firstname = fullname

            try:
                if 'userPrincipalName' in data:
                    email = data['userPrincipalName']
                else:
                    if "unique_name" in data:
                        email = data['unique_name']
                user = User.objects.get(email=email)

                if user.first_name == "" and user.last_name == "":
                    user.first_name = first_name
                    user.last_name = last_name
                    user.Tenant = tenant
                    user.save()
            except User.DoesNotExist:
                user = User(
                    username=data["userPrincipalName"],
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.Tenant = tenant
                user.save()

        microsoft_user.user = user
        microsoft_user.save()
        return user

    def get_app_authenticated(self):
        url = 'https://login.microsoftonline.com/' + self.tenant_id + '/oauth2/v2.0/token'
        if not self.client_id:
            raise Exception(
                "The required parameter `client_id` was not supplied, "
            )
        if not self.client_secret:
            raise Exception(
                "The required parameter `client_id` was not supplied, "
            )

        body = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scope': 'https://graph.microsoft.com/.default'
        }
        return requests.post(url, data=body)

    def get_user_from_ad(self, access_token, ms_id):
        try:

            http_headers = {'Authorization': '{}'.format(access_token),
                            # 'User-Agent': 'adal-python-sample',
                            'Accept': 'application/json',
                            'Content-Type': 'application/json',
                            }
            url = "{}users/{}".format(self.graphApiBaseURL, ms_id)
            res = requests.get(url, headers=http_headers, stream=False)
            if res.status_code == status.HTTP_200_OK:
                return res.json()
            raise res.text
        except Exception as e:
            logger.error("get_user:ms graph auth failed  {}".format(e))
            return None

    def get_profile(self, access_token):
        http_headers = {'Authorization': 'Bearer {}'.format(access_token),
                        # 'User-Agent': 'adal-python-sample',
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        }
        url = "https://graph.microsoft.com/v1.0/me"
        res = requests.get(url, headers=http_headers, stream=False)
        if res.status_code == status.HTTP_200_OK:
            return res.json()
        err = res.json().get('error', None).get('message', None)
        logger.error("get profile :ms graph auth failed  {}".format(err))
        raise Exception(err)


    def get_groups(self, access_token):
        try:

            http_headers = {'Authorization': 'Bearer {}'.format(access_token),
                            # 'User-Agent': 'adal-python-sample',
                            'Accept': 'application/json',
                            'Content-Type': 'application/json',
                            }
            url = "https://graph.microsoft.com/v1.0/me/memberOf"
            res = requests.get(url, headers=http_headers, stream=False)
            if res.status_code == status.HTTP_200_OK:
                return res.json()
            raise res.text
        except Exception as e:
            logger.error("get groups  :ms graph auth failed  {}".format(e))
            return None


from apps.user.models import User


class GraphApi(OAuthFlow):

    def __init__(self, tenant_id, client_id, client_secret, code=None, redirect_uri=None, state=None,
                 session_state=None, *args, **kwargs):
        super().__init__(tenant_id, client_id, client_secret, code, redirect_uri, state, session_state, *args, **kwargs)

    def create_user(self, token, fname, displayname, email, password):
        req_body = {
            "accountEnabled": True,
            "displayName": displayname,
            "mailNickname": fname,
            "userPrincipalName": email,
            "passwordProfile": {
                "forceChangePasswordNextSignIn": True,
                "password": gen_password(12)
            }
        }

        http_headers = {'Authorization': 'Bearer {}'.format(token),
                        'User-Agent': 'adal-python-sample',
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        }
        url = '{}users'.format(self.graphApiBaseURL)
        response = requests.post(url, headers=http_headers, json=req_body)
        return response

    def update_user(self, token, fname, displayname, email, previousUserPrincipalName):
        req_body = {
            "accountEnabled": True,
            "displayName": displayname,
            "mailNickname": fname,
            "userPrincipalName": email
        }

        http_headers = {'Authorization': 'Bearer {}'.format(token),
                        'User-Agent': 'adal-python-sample',
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        }
        url = '{}users/{}'.format(self.graphApiBaseURL, previousUserPrincipalName)
        response = requests.patch(url, headers=http_headers, json=req_body)
        return response


class GraphApiManager:
    BaseURL = 'https://graph.microsoft.com/v1.0/'

    def __init__(self, request):
        self.access_token = self.get_access_token(request)

    def get_access_token(self, request):
        access_token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
        return access_token

    def reset_password(self, current_Password, new_password):
        url = '{}me/changePassword'.format(self.BaseURL)
        req_body = {
            "currentPassword": current_Password,
            "newPassword": new_password
        }
        if not self.access_token:
            raise Exception("Unauthenticated Request")

        http_headers = {'Authorization': 'Bearer {}'.format(self.access_token),
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        }
        response = requests.post(url, headers=http_headers, json=req_body)
        return response
