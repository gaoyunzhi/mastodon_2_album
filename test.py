#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import twitter_2_album
import yaml
from telegram.ext import Updater
import album_sender

with open('CREDENTIALS') as f:
	CREDENTIALS = yaml.load(f, Loader=yaml.FullLoader)
tele = Updater(CREDENTIALS['bot_token'], use_context=True)
chat = tele.bot.get_chat(-1001198682178)
# chat = tele.bot.get_chat('@web_record')

def test(url, rotate=False):
	r = twitter_2_album.get(url, origin=['twitter_read'])
	print(r)
	album_sender.send_v2(chat, r, rotate = rotate)
	
if __name__=='__main__':
	# test('https://twitter.com/xyczgmyx1/status/1556214056008052736') 
	test('http://twitter.com/Jason_changgggg/status/1615896133384945666')
	