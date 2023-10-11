# -*- coding: utf-8 -*-

import os
from datetime import datetime

import twitter


api = twitter.Api(consumer_key=os.environ["API_KEY"],
                  consumer_secret=os.environ["API_SECRET"],
                  access_token_key=os.environ["ACCESS_TOKEN"],
                  access_token_secret=os.environ["ACCESS_SECRET"]
                  )
api.PostUpdate("system time is %s" % datetime.now())