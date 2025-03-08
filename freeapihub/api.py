import requests

async def getUser():
    response = requests.get("api.url")
    return response.json();
