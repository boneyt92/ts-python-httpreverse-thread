import requests
import config
import random
import time
import json
import thread

temperature = random.randint(1,31);
preassure = random.randint(21,71);
def checkCommands():
	while True:
		url = 'https://api.thingspeak.com/channels/' + str(config.CHANNELID) + '/fields/4/last.json?api_key=' + config.READKEY
		headers = {'Content-type': 'application/json'}
		response = requests.request("GET", url,headers=headers)
		command = json.loads(response.text)
		print response.text
		led4 =  str(command['field4'])
		url = 'https://api.thingspeak.com/channels/' + str(config.CHANNELID) + '/fields/5/last.json?api_key=' + config.READKEY
		response = requests.request("GET", url,headers=headers)
		command = json.loads(response.text)
		led5 = command['field5']
		print '\n\n--------------------------------' + str(led4) + '----' + str(led5) + '\n\n';
		time.sleep(10);
try:
   thread.start_new_thread( checkCommands, () )
except:
   print "Error: unable to start thread"

while True:
	temperature = temperature + 5;
	preassure = preassure + 5;
	print "Temperature : " + str(temperature) + ", Preassure : " + str(preassure);
	payload = '{ "api_key" : "'+ config.WRITEKEY + '","field1":' + str(temperature) + ', "field2":' +str(preassure) + '}'
	headers = {'Content-type': 'application/json'}
	response = requests.request("POST", 'https://api.thingspeak.com/update', data=payload, headers=headers);
	#print response.text;
	time.sleep(60);