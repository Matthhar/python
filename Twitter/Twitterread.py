import twitter
import datetime
import sqlite3

file = open("/Users/htmatthews/Documents/python/Twitter/Twittercredentials.txt")
creds = file.read().split('\n')

api = twitter.Api(creds[0],creds[1],creds[2],creds[3])

#file = open("/Users/htmatthews/Library/Application Support/Google/Chrome/Default/History")
#sites = file.read().split('\n')

#print sites[len(sites)-1]

console = sqlite3.connect("/Users/htmatthews/Library/Application Support/Google/Chrome/Default/History")
cursor = console.cursor()
CREATE TABLE history
cursor.execute("SELECT * FROM history")
rows = cursor.fetchall()
for row in rows: print row
console.close()


#timestamp = datetime.datetime.utcnow()

#response = api.PostUpdate("Tweeted at " + str(timestamp))
#print ("Status updated to: " + response.text)