import requests

def get_response(url):
    try:
        response = requests.get(url)
    except:
        response = None
    return response
