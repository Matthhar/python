stopwords = ("i","am","called","my","name","is","it's","it","outside"," ","i'm","in","the","weather")
#list of stopwords for this chatbot

name = raw_input("What is your name? ")
name2 = name.lower()
name3 = name2.split(" ")
    
for found in name3:
    if found in stopwords: continue
    else: break
        
found2 = found.capitalize()
print("Hello " + found2)
#code for finding out your name


condition = raw_input("How are you feeling today? ")
condition2 = condition.lower()
condition3 = condition2.split(" ")

for feels in condition3:
    if feels in stopwords: continue
    else: break

print("You are feeling "+ feels + " today")
#code to find out how you are


location = raw_input("Where are you? ")
location2 = location.lower()
location3 = location2.split(" ")
#print(location3)

for place in location3:
    if place in stopwords: continue
    else: break

place2 = place.capitalize()
#code to ask where you are


weather = raw_input("What's the weather like in " + place2 +"? ")
weather2 = weather.lower()
weather3 = weather2.split(" ")

for wfound in weather3:
    if wfound in stopwords: continue
    else: break

print("So, It's a " + wfound + " day in " + place2)
#code to find out how the weather is where you are