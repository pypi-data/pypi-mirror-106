from .IAuthProvider import ADUserAuthProvider as aduap, ADApplicationAuthProvider


def get_user_authentication_provider(tenant, params):
    return aduap(tenant, params)


def get_application_authentication_provicer(tenant ):
    return ADApplicationAuthProvider(tenant)
