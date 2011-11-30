# dataviz2-gilad.py
# 
# Exercise #2 / BetaLabs tutorial: iterate over a list of Twitter users (in this case, the list we pickled in #1) and grab the list of people they follow. Save only the relevant subset.

import tweepy
import pickle

# fill these in from Twitter API Dev
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

# setup connection to Twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# unpickle the betaworkers list
f = open('betaworkers.pkl','rb')
betaworkers = pickle.load(f)
f.close()

# dictionary to hold the friendships data
friendships = {}

# iterate over list of betaworks users
for curID,curUser in betaworkers.items():
    
    # array to store friendships
    friendships[curUser]=[]
    
    # for every user, iterate over list of people they follow
    for id in tweepy.Cursor(api.friends_ids,id=curID).items():
	
	# only save ids of other betaworkers
	if id in betaworkers.keys():
	    friendships[curUser].append(betaworkers[id])
	    
# pickle friendships
f = open('friendships.pkl','wb')
pickle.dump(friendships,f)
f.close()
