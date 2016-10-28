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
cursor.execute("SELECT * FROM urls")
rows = cursor.fetchall()
console.close()

#print rows[len(rows)-1]

row = rows[len(rows)-1]

print row[2]

timestamp = datetime.datetime.utcnow()

response = api.PostUpdate("Tweeted at " + str(timestamp) + " most recent page in history is " + row[2])
print ("Status updated to: " + response.text)