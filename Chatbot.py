stopwords = ("i","am","called","my","name","is","it's","it","outside"," ")

name = raw_input("What is your name? ")
name2 = name.lower()
name3 = name2.split(" ")
    
for found in name3:
    if found in stopwords: continue
    else: break
        
#print(found)
print("Hello " + found)

condition = raw_input("How are you feeling today? ")
print("You are feeling "+ condition + " today")

location = raw_input("Where are you? ")
weather = raw_input("What's the weather like in " + location +"? ")
print("So, It's a " + weather + " day in " + location)