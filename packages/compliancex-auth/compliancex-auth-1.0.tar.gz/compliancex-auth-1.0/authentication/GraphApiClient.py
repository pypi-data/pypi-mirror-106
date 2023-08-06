from urllib.parse import urlencode

import requests

from .decorators import token_required
from .exceptions import *


class GraphApiClient(object):
    AUTHORITY_URL = 'https://login.microsoftonline.com/'
    AUTH_ENDPOINT = '/oauth2/v2.0/authorize?'
    TOKEN_ENDPOINT = '/oauth2/v2.0/token'
    RESOURCE = 'https://graph.microsoft.com/'

    def __init__(self, client_id, client_secret, api_version='v1.0', account_type='common', office365=False):
        self.client_id = client_id
        self.client_secret = client_secret
        self.api_version = api_version
        self.account_type = account_type

        self.base_url = self.RESOURCE + self.api_version + '/'
        self.token = None
        self.office365 = office365
        self.office365_token = None

    def authorization_url(self, redirect_uri, scope, state=None):
        """

        Args:
            redirect_uri: The redirect_uri of your app, where authentication responses can be sent and received by
            your app.  It must exactly match one of the redirect_uris you registered in the app registration portal

            scope: A list of the Microsoft Graph permissions that you want the user to consent to. This may also
            include OpenID scopes.

            state: A value included in the request that will also be returned in the token response.
            It can be a string of any content that you wish.  A randomly generated unique value is typically
            used for preventing cross-site request forgery attacks.  The state is also used to encode information
            about the user's state in the app before the authentication request occurred, such as the page or view
            they were on.

        Returns:
            A string.

        """
        params = {
            'client_id': self.client_id,
            'redirect_uri': redirect_uri,
            'scope': ' '.join(scope),
            'response_type': 'code',
            'response_mode': 'query'
        }

        if state:
            params['state'] = state
        if self.office365:
            response = self.OFFICE365_AUTHORITY_URL + self.OFFICE365_AUTH_ENDPOINT + urlencode(params)
        else:
            response = self.AUTHORITY_URL + self.account_type + self.AUTH_ENDPOINT + urlencode(params)
        return response

    def authenticate_app(self):
        """Get Token for Application
                Returns:
                    A dict.
                """
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scope': 'https://graph.microsoft.com/.default'
        }
        if self.office365:
            response = requests.post(self.OFFICE365_AUTHORITY_URL + self.OFFICE365_TOKEN_ENDPOINT, data=data)
        else:
            response = requests.post(self.AUTHORITY_URL + self.account_type + self.TOKEN_ENDPOINT, data=data)
        return self._parse(response)

    def exchange_code(self, redirect_uri, code):
        """Exchanges a code for a Token.

        Args:
            redirect_uri: The redirect_uri of your app, where authentication responses can be sent and received by
            your app.  It must exactly match one of the redirect_uris you registered in the app registration portal

            code: The authorization_code that you acquired in the first leg of the flow.

        Returns:
            A dict.

        """
        data = {
            'client_id': self.client_id,
            'redirect_uri': redirect_uri,
            'client_secret': self.client_secret,
            'code': code,
            'grant_type': 'authorization_code',
        }
        if self.office365:
            response = requests.post(self.OFFICE365_AUTHORITY_URL + self.OFFICE365_TOKEN_ENDPOINT, data=data)
        else:
            response = requests.post(self.AUTHORITY_URL + self.account_type + self.TOKEN_ENDPOINT, data=data)
        return self._parse(response)

    def refresh_token(self, redirect_uri, refresh_token):
        """

        Args:
            redirect_uri: The redirect_uri of your app, where authentication responses can be sent and received by
            your app.  It must exactly match one of the redirect_uris you registered in the app registration portal

            refresh_token: An OAuth 2.0 refresh token. Your app can use this token acquire additional access tokens
            after the current access token expires. Refresh tokens are long-lived, and can be used to retain access
            to resources for extended periods of time.

        Returns:
            A dict.

        """
        data = {
            'client_id': self.client_id,
            'redirect_uri': redirect_uri,
            'client_secret': self.client_secret,
            'refresh_token': refresh_token,
            'grant_type': 'refresh_token',
        }
        if self.office365:
            response = requests.post(self.OFFICE365_AUTHORITY_URL + self.OFFICE365_TOKEN_ENDPOINT, data=data)
        else:
            response = requests.post(self.AUTHORITY_URL + self.account_type + self.TOKEN_ENDPOINT, data=data)
        return self._parse(response)

    def set_token(self, token):
        """Sets the Token for its use in this library.

        Args:
            token: A string with the Token.

        """
        if self.office365:
            self.office365_token = token
        else:
            self.token = token

    @token_required
    def reset_password(self, id, password):
        """Get Token for Application
                Returns:
                    A dict.
                """
        data = {
            "passwordProfile": {
                "forceChangePasswordNextSignIn": True,
                "password": password
            }
        }

        response = self._patch( self.base_url+"users/{}".format(id), json=data)
        return self._parse(response)

    @token_required
    def get_userByPrincipleIdOrId(self, userIdOrPrincipleName, params=None):
        """Retrieve the properties and relationships of user object.

        Note: Getting a user returns a default set of properties only (businessPhones, displayName, givenName, id,
        jobTitle, mail, mobilePhone, officeLocation, preferredLanguage, surname, userPrincipalName).
        Use $select to get the other properties and relationships for the user object.

        Args:
            params: A dict.

        Returns:
            A dict.

        """
        return self._get(self.base_url + 'Users/{}'.format(userIdOrPrincipleName), params=params)

    @token_required
    def get_me(self, params=None):
        """Retrieve the properties and relationships of user object.

        Note: Getting a user returns a default set of properties only (businessPhones, displayName, givenName, id,
        jobTitle, mail, mobilePhone, officeLocation, preferredLanguage, surname, userPrincipalName).
        Use $select to get the other properties and relationships for the user object.

        Args:
            params: A dict.

        Returns:
            A dict.

        """
        return self._get(self.base_url + 'me')

    @token_required
    def create_user(self, email, fname, displayname, password, accountEnabled: True):
        """Create User

        Args:
            params: A dict.
        Returns:
            A dict.
        """
        data = {
            "accountEnabled": accountEnabled,
            "displayName": displayname,
            "mailNickname": fname,
            "userPrincipalName": email,
            "passwordProfile": {
                "forceChangePasswordNextSignIn": True,
                "password": password
            }
        }
        response = self._post(self.base_url + 'users', json=data)

        return self._parse(response) if response.get("status_code", None) else response

    @token_required
    def get_groups(self, filterBydisplayName=''):

        """Retrieve groups & subscription of user object.

        Note:

        Returns:
            A dict.

        """
        uri = "groups/?$filter=startsWith(displayName,'{}')".format(
            filterBydisplayName) if filterBydisplayName else 'groups'

        return self._get(self.base_url + uri)

    @token_required
    def get_member_of(self):

        """Retrieve groups & subscription of user object.

        Note:

        Returns:
            A dict.

        """

        return self._get(self.base_url + 'me/memberOf')

    @token_required
    def get_message(self, message_id, params=None):
        """Retrieve the properties and relationships of a message object.

        Args:
            message_id: A dict.
            params:

        Returns:
            A dict.

        """
        return self._get(self.base_url + 'me/messages/' + message_id, params=params)

    def _get(self, url, **kwargs):
        return self._request('GET', url, **kwargs)

    def _post(self, url, **kwargs):
        return self._request('POST', url, **kwargs)

    def _put(self, url, **kwargs):
        return self._request('PUT', url, **kwargs)

    def _patch(self, url, **kwargs):
        return self._request('PATCH', url, **kwargs)

    def _delete(self, url, **kwargs):
        return self._request('DELETE', url, **kwargs)

    def _request(self, method, url, headers=None, **kwargs):
        _headers = {
            'Accept': 'application/json',
        }
        if self.office365:
            _headers['Authorization'] = 'Bearer ' + self.office365_token['access_token']
        else:
            _headers['Authorization'] = 'Bearer ' + self.token['access_token']
        if headers:
            _headers.update(headers)
        if 'files' not in kwargs:
            # If you use the 'files' keyword, the library will set the Content-Type to multipart/form-data
            # and will generate a boundary.
            _headers['Content-Type'] = 'application/json'
        return self._parse(requests.request(method, url, headers=_headers, **kwargs))

    def _parse(self, response):
        status_code = response.status_code
        if 'application/json' in response.headers['Content-Type']:
            r = response.json()
        else:
            r = response.content
        if status_code in (200, 201, 202):
            return r
        elif status_code == 204:
            return None
        elif status_code == 400:
            raise BadRequest(r)
        elif status_code == 401:
            raise Unauthorized(r)
        elif status_code == 403:
            raise Forbidden(r)
        elif status_code == 404:
            raise NotFound(r)
        elif status_code == 405:
            raise MethodNotAllowed(r)
        elif status_code == 406:
            raise NotAcceptable(r)
        elif status_code == 409:
            raise Conflict(r)
        elif status_code == 410:
            raise Gone(r)
        elif status_code == 411:
            raise LengthRequired(r)
        elif status_code == 412:
            raise PreconditionFailed(r)
        elif status_code == 413:
            raise RequestEntityTooLarge(r)
        elif status_code == 415:
            raise UnsupportedMediaType(r)
        elif status_code == 416:
            raise RequestedRangeNotSatisfiable(r)
        elif status_code == 422:
            raise UnprocessableEntity(r)
        elif status_code == 429:
            raise TooManyRequests(r)
        elif status_code == 500:
            raise InternalServerError(r)
        elif status_code == 501:
            raise NotImplemented(r)
        elif status_code == 503:
            raise ServiceUnavailable(r)
        elif status_code == 504:
            raise GatewayTimeout(r)
        elif status_code == 507:
            raise InsufficientStorage(r)
        elif status_code == 509:
            raise BandwidthLimitExceeded(r)
        else:
            if r['error']['innerError']['code'] == 'lockMismatch':
                # File is currently locked due to being open in the web browser
                # while attempting to reupload a new version to the drive.
                # Thus temporarily unavailable.
                raise ServiceUnavailable(r)
            raise UnknownError(r)
