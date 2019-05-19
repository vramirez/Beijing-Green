from twitter import Twitter, OAuth 
import configparser,json,time
config = configparser.RawConfigParser()
config.read('twauth.properties')
consumer_key = config.get('OAuth','key')
consumer_secret = config.get('OAuth','key_secret')
access_key = config.get('OAuth','token')
access_secret = config.get('OAuth','token_secret')
oauth = OAuth(access_key, access_secret,consumer_key,consumer_secret)
t = Twitter(auth=oauth)

#searchit='%23yovoyconordonez'
#searchit='%23elfuturoconpetro'
#searchit='%23martaluciaenvenezuela'
#searchit='#EllosEstánAquí'
searchit='#CreoEnUribe'
print("Downloading Search Tweets")
filename="creoenUribe.json"
all_tweets=[]
#query = t.search.tweets(q='%23yovotodelacalle OR %23yovotoCristo OR %23yovotedelacalle OR %23yovotecristo',count=1000)
query = t.search.tweets(q=searchit,count=1000)
all_tweets.extend(query['statuses'])
oldest=all_tweets[-1]['id']

while (len(query['statuses'])>1):
	query = t.search.tweets(q=searchit,count=1000,max_id=oldest-1)
	all_tweets.extend(query['statuses'])
	oldest=all_tweets[-1]['id']
	print("Processing "+str(len(query['statuses']))+" tweets. Last id = "+str(oldest))
	time.sleep(10)


for tweet in all_tweets:
	with open(filename, 'a+') as outfile:
		json.dump(tweet, outfile)
		#outfile.write(tweet)
		outfile.write("\n")
		outfile.close()


