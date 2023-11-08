import tweepy
from Credentials import client
import Credentials

#In here we create a reply to a specific tweet we have created we inset the tweet's id in the in_reply_to_tweet_id field
response = client.create_tweet( text = 'Testing a reply!!!', in_reply_to_tweet_id='TWEETID')

print(response)