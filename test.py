#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mastodon_2_album
import yaml
from telegram.ext import Updater
import album_sender
from mastodon import Mastodon

with open('credential') as f:
    credential = yaml.load(f, Loader=yaml.FullLoader)
tele = Updater(credential['bot_token'], use_context=True)
chat = tele.bot.get_chat(credential['debug_group'])

def testImp(status):
    result = mastodon_2_album.get(status)
    print(result)
    album_sender.send_v2(chat, result)

def test():
    mastodon = Mastodon(
        access_token = 'db/main_mastodon_secret',
        api_base_url = credential['mastodon_domain']
    )
    my_id = mastodon.me().id
    for user in mastodon.account_following(my_id, limit=80):
        statuses = mastodon.account_statuses(user.id, limit=40)
        for status in statuses:
            testImp(status)
            return

def testFindAccount(text):
    mastodon = Mastodon(
        access_token = 'db/main_mastodon_secret',
        api_base_url = credential['mastodon_domain']
    )
    print(mastodon_2_album.findAccount(mastodon, text))

def testStatusGet(status_search_key):
    mastodon = Mastodon(
        access_token = 'db/main_mastodon_secret',
        api_base_url = credential['mastodon_domain']
    )
    status = mastodon.search_v2(status_search_key)['statuses'][0]
    testImp(status)
    
if __name__=='__main__':
    # test()
    # testFindAccount('79470')
    testStatusGet('https://bgme.me/@ShrimpZhou/107432772239009987')