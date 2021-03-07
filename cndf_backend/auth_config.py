from os import environ as env

CLIENT_ID = env.get('GOOGLE_CLIENT_ID')
CLIENT_SECRET = env.get('GOOGLE_SECRET_KEY')
SCOPE = 'https://www.googleapis.com/auth/contacts.readonly'
OAUTH2TOKEN_URL = 'https://oauth2.googleapis.com/token'
GOOGLE_AUTH_URI = 'https://accounts.google.com/o/oauth2/v2/auth?response_type=code'

def google_auth_config(redirect_uri):
    return f'{GOOGLE_AUTH_URI}&client_id={CLIENT_ID}&redirect_uri={redirect_uri}&scope={SCOPE}'


def oauth2_token_config(auth_code, redirect_uri):
    return {'url': OAUTH2TOKEN_URL,
            'data': 
                {'code': auth_code,
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
                'redirect_uri': redirect_uri,
                'grant_type': 'authorization_code'}
            }