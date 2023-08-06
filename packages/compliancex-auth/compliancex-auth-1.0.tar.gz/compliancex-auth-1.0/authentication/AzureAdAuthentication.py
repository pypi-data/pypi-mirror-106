from django.contrib.auth import get_user_model
from django.utils.encoding import smart_text
from django.utils.translation import ugettext as _
from jwt.exceptions import (
    ExpiredSignatureError,

)
from microsoft_auth.models import MicrosoftAccount
from rest_framework import exceptions
from rest_framework.authentication import (
    BaseAuthentication, get_authorization_header
)
from rest_framework_jwt.settings import api_settings

from .GraphApiModel import OAuthFlow
from Common.utils import get_tenant_config


class ADBaseJSONWebTokenAuthentication(BaseAuthentication):
    """
    Token based authentication using the JSON Web Token standard.
    """

    def authenticate(self, request):
        """
        Returns a two-tuple of `User` and token if a valid signature has been
        supplied using JWT-based authentication.  Otherwise returns `None`.
        """

        try:
            jwt_value = self.get_jwt_value(request)
            if jwt_value is None:
                return None

        except Exception as e:
            return None
        try:
            if api_settings.JWT_DECODE_HANDLER:
                parsed_jwt = api_settings.JWT_DECODE_HANDLER(jwt_value)
                is_internal_token = parsed_jwt.get('source') == 'complianceXInternal'
                if is_internal_token:
                    return None
        except Exception as e:
            pass
        
        try:
            tenant, tenant_id, client_id, client_sec = get_tenant_config(request)
            auth_flow = OAuthFlow(tenant_id, client_id, client_sec)
            jwt_token = jwt_value.decode("utf-8")
            payload = auth_flow.get_profile(jwt_token)
        except ExpiredSignatureError as e:
            msg = _('Signature has expired.')
            return None
        except Exception as e:
            msg = _(str(e))
            return None

        user = self.authenticate_credentials(payload)

        return (user, jwt_token)

    def jwt_decode_handler(self, jwt_value):
        pass

    def authenticate_credentials(self, payload):
        """
        Returns an active user that matches the payload's user id and email.
        """
        User = get_user_model()
        userid = self.jwt_get_username_from_payload(payload)

        if not userid:
            msg = _('Invalid payload.')
            raise exceptions.AuthenticationFailed(msg)

        microsoft_user = MicrosoftAccount.objects.filter(
            microsoft_id=userid
        )[0]

        if not microsoft_user:
            msg = _('Invalid payload.')
            raise exceptions.AuthenticationFailed(msg)

        user = microsoft_user.user
        if not user.Tenant or not user.Tenant.Enabled \
                or not user.Tenant.Status or \
                user.Tenant.Status == 'Inactive' \
                or user.Tenant.Status == 'Suspended':
            msg = _('Tenant is disabled or Inactive or Suspended.')
            raise exceptions.AuthenticationFailed(msg)
        if not user:
            msg = _('Invalid payload.')
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = _('User account is disabled.')
            raise exceptions.AuthenticationFailed(msg)
        return user

    def jwt_get_username_from_payload(self, payload):
        userId = ""
        try:
            userId = payload['id']
        except Exception as e:
            userId = payload["upn"]
        return userId


class AzureAdAuthentication(ADBaseJSONWebTokenAuthentication):
    """
    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string specified in the setting
    `JWT_AUTH_HEADER_PREFIX`. For example:

        Authorization: JWT eyJhbGciOiAiSFMyNTYiLCAidHlwIj
    """
    www_authenticate_realm = 'api'

    def get_jwt_value(self, request):
        auth = get_authorization_header(request).split()
        auth_header_prefix = api_settings.JWT_AUTH_HEADER_PREFIX.lower()

        if not auth:
            if api_settings.JWT_AUTH_COOKIE:
                return request.COOKIES.get(api_settings.JWT_AUTH_COOKIE)
            return None

        if smart_text(auth[0].lower()) != auth_header_prefix:
            return None

        if len(auth) == 1:
            msg = _('Invalid Authorization header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid Authorization header. Credentials string '
                    'should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        return auth[1]

    def authenticate_header(self, request):
        """
        Return a string to be used as the value of the `WWW-Authenticate`
        header in a `401 Unauthenticated` response, or `None` if the
        authentication scheme should return `403 Permission Denied` responses.
        """
        return '{0} realm="{1}"'.format(api_settings.JWT_AUTH_HEADER_PREFIX, self.www_authenticate_realm)
