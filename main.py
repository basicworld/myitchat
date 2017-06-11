# coding: utf8
import os
import sys
import time
import itchat
import settings as st
import utils as ut
reload(sys)
sys.setdefaultencoding('utf8')
ut.makesure_env()


@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing', ])
def text_reply(msg):
    """
    自动回复消息
    """
    itchat.send(st.msgs['rest'], msg['FromUserName'])


@itchat.msg_register(['Picture', 'Recording', 'Attachment', ])
def download_files(msg):
    """
    下载多媒体附件
    """
    filename = '_'.join([msg['User']['RemarkName'] or msg['User']['NickName'], ut.timestamp2str(msg['CreateTime']), msg['FileName']])
    full_filename = os.path.join(st.downloads_dir, filename)
    msg['Text'](full_filename)

    itchat.send('@%s@%s' % ('img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']), msg['FromUserName'])
    itchat.send(st.msgs['received'], msg['FromUserName'])


@itchat.msg_register(['Video', ])
def show_files(msg):
    """
    视频不做处理
    """
    itchat.send('@%s@%s' % ('img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']), msg['FromUserName'])


def lc():
    print('finish login')


def ec():
    print('exit')

# itchat.auto_login()
# itchat.auto_login(enableCmdQR=True, hotReload=True)
itchat.auto_login(hotReload=True, loginCallback=lc, exitCallback=ec)
itchat.run()
