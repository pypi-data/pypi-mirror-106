from rest_framework import serializers


class SsoAdAuthSerializer(serializers.Serializer):
    code = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True,
    )
    redirectURL = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True,
    )
    state = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True,
    )
    session_state = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True,
    )


class SsoRefreshTokenSerializer(serializers.Serializer):
    refreshToken = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True,
    )
