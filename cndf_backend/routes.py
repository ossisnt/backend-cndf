import json
import requests

from collections import defaultdict
from flask import url_for, redirect, session, request

from cndf_backend import app
from cndf_backend.auth_config import google_auth_config, oauth2_token_config


@app.route('/')
def index():
    if 'credentials' not in session:
        return redirect(url_for('oauth2callback'))
    credentials = json.loads(session['credentials'])

    if credentials['expires_in'] <= 0:
        return redirect(url_for('oauth2callback'))
    else:
        headers = {'Authorization': f'Bearer {credentials["access_token"]}'}
        req_uri = 'https://people.googleapis.com/v1/people/me/connections?personFields=emailAddresses'
        r = requests.get(req_uri, headers=headers)
        r = r.json()
        r = r['connections']

        data = defaultdict(list)

        for x in r:
            if 'emailAddresses' in x.keys():
                email = x['emailAddresses'][0]['value']
                data[email.split("@")[1]].append(email)

        return {'data': data, 'status': 'success'}


@app.route('/auth/google')
def oauth2callback():
    REDIRECT_URI = f'{request.url_root}{url_for("oauth2callback")[1:]}'

    if 'code' not in request.args:
        auth_uri = google_auth_config(REDIRECT_URI)

        return redirect(auth_uri)

    else:
        auth_code = request.args.get('code')
        config = oauth2_token_config(auth_code, REDIRECT_URI)
        r = requests.post(config['url'], data=config['data'])
        session['credentials'] = r.text

        return redirect(url_for('index'))

