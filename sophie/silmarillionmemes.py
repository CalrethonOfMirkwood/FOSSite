import requests, random

def getReddit():
    request = requests.get(f'https://www.reddit.com/r/silmarillionmemes/top.json?limit=1&t=day', headers = {'User-agent': 'bruh'})
    return request.json()

def getResults(redditdata):
    for post in redditdata['data']['children']:
        rtitle = post['data']['title']
        rurl = post['data']['url']
    return (rtitle, rurl)

def getSilmMeme():
    redditdata = getReddit()
    (title, url) = getResults(redditdata)
    return (title, url)

def noldolante():
    songs = ("{{url_for('sophie.static', filename='badapple.mp3')}}",
             "{{url_for('sophie.static', filename='beastars.mp3')}}",
             '/static/sophiemusic/BLOODYSTREAM.mp3',
             '/static/sophiemusic/connect.mp3',
             '/static/sophiemusic/dadadadatenshi.mp3',
             '/static/sophiemusic/daddy.mp3',
             '/static/sophiemusic/fmaending.mp3',
             '/static/sophiemusic/fmaopening.mp3',
             '/static/sophiemusic/insaeng.mp3',
             '/static/sophiemusic/mincho.mp3',
             '/static/sophiemusic/klk.mp3',
             '/static/sophiemusic/onewingedangeladvent.mp3',
             '/static/sophiemusic/opm.mp3',
             '/static/sophiemusic/pandf.mp3',
             '/static/sophiemusic/parttimer.mp3',
             '/static/sophiemusic/puff.mp3',
             '/static/sophiemusic/requiem.mp3',
             '/static/sophiemusic/resonance.mp3',
             '/static/sophiemusic/sasageyo.mp3',
             '/static/sophiemusic/takingthehobbitstoisengard.mp3',
             '/static/sophiemusic/yumiya.mp3')

    return random.choice(songs)