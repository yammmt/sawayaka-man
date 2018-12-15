# coding: utf-8


from slackbot.bot import respond_to
from slackbot.bot import listen_to


@respond_to('oniku')
def oniku_func(message):
    message.reply('delicious!')


@listen_to(r'sawayaka|さわやか')
def plus_one_func(message):
    message.react('+1')
