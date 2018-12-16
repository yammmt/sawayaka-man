# coding: utf-8


from slackbot.bot import respond_to
from slackbot.bot import listen_to
import json
import random


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
