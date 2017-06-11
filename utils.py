# coding: utf8
import settings as st
import os
import time
import functools


def timestamp2str(stamp, strf_type="%Y-%m-%d %H-%M-%S"):
    time_array = time.localtime(stamp)
    return time.strftime(strf_type, time_array)


def makesure_env():
    if not os.path.isdir(st.downloads_dir):
        os.makedirs(st.downloads_dir)


def print_msg(func):
    # http://itchat.readthedocs.io/zh/latest/intro/messages/
    @functools.wraps(func)
    def wrapper(msg, *args, **kwargs):
        print timestamp2str(msg['CreateTime'], strf_type="%Y-%m-%d %H:%M:%S")
        username = (msg['User']['RemarkName'] or msg['User']['NickName'])
        if msg['MsgType'] == 1:  # text map
            print '%s: %s' % (username, msg['Content'])
        elif msg['MsgType'] == 3:  # picture
            print '%s: %s' % (username, '<Picture>')
        elif msg['MsgType'] == 62:  # small video
            print '%s: %s' % (username, '<SmallVideo>')
        elif msg['MsgType'] == 42:  # idcard
            print '%s: <RecommendInfo: %s>' % (username, msg['Text']['NickName'])
        elif msg['MsgType'] == 43:  # video
            print '%s: %s' % (username, '<Video>')
        else:
            print msg
            print '%s: %s' % (username, msg['Content'])
        return func(msg, *args, **kwargs)
    return wrapper
