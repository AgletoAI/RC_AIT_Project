import requests

def call_api(api_url, params):
    response = requests.get(api_url, params=params)
    return response.json()
