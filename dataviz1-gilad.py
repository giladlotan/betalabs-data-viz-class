# dataviz1-gilad.py
# 
# Exercise #1 / BetaLabs tutorial: use tweepy to grab Twitter users from specified lists (Betaworks). Save user list to pickled file.

import tweepy
import pickle

# fill these in from Twitter API Dev
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# wanted lists, needed format: '/{owner}/{slug}/members.json'
lists = (('tolar','betaworks'),('mario','betaworks'),('soniasaraiya','betaworks'),('gilgul','betaworks'))

# dictionaries to hold our data
betaworkers = {}
friendships = {}

# grab users from lists
for l in lists:
    owner = l[0]
    slug = l[1]
    
    for page in tweepy.Cursor(api.list_members,owner,slug).pages():
	for user in page:
	    betaworkers[user.id] = user.screen_name


output = open('betaworkers.pkl','wb')
pickle.dump(betaworkers, output)
output.close()

