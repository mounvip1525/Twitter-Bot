import tweepy
import time

consumer_key='icFfgegzBRZ8Dzo0nvDKYfKvH'
consumer_secret='MOZtDFBC04VtHkrpz1NUl2VS4vnj1A79F7pE3NBbobTzdwcxVd'
key='3231815648-f6GFawi7aOMWiRmeZ335Iscs0dNfYiBGA810Zc6'
secret='ZcSp8nt695qGSlLtt6vLB1gpqIJacSbjlJQqUgpdRtqo5'

#Using the keys and tokens for twitter authentication and generate an api through which we can read, write and perform other functionalities
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

hashtag=('100daysofcode','python','javascript','bot')
tweetNumber=10

tweets=tweepy.Cursor(api.search,hashtag).items(tweetNumber) #search 5 tweets with the hashtag python and to retweet them

def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print('Retweeted')
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)
searchbot()