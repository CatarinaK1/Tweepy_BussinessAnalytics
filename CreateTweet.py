import tweepy
from Credentials import client



response = client.create_tweet(text= 'This is a Tweet!!')

print(response)
