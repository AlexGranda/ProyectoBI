'''

 
 QUITO 
==============
'''
import couchdb
import sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
 
 
##########API CREDENTIALS ############   Poner sus credenciales del API de dev de Twitter.. aqui ya estan mis credenciales editadas.. lo otro no creo q sea necesario editar
ckey = "C2HSs9xaXh0Dqp5b8p8ggAeob"
csecret = "JKip86zRqvS4EZHEH80gwIN0m1rCUdZwvUtjvReZeh7htSzuIp"
atoken = "581847720-vDp2PKNcgsafI1N3mLxJl2raSHwnzycBklblYKUZ"
asecret = "d7Y7ulRzrQXwBWFcUi0mtGs1xcf7NDAKRykIQq3hJ5Y9a"
 
class listener(StreamListener):
 
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print("SAVED" + str(doc) +"=>" + str(data))
        except:
            print("Already exists")
            pass
        return True
 
    def on_error(self, status):
        print(status)
 
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
 
 
if len(sys.argv)!=3:
    sys.stderr.write("Error: needs more arguments: <URL><DB name>\n")
    sys.exit()
 
URL = sys.argv[1]
db_name = sys.argv[2]
 
 
'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  #('http://245.106.43.184:5984/') poner la url de su base de datos
try:
    print(db_name)
    db = server[db_name]
 
except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()
 
 
'''===============LOCATIONS=============='''
 
twitterStream.filter(locations=[-78.593445,-0.370099,-78.386078,-0.081711]) #QUITO 
