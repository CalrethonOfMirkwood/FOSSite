import requests

def getReddit():
    request = requests.get(f'https://bible-api.com/john%203:16', headers = {'User-agent': 'brap'})
    return request.json()

def getResults(versejson):
    for verse in versejson['verses']['text']:
        rtitle = post['data']['title']
        rurl = post['data']['url']
    return (rtitle, rurl)