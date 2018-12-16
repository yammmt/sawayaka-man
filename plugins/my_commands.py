# coding: utf-8


from slackbot.bot import respond_to
from slackbot.bot import listen_to
import bs4
import json
import random
import requests


GENKOTSU_FAIR_URL = "https://www.genkotsu-hb.com/menu/anniversary/"
SAWAYAKA_IMG_URL = [
    "https://i.imgur.com/7iGcSze.jpg",
    "https://i.imgur.com/jDGZaAk.jpg",
    "https://i.imgur.com/IEHfMwl.jpg",
    "https://i.imgur.com/PcC7kj5.jpg",
    "https://i.imgur.com/PMSWINb.jpg",
    "https://i.imgur.com/2rlOPvw.jpg",
    "https://i.imgur.com/8emCYcA.jpg",
    "https://i.imgur.com/NXXP53n.jpg",
    "https://i.imgur.com/HAU2MrA.jpg",
    "https://i.imgur.com/Xll9uq8.jpg"
]


@respond_to(r'fair|festival|げんこつおにぎりフェア')
def fair(message):
    res = requests.get(GENKOTSU_FAIR_URL, verify=False) # bad way...
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    fair_str = soup.select(".leadTxt")[0].getText().replace("\u3000", "")
    message.reply(fair_str)


@respond_to('oniku')
def oniku(message):
    attachments = [{
        "fallback": "Awesome food image.",
        "image_url": SAWAYAKA_IMG_URL[random.randrange(0, len(SAWAYAKA_IMG_URL))]
    }]
    message.send_webapi('Awesome!', json.dumps(attachments))


@listen_to(r'sawayaka|さわやか')
def plus_one(message):
    message.react('+1')
