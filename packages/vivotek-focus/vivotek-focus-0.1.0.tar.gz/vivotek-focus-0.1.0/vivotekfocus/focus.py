import requests, onetrick
import requests.auth
from urllib.parse import urlunparse

PATH = "/cgi-bin/admin/remotefocus.cgi"

@onetrick
def focus(netloc:str, focus:int, username:str, password:str, https=True, verify=True) -> bool:
    components = [
        "https" if https else "http",
        netloc,
        PATH,
        '',
        '',
        ''
    ]

    url = urlunparse(components)

    params = {
        "function":"focus",
        "direction":"direct",
        "position":focus
    }

    auth = requests.auth.HTTPBasicAuth(username, password)
    
    response = requests.get(url, verify=verify, auth=auth, params=params)

    return response.ok