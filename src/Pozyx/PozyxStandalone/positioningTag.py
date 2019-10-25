from pypozyx import PozyxSerial, get_first_pozyx_serial_port, Coordinates
from configparser import ConfigParser
import paho.mqtt.client as mqtt

#read config files
cParser = ConfigParser()
cParser.read('config.ini')
eParser = ConfigParser()
eParser.read('export.ini')

#Change the remote ID for positioning from another device from config file
r_id = int(cParser.get('default','remote_id'),16)

#Set Export properties
exportFile = eParser.get('default','export_file')
fileName = eParser.get('default','file_name')
exportMQTT = eParser.get('default','export_mqtt')
host = eParser.get('default','mqtt_host')
topic = eParser.get('default','mqtt_topic')
clientID = eParser.get('default','mqtt_clientid')

#Setup variables
positionTag = Coordinates()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("topic")

#Check if connected
serial_port = get_first_pozyx_serial_port()
if serial_port is not None:
    pozyx = PozyxSerial(serial_port)
    print("Connection success!")
else:
    print("No Pozyx port was found")
    exit()

try:
    if exportFile is "y": f = open("position.txt", "a+")
    if exportMQTT is "y":
        client = mqtt.Client(client_id=clientID)
        client.on_connect = on_connect
        client.connect("broker.mqttdashboard.com")
        client.loop_start()
    while True:
        pozyx.doPositioning(positionTag, remote_id=r_id)
        publishString = hex(r_id) + ": " + str(positionTag)
        print(publishString)
        if exportFile is "y": f.write(publishString + "\n")
        if exportMQTT is "y": client.publish(topic,publishString)

#Exception exit
except:
    if exportFile is "y": f.close()
    if exportMQTT is "y": client.loop_stop()
    print("")
    print("Exit program")
