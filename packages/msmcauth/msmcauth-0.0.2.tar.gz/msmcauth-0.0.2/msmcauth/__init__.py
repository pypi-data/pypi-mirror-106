from msmcauth.microsoft import Microsoft
from msmcauth.xbox import XboxLive
from msmcauth.consts import userAgent, Authorize, ownership, login_with_xbox, profile, Xbl, Xsts
from msmcauth.types import PreAuthResponse, UserProfile, UserLoginResponse, XSTSAuthenticateResponse, XblAuthenticateResponse
from requests import Session

def login(email: str, password: str, client = None):
    """
    :param str email: Email for authorize
    :param str password: password for authorize
    :param client: Requests session, Default `requests.Session`
    """
    
    try:
        client = client if client != None else Session()
        
        xbx = XboxLive(client)
        mic = Microsoft(client)

        login = xbx.user_login(email, password, xbx.pre_auth())

        xbl = mic.xbl_authenticate(login)
        xsts = mic.xsts_authenticate(xbl)
        
        access_token = mic.login_with_xbox(xsts.token, xsts.user_hash)
        hasGame = mic.user_hash_game(access_token)
        
        if hasGame:
            profile = mic.get_user_profile(access_token)
            data = {
                "access_token": access_token,
                "username": profile.username,
                "uuid": profile.uuid
            }

            return data
        else:
            return "Not a premium account"
    except Exception as ex:
        return f"Microsoft authenticate failed: {str(ex)}"