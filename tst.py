import tweepy
import json

from tweepy import OAuthHandler

consumer_key = 'fjAE2wsNO0yQGcK9vXYMJzuCy'
consumer_secret = 'oNKFPbejfqqPfybq0YxAGEYUcqM5DDO9dfqXEtik8joJgPCrUh'
access_token = '2859185412-enPqXdVU93klZVZ8TEMRlzd23h2JcYayqQsecvG'
access_secret = 'SaacgVZxEhcpnCTX8JIi8Z01Ct8SUett7arqbxWI4L8kz'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api=tweepy.API(auth)



def store_json(tweet):
	with open('mytweets.json','a') as f:
		f.write(json.dumps(tweet))
		f.write('\n')
		return True
	f.close()

for indexes in range(0,10):
	for status in tweepy.Cursor(api.home_timeline).items(1):
		store_json(status._json)




