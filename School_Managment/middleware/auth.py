import re

from django.contrib.auth import get_user_model

from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from django.utils.translation import ugettext_lazy as _


class CustomAuthentication(BaseAuthentication):
    """
    Custom authentication class.
    It will authenticate any incoming request
    as the user given by the username in a
    custom request header.
    """

    def authenticate(self, request):
        """
        Returns a `User` if a correct username and password have been supplied
        using HTTP Basic authentication.  Otherwise returns `None`.
        """

        # Gets authorization from request header
        # and checks different possibility of
        # invalid header.
        # ======================================
        if self.get_authorization_header(request) is None:
            raise exceptions.AuthenticationFailed("Bearer token Not Set!")

        auth = self.get_authorization_header(request).split()

        if not auth or auth[0].lower() != "bearer":
            raise exceptions.AuthenticationFailed(_("Token Is Not Bearer!"))
        if len(auth) == 1:
            msg = _("Invalid basic header. No credentials provided.")
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _(
                "Invalid basic header. Credentials string should not contain spaces."
            )
            raise exceptions.AuthenticationFailed(msg)

        api_token = auth[1]
        if not re.findall(r"([a-fA-F\d]{32})", api_token):
            raise exceptions.AuthenticationFailed(_('api token format not true'))
        user_model = get_user_model()
        target_user = user_model.objects.filter(api_token=api_token).first()
        if not target_user:
            raise exceptions.AuthenticationFailed(_('api token is expired'))

        return target_user, None

    @staticmethod
    def get_authorization_header(request):
        """
        Return request's 'Authorization:' header, as a bytestring.

        Hide some test client ickyness where the header can be unicode.
        """

        auth = request.META.get("HTTP_AUTHORIZATION", )
        # if isinstance(auth, text_type):
        #     # Work around django test client oddness
        #     auth = auth.encode(HTTP_HEADER_ENCODING)
        return auth
