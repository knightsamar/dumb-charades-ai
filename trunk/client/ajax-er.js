/* ajax-er.js -- provides ajax interface for the frontend to connect to the backend.
 * basic work is to propagate sensor data from client to server.
 *
 * written by samar -- 060321011
 *
 */
debug = true;

function sensorRequestHandler(sensorName,dataString)
{
	//which sensor said ? sensorName
	//what did it say ? dataString
	
	//make proper url
	
	url = "/appy/engine/AJAXSensor.py?sensorName="+sensorName+"&q="+dataString;
	
	//create ajax request object
	var sensorRequest;
	if (window.XMLHttpRequest) { // Mozilla, Safari, ...
		sensorRequest = new XMLHttpRequest();
		if (sensorRequest.overrideMimeType) {
			sensorRequest.overrideMimeType('text/xml');
			// See note below about this line
		}
	} 
	else if (window.ActiveXObject) { // IE
		try {
			sensorRequest = new ActiveXObject("Msxml2.XMLHTTP");
		} 
		catch (e) {
			try {
				sensorRequest = new ActiveXObject("Microsoft.XMLHTTP");
			} 
			catch (e) {}
		}
	}

	if (!sensorRequest) {
		alert('Giving up :( Cannot create an XMLHTTP instance! AppY won\'t work');
		return false;
	}
	
	sensorRequest.onreadystatechange = function() 
	{ 
		if (sensorRequest.readyState == 4) 
		{
			if (sensorRequest.status == 200) 
			{
				response = sensorRequest.responseXML;
				if (debug) alert(response);
				var element = response.getElementsByTagName('root').item(0);   // Read the first element
				document.ajax.dyn.value = element.firstChild.data;    		   // Assign the content to the form
				
				exec(actuator(sensorRequestHandler.responseText));
		} else {
			alert('There was a problem with the request.');
		}
	}
	};
    
    //send request
    sensorRequest.open('GET', url, true);
    sensorRequest.send('');
	
	
	
		//attach actuator

}

//this is the beginning of all things
function beginGame()
{
	//get status from server
	//if working
			//ask to start game
			//get user details
				getUserDetails()
			//get the number of words in the movie title
			//create guessBoxes
				createGuessBoxes()
			//hand-over control to the GameController
	//else
			//say the error
			//give contact details
}

function userEnteredWordSensor(word)
{
	//what word ?
	alert(word);
	sensorRequestHandler("userEnteredWordSensor",word);
}

function userIdleForLongTimeSensor(idle_time)
{
	//how much time was the user idle for ?
}

function userEnteredNonPerformedWordSensor()
{
	//which word did he enter ?
}

function userGuessedtheMovieTitle()
{
	
}
