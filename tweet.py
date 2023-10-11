# -*- coding: utf-8 -*-

import os
from datetime import datetime
import tweepy


# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(consumer_key=os.environ["API_KEY"], consumer_secret=os.environ["API_SECRET"])
auth.set_access_token(access_token_key=os.environ["ACCESS_TOKEN"], access_token_secret=os.environ["ACCESS_SECRET"])
api = tweepy.API(auth)

api.update_status("system time is %s" % datetime.now())