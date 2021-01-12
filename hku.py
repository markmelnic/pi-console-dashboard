import requests, json

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/vnd.heroku+json; version=3"
    }

def fetch_heroku():
    req = requests.get("https://api.heroku.com/apps", headers = HEADERS)
    content = json.loads(req.content)
    return [(i['name'], i['acm']) for i in content]
