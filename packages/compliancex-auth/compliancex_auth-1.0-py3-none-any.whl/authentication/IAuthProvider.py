from django.conf import settings


class IUserAuthProvider:

    def get_access_token(self):
        raise NotImplemented()

    #
    def get_user_profile(self):
        raise NotImplemented()

    def get_auth_url(self):
        raise NotImplemented()

    def get_member_of(self):
        raise NotImplemented()

    def get_Token(self):
        raise NotImplemented()

    def refresh_token(self):
        raise NotImplemented()
    # def get_user(self):
    #     pass
    #
    # def create_user(self):
    #     pass


class IApplicationAuthProvider:
    def get_access_token(self):
        raise NotImplemented()

    def create_user(self, username, fullname, email, password, role="View"):
        raise NotImplemented()

    def reset_password(self, ms_id, password):
        raise NotImplemented()


from microsoft_auth.models import MicrosoftAccount

from Common.utils import decrypt
from apps.user.models import ComplianceGroup
from apps.user.models import User
from .GraphApiClient import GraphApiClient as gac


class ADApplicationAuthProvider(IApplicationAuthProvider):
    def __init__(self, tenant):
        self.__request_headers = {'Authorization': ''}
        self.__scope = ['openid%20offline_access%20%20email%20profile%20User.Read']
        self.__Token = None
        self.Tenant = tenant
        self.__ms_tenant_id = decrypt(tenant.MICROSOFT_AUTH_TENANT_ID)
        self.__client_id = decrypt(tenant.MICROSOFT_AUTH_CLIENT_ID)
        self.__client_secret = decrypt(tenant.MICROSOFT_AUTH_CLIENT_SECRET)
        self.__authority = 'https://login.microsoftonline.com/' + self.__ms_tenant_id
        self.__client = gac(self.__client_id, self.__client_secret, account_type=self.__ms_tenant_id)

    def get_access_token(self):
        self.__Token = self.__client.authenticate_app()
        self.__client.set_token(self.__Token)
        return self.__Token

    def reset_password(self, ms_id, password):
        try:
            self.__acquire_token()
            return self.__client.reset_password(ms_id, password)
        except Exception as e:
            pass

    def create_user(self, username, fullname, email, password, role=settings.AZURE_AD_ROLES['Admin']):
        self.__acquire_token()
        try:
            ad_response = self.__client.get_userByPrincipleIdOrId(email)
            is_created = True
        except Exception as e:
            is_created = False

        if is_created:
            raise Exception("Azure Active directory user already created for {}".format(email))

        ad_response = self.__client.create_user(email, username, fullname, password, accountEnabled=True)
        ms_user = self.__get_microsoft_user(ad_response)

        # self.assign_to_app(ms_user)
        return ms_user.user, ad_response

    def __acquire_token(self):
        if not self.__Token:
            return self.get_access_token()
        return self.__Token

    def __get_microsoft_user(self, data):
        microsoft_user = None
        microsoft_user, created = MicrosoftAccount.objects.get_or_create(
            microsoft_id=data["id"]
        )

        if microsoft_user.user is None:
            self.__verify_microsoft_user(microsoft_user, data)
        return microsoft_user

    def __verify_microsoft_user(self, microsoft_user, data):
        user = microsoft_user.user
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

                try:
                    if user.microsoft_account:
                        user.microsoft_account.delete()
                except:
                    pass

                if user.first_name == "" and user.last_name == "":
                    user.first_name = first_name
                    user.last_name = last_name
                    user.Tenant = self.Tenant
                    user.save()
            except User.DoesNotExist:
                user = User(
                    username=data["userPrincipalName"],
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.Tenant = self.Tenant
                user.save()
        microsoft_user.user = user
        microsoft_user.save()
        # self.__assign_groups(user)
        return user

    def __assign_groups(self, user):
        groups = self.get_groups()
        user.groups.clear()
        if groups:
            for g in groups['value']:
                if g['displayName'] == settings.AZURE_AD_ROLES["Admin"]:
                    ComplianceGroup.assign_tenant_admin(user, user.Tenant)

                if g['displayName'] == settings.AZURE_AD_ROLES["ViewOnly"]:
                    ComplianceGroup.assign_tenant_view_only(user, user.Tenant)

    def get_groups(self, groupName=''):
        self.__acquire_token()
        return self.__client.get_groups(filterBydisplayName=groupName)

    def get_member_of(self):
        self.__acquire_token()
        return self.__client.get_member_of()


class ADUserAuthProvider(IUserAuthProvider):

    def __init__(self, tenant, dic_reponse_from_server):
        self.__auth_response = dic_reponse_from_server
        self.__request_headers = {'Authorization': ''}
        self.__scope = ['openid%20offline_access%20%20email%20profile%20User.Read']
        self.__Token = None
        self.Tenant = tenant
        self.__ms_tenant_id = decrypt(tenant.MICROSOFT_AUTH_TENANT_ID)
        self.__client_id = decrypt(tenant.MICROSOFT_AUTH_CLIENT_ID)
        self.__client_secret = decrypt(tenant.MICROSOFT_AUTH_CLIENT_SECRET)
        self.__authority = 'https://login.microsoftonline.com/' + self.__ms_tenant_id
        self.__client = gac(self.__client_id, self.__client_secret, account_type=self.__ms_tenant_id)

    def get_auth_url(self):
        url = self.__client.authorization_url(self.__auth_response['redirect_url'], self.__scope, state=None)

    def get_access_token(self):
        self.__Token = self.__client.exchange_code(self.__auth_response['redirect_url'], self.__auth_response["code"])

        if self.__Token['access_token']:
            print(self.__Token['access_token'])
            self.__request_headers = {'Authorization': 'Bearer ' + self.__Token['access_token']}
            self.__client.set_token(self.__Token)
        else:
            msg = 'Error aquiring authorization token. Check your tenantID, clientID and clientSecret.'
            print(msg)
            raise Exception(msg)
        # data = {}
        # decodedAccessToken = jwt.decode(data['access_token'], verify=False)
        # accessTokenFormatted = json.dumps(decodedAccessToken, indent=2)
        # print('Decoded Access Token')
        # print(accessTokenFormatted)
        #
        # # Token Expiry
        # tokenExpiry = datetime.fromtimestamp(int(decodedAccessToken['exp']))
        # print('Token Expires at: ' + str(tokenExpiry))
        return self.__Token

    def get_Token(self):
        self.__acquire_token()
        return self.__Token

    def get_user_profile(self):
        self.__acquire_token()
        me = self.__client.get_me()
        return me

    def get_member_of(self):
        self.__acquire_token()
        return self.__client.get_member_of()

    def __acquire_token(self):
        if not self.__Token and self.__auth_response:
            return self.get_access_token()
        return self.__Token

    def sign_in_or_signup(self):
        self.__acquire_token()

        profile = self.get_user_profile()

        ms_user = self.__get_microsoft_user(profile)
        # auth_flow.assign_groups(user.user, data['access_token'])

        # self.__assign_groups(ms_user.user)
        return ms_user.user

    def __get_microsoft_user(self, data):
        microsoft_user = None
        try:
            microsoft_user = MicrosoftAccount.objects.get(
                microsoft_id=data["id"]
            )
        except MicrosoftAccount.DoesNotExist:
            microsoft_user = MicrosoftAccount(microsoft_id=data["id"])
            microsoft_user.save()

        if microsoft_user.user is None:
            self.__verify_microsoft_user(microsoft_user, data)
        return microsoft_user

    def __verify_microsoft_user(self, microsoft_user, data):
        user = microsoft_user.user
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

                try:
                    if user.microsoft_account:
                        user.microsoft_account.delete()
                except:
                    pass
                if user.first_name == "" and user.last_name == "":
                    user.first_name = first_name
                    user.last_name = last_name
                    user.Tenant = self.Tenant
                    user.save()
            except User.DoesNotExist:
                user = User(
                    username=data["userPrincipalName"],
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.Tenant = self.Tenant
                user.save()

        microsoft_user.user = user
        microsoft_user.save()
        return user

    def __assign_groups(self, user):
        groups = self.get_member_of()
        if groups:
            user.groups.clear()
            for g in groups['value']:
                if g['displayName'] == 'ComplianceXAdmin':
                    ComplianceGroup.assign_tenant_admin(user, user.Tenant)
                if g['displayName'] == "ComplianceXViewOnly":
                    ComplianceGroup.assign_tenant_view_only(user, user.Tenant)

    def refresh_token(self, redirect_uri, refresh_token):
        token = self.__client.refresh_token(redirect_uri, refresh_token)
        self.__Token = token
        self.__client.set_token(token)
        return token

    def get_user(self):
        user = self.get_user_profile()
        return self.__get_microsoft_user(user)
