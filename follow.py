import tweepy
import time
import random
from random import randint
from keys import keys

SCREEN_NAME = keys['screen_name']
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
followers = api.followers_ids(SCREEN_NAME)
friends = api.friends_ids(SCREEN_NAME)

for f in followers:
    if f not in friends:
        print "{0}".format(api.get_user(f).screen_name)
        api.create_friendship(f)
        time.sleep(randint(5, 25))
print "no one left to follow"
