#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mastodon_2_album
import yaml
from telegram.ext import Updater
import album_sender

with open('credential') as f:
	credential = yaml.load(f, Loader=yaml.FullLoader)
tele = Updater(credential['bot_token'], use_context=True)
chat = tele.bot.get_chat(-1001198682178)

def test():
    mastodon = Mastodon(
        access_token = 'db/main_mastodon_secret',
        api_base_url = credential['mastodon_domain']
    )
    my_id = mastodon.me().id
    for user in mastodon.account_following(my_id, limit=80):
        statuses = mastodon.account_statuses(user.id, limit=40)
        for status in statuses:
        	# do some test here
        	return
	
if __name__=='__main__':
	test()
	