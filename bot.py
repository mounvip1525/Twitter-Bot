#Bot account- @MythiliSudhan
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

def reply():  
    tweets=api.mentions_timeline(last_read_file(file),tweet_mode='extended') #contains recent 20 mentions from any account
    # print(tweets[1].text)
    for tweet in reversed(tweets): #reversing so as to have the latest tweet for ex. if 6,7,8,9 tweets exits the file will have 6th id after replying to the rest in the order(9,8,7,6) and using reversed we can have the id of the 9th tweet by replying in the order(6,7,8,9)
        if '#randomtweet' in tweet.full_text.lower():
            # print(str(tweet.id) + ' - ' + tweet.full_text)
            #print('Replied to ID: ' + tweet.id)
            api.update_status("@" + tweet.user.screen_name + " Have a nice day!", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
        store_readids(file,tweet.id) #Once replied by the bot it has to be removed and write method basically overwrites the file-content, hence removing the prev. replied data(if it contains the hashtag)

while True:
    reply()
    time.sleep(15) #sleep for 15 seconds and check for new tweets by running the reply function