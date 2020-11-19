#Bot account- @MythiliSudhan
import tweepy

consumer_key='icFfgegzBRZ8Dzo0nvDKYfKvH'
consumer_secret='MOZtDFBC04VtHkrpz1NUl2VS4vnj1A79F7pE3NBbobTzdwcxVd'
key='3231815648-f6GFawi7aOMWiRmeZ335Iscs0dNfYiBGA810Zc6'
secret='ZcSp8nt695qGSlLtt6vLB1gpqIJacSbjlJQqUgpdRtqo5'

#Using the keys and tokens for twitter authentication and generate an api through which we can read, write and perform other functionalities
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)
# api.update_status('Hello from Twitter bot- First tweet')
# print('Status Updated')


file='prev_replied.txt'
def last_read_file(file):
    file_read=open(file,'r')
    last_read_id=int(file_read.read().strip())
    file_read.close()
    return last_read_id
def store_readids(file,last_read_id):
    file_write=open(file,'w')
    file_write.write(str(last_read_id))
    file_write.close()
    return

    
tweets=api.mentions_timeline(last_read_file(file),tweet_mode='extended') #contains recent 20 mentions from any account
# print(tweets[1].text)

for tweet in tweets:
    # if '#randomtweet' in tweet.text.lower():
    print(str(tweet.id) + ' - ' + tweet.text)