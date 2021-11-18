import requests, json

def getReddit():
    try:
        request = requests.get(f'https://www.reddit.com/r/silmarillionmemes/top.json?limit=1&t=day', headers = {'User-agent': 'bruh'})
    except:
        print('An Error Occurred')
    return request.json()

def getResults(redditdata):
    myDict = {}
    for post in redditdata['data']['children']:
        rtitle = post['data']['title']
        rurl = post['data']['url']
    return (rtitle, rurl)

def getSilmMeme():
    SilmarillionMeme = getReddit()
    (title, url) = getResults(SilmarillionMeme)
    return (title, url)