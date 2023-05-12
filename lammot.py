import paho.mqtt.publish as publish
import psutil
import string
from subprocess import check_output
import re
from gpiozero import CPUTemperature

# Kanavan ID
channel_ID = "2017364"

# Hosti
mqtt_host = "mqtt3.thingspeak.com"

# Client id, nimi ja salasana
mqtt_client_ID = "BTgYKCcGMSM6PB05ISwjDRw"
mqtt_username  = "BTgYKCcGMSM6PB05ISwjDRw"
mqtt_password  = "suMrzU2fqdmo/dfWK0gy73IJ"

t_transport = "websockets"
t_port = 80

topic = "channels/" + channel_ID + "/publish"

while (True):

    # Päivitetään tietoja 1 sekunnin välein
    
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_percent = psutil.virtual_memory().percent
    cpu_temp = CPUTemperature ()
    
    
    print (f"Prosessorin lämpötila {cpu_temp.temperature}")

    #Rakennetaan payload saaduilla tiedoilla
    
    payload = "field3=" + str(cpu_percent) + "&field4=" + str(ram_percent) + "&field5=" + str(cpu_temp.temperature)

    # Julkaistaan tehty payload
    try:
        print ("Writing Payload = ", payload," to host: ", mqtt_host, " clientID= ", mqtt_client_ID, " User ", mqtt_username, " PWD ", mqtt_password)
        publish.single(topic, payload, hostname=mqtt_host, transport=t_transport, port=t_port, client_id=mqtt_client_ID, auth={'username':mqtt_username,'password':mqtt_password})
    except keyboardInterrupt:
        break
    except Exception as e:
        print (e) 