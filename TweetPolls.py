import tweepy
from Credentials import *


response = client.create_tweet( text="Tweeting with polls for my Assignment!!!", poll_options = ["yeees", "maybe", "nooo"], poll_duration_minutes = 120 )

print(response)