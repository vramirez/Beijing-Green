from twitter import Twitter, OAuth 
import configparser,json,time,sys
config = configparser.RawConfigParser()
config.read('twauth.properties')
consumer_key = config.get('OAuth','key')
consumer_secret = config.get('OAuth','key_secret')
access_key = config.get('OAuth','token')
access_secret = config.get('OAuth','token_secret')
oauth = OAuth(access_key, access_secret,consumer_key,consumer_secret)
t = Twitter(auth=oauth)

#searchit='#EllosEstánAquí'
oldest=0
if len(sys.argv)>2 : 
	searchit=sys.argv[1]
	filename=sys.argv[2]
	if(len(sys.argv)>3):
		oldest=int(sys.argv[3])
else:
	print("Two parameters needed. Search term and output filename")
	exit()
filename+=".json"
all_tweets=[]
print("Downloading Search Tweets")
if(oldest==0):
	query = t.search.tweets(q=searchit,count=1000)
else:
	query = t.search.tweets(q=searchit,count=1000,max_id=oldest-1)

#all_tweets.extend(query['statuses'])
#oldest=all_tweets[-1]['id']

with open(filename, 'a+') as outfile:
	while (len(query['statuses'])>1):
		#query = t.search.tweets(q=searchit,count=1000,max_id=oldest-1)
		all_tweets.extend(query['statuses'])
		oldest=all_tweets[-1]['id']
		print("Processing "+str(len(query['statuses']))+" tweets. Last id = "+str(oldest))
		for tweet in all_tweets:
			json.dump(tweet, outfile)
			outfile.write("\n")
		all_tweets=[]
		query = t.search.tweets(q=searchit,count=1000,max_id=oldest-1)
		time.sleep(5)

