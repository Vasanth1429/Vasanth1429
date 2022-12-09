import sys
import RPi.GPIO as GPIO
import time
from Adafruit_IO import MQTTClient
import Adafruit_DHT
import twilio.rest as twilio

account = "ACe281d1e3d19a3ae34d5d1c81e9023aa6"
token = "fcac9c6a39b1faf7702dd55aba63da9c"
client = twilio.Client(account, token)

relay=12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay,GPIO.OUT)
soil=18
GPIO.setup(soil,GPIO.IN)


def temperature():
    humidity, temperature=Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,2)
    print ("humidity is",humidity,"temperature is",temperature)
    time.sleep(1)
    return temperature
def humidity():
    humidity, temperature=Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,2)
    print ("humidity is",humidity,"temperature is",temperature)
    time.sleep(1)
    return humidity
       
def light(pin,status):
 GPIO.setup(pin,GPIO.OUT)
 if(status=='ON'):
  GPIO.output(pin,1)
 else:
  GPIO.output(pin,0)
 



# Set to your Adafruit IO key.
ADAFRUIT_IO_KEY = 'aio_Xpms72VUa0K2x3vtBbxo2YjcMP4A'
# Set to your Adafruit IO username.
ADAFRUIT_IO_USERNAME = 'VelamalaManiKanta'

def connected(client):
    print('Connected to Adafruit IO!  Listening for changes...')
    # Subscribe to changes on a feed .
    client.subscribe('relay')

def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
    print('Feed {0} received new value: {1}'.format(feed_id, payload))
    if(feed_id=='Relay'):
        print("Relay is turned ",payload)
        light(relay,payload)
   
# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
# Connect to the Adafruit IO server.
client.connect()
# Now the program needs to use a client loop function to ensure messages are
# sent and received.  There are a few options for driving the message loop,
# depending on what your program needs to do.

# The first option is to run a thread in the background so you can continue
# doing things in your program.
client.loop_background()
# Now send new values every 10 seconds.
tim=3
print('Publishing a new message every ' ,tim,'seconds (press Ctrl-C to quit)...')
while True:
    soil_moisture=GPIO.input(soil)
    print("soil moisture is "soil_moisture)
    temp = temperature()
    print(' temperature value {0} {1}'.format(temp,"C °"))
    client.publish('temperature', temp)
    hum = humidity()
    print(' humidity value {0} {1}'.format(hum,"%"))
    client.publish('humidity', hum)
    time.sleep(tim)
    if temp >= 30:
        message = client.messages.create(to="+919866668987", from_="+19412542489",
                                 body="temperature is high more then 30")
 
    hum = humidity()
    if hum >= 75:
        message = client.messages.create(to="+919866668987", from_="+19412542489",
                                 body="humidity is high more then 75")

