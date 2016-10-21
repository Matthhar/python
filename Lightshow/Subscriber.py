from mosquitto import *
from serial import *
from random import *

def messageReceived(broker,obj,msg):
    global client
    payload = msg.payload.decode()
    print("Message " + msg.topic + "containing: " + payload)
    if (payload == "ON"):
        payload = "1"
    else:
        payload = "0"
    
    board.write(payload.encode())


# FULL DEVICE NAME can be found by running: python PortScanner.py
# SPEED is usually 115200 for Microbit and 9600 for Arduino
board = Serial("/dev/cu.usbmodem1431",9600,timeout=2)

randomID = random()
client = Mosquitto("LightSubscriber" + str(randomID))
client.connect("10.212.61.136")
client.subscribe("/lights")
client.on_message = messageReceived
while (True): client.loop()

# The rest of your code goes in here !!!