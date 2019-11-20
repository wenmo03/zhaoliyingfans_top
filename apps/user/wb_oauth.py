import requests
import json


class OAuthWB:
    def __init__(self, client_id, client_key, redirect_uri):
        self.client_id = client_id
        self.client_key = client_key
        self.redirect_uri = redirect_uri

    def get_access_token(self, code):  # 获取用户token和uid
        url = "https://api.weibo.com/oauth2/access_token"

        querystring = {
            "client_id": self.client_id,
            "client_secret": self.client_key,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self.redirect_uri
        }

        response = requests.request("POST", url, params=querystring)

        return json.loads(response.text)

    def get_user_info(self, access_token_data):
        url = "https://api.weibo.com/2/users/show.json"

        querystring = {
            "uid": access_token_data['uid'],
            "access_token": access_token_data['access_token']
        }

        response = requests.request("GET", url, params=querystring)

        return json.loads(response.text)
