from json import loads, dumps
import requests
import os

meta_api_key = os.getenv('META_API_KEY')

def login(key, machine):
    try:
        response = requests.patch(f"https://api.metalabs.io/v4/licenses/{key}",
            headers = {
                "Authorization": meta_api_key,
                "Content-Type": "application/json"
            },
            data = dumps({
                "metadata": {
                    "machine": machine
                }
            })
        )

        print(response.text)
        data = loads(response.text)
        status = data["status"]

        if status == "active" or status == "trialing":
            return data
        else:
            return { "isUser": False }

    except:
        return { "isUser": False }

def reset(key):
    try:
        response = requests.patch(f"https://api.metalabs.io/v4/licenses/{key}",
            headers = {
                "Authorization": meta_api_key,
                "Content-Type": "application/json"
            },
            data = dumps({
                "metadata": {
                    "machine": None
                }
            })
        )

        print(response.text)
        data = loads(response.text)
        status = data["status"]

        if status == "active" or status == "trialing":
            return 200
        else:
            return 404

    except:
        return 404