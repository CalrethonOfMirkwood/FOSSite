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
    songs = ('assets/sophiemusic/badapple.mp3',
             'assets/sophiemusic/beastars.mp3',
             'assets/sophiemusic/BLOODYSTREAM.mp3',
             'assets/sophiemusic/connect.mp3',
             'assets/sophiemusic/dadadadatenshi.mp3',
             'assets/sophiemusic/daddy.mp3',
             'assets/sophiemusic/electricangel.mp3',
             'assets/sophiemusic/fmaending.mp3',
             'assets/sophiemusic/fmaopening.mp3',
             'assets/sophiemusic/freesoftware.mp3',
             'assets/sophiemusic/gopnik.mp3',
             'assets/sophiemusic/insaeng.mp3',
             'assets/sophiemusic/mincho.mp3',
             'assets/sophiemusic/klk.mp3',
             'assets/sophiemusic/mataashite.mp3',
             'assets/sophiemusic/onewingedangeladvent.mp3',
             'assets/sophiemusic/opm.mp3',
             'assets/sophiemusic/pandf.mp3',
             'assets/sophiemusic/parttimer.mp3',
             'assets/sophiemusic/puff.mp3',
             'assets/sophiemusic/rat.mp3',
             'assets/sophiemusic/requiem.mp3',
             'assets/sophiemusic/resonance.mp3',
             'assets/sophiemusic/sasageyo.mp3',
             'assets/sophiemusic/takingthehobbitstoisengard.mp3',
             'assets/sophiemusic/tiger.mp3',
             'assets/sophiemusic/yumiya.mp3')

    return random.choice(songs)