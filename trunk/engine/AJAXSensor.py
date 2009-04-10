#AJAXSensor.py -- 
#	handles the sensor requests from the front-end and propages it to the proper sensor on the backend
#	then responds back to the client with the response in XML form.

# written by samar - 060321011
# This file is under Apache License.

#uses the mod_python libraries for all cgi dealings
from mod_python import util, apache;
from urllib import unquote;
from sensors import *;

debug = True;

def handler(req):
	'''this is sort of main(char args[]) in C -- req is the request object'''
	global debug #refer to the global instance
	
	req.content_type = "text/html";
	query_string = util.parse_qs(req.parsed_uri[7]);
	
	req.write(str(query_string));
	sensorName = query_string['sensorName'][0];
	if debug: req.write("Sensor = " + sensorName);
	senseString = query_string['q'][0]; 
	
	#dynamic calls implemented for the first time in history of SICSR!
	if (len(q.strip())) == 0:
		prepareandsendResponse('Error: You need to enter something!');
	else:
		call = "responseDict = %s(req,'%s')" % (sensorName,senseString);
		exec(call);	#call the right function and stores the response in responseList;
		req.write("You said %s and the response is %s" % senseString, responseList );
	return apache.OK;

def prepareandsendResponse(responseList):
	
	
