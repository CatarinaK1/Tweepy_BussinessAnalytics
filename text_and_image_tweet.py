import tweepy
#from Credentials import client
from Credentials import *


# We shall insert the keys necessary to publish the tweet
auth = tweepy.OAuthHandler(consumer_key, consumer_secret )

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit= True)

client = tweepy.Client( bearer_token, consumer_key, consumer_secret, access_token, access_token_secret, wait_on_rate_limit= True)

# Here we add the image that will be uploaded
media_id = api.media_upload( filename = 'fine.jpeg').media_id_string

print(media_id)

# Here is the text that will be included in that same tweet
text = 'Testing media upload'

# Here we insert the text and image that will be published in the tweet
client.create_tweet( text = text, media_ids = [media_id])

print('Tweet published successfully')
