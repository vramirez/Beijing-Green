#A python3 file

import os,configparser,math,sys,time,tweepy,json

config = configparser.RawConfigParser()
config.read('twauth.properties')


consumer_key=config.get('OAuth','key')
consumer_secret=config.get('OAuth','key_secret')
access_key=config.get('OAuth','token')
access_secret=config.get('OAuth','token_secret')


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
