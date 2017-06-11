# coding: utf8
import itchat
from itchat.content import *
import settings as st


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    itchat.send(st.msgs['busy'], msg['FromUserName'])


# itchat.auto_login(enableCmdQR=True, hotReload=True)
itchat.auto_login(enableCmdQR=2, hotReload=True)
itchat.run()
