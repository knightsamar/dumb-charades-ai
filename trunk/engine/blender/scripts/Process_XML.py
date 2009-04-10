#####################################################################################################
#
#	This script reads the action sequence XML file and generates the action sequence corresponding
#	to the script.
#	Created By :- Deepak Shakya
#	Date :- 10th April 2009, 04:38 Hrs
#
#	If you dont recognize the importance of comments, try coding after a power nap of 2 hrs and 
#	and getting to know that your pen drive that contains all your code has malfunctioned and
#	all your data is lost. You will know what I mean. 
#
#	ALGORITHM
#		I devised this stuff early in the morning so you could find the better way. My
#	requirements was to traverse an XML file that could generate the list of function calls
#	in the cuteBEAR.blend that could generate the animation for the action sequences in the
#	XML file.
#		Basically, I drew a flowchart considering all possible sequence patterns so that this
#	file gets more generic. I found following things - 
#	- If a 'seq' tag is inside another 'seq' tag, the starting frame for the following nodes will
#	  be the ending frame of the parent node.
#	- If a 'par' or 'body' tag is inside a 'seq' tag, the starting frame for the following nodes will
#	  be the starting frame of the parent node.
#
#####################################################################################################

# Import the relevant packages
from xml.dom.ext.reader import Sax2
from xml.dom import minidom,Node

# Determines how the action should be performed
Frame = {}
Frame["VERY_FAST"] = 10		# The animation will be played VERY FAST
Frame["FAST"] = 20			# The animation will be played FAST
Frame["NORMAL"] = 30		# The animation will be played NORMAL
Frame["SLOW"] = 40			# The animation will be played SLOW
Frame["VERY_SLOW"] = 50		# The animation will be played VERY SLOW

# the action sequence object - stores the actions
action_script = []


# This function traverses the Nodes to get the Action Sequence details
def traverseNodes(xmlnodes,start_frame):
	global action_script
	max_length = 0
	last_frame = start_frame
	for childNode in xmlnodes:
		if childNode.nodeType == Node.ELEMENT_NODE:
			if childNode.nodeName == "seq":
				# Handle node - seq (sequence)
				last_node = handleSequence(childNode,start_frame)
			elif childNode.nodeName == "par":
				# Handle node - par (parallel)
				last_node = handleParallel(childNode,start_frame)
			elif childNode.nodeName == "body":
				# Handle node - body (action sequence tag)
				last_node = handleBody(childNode,start_frame)

	if max_length < last_frame:
		max_length = last_frame
	
	return action_script


# Handles the 'body' tag and gets the action sequence details from the tag
def handleBody(body_node,start_frame):
	# Get all attributes of the node
	attrs = body_node.attributes

	# Initialize my attribute fields
	part = ""
	direction = ""
	speed = ""

	# Iterate through the attributes to get our attributes from the 'body' tag
	for attrName in attrs.keys():
		attrNode = attrs.get(attrName)
		if attrName[1] == "part":
			part = attrNode.nodeValue
		elif attrName[1] == "direction":
			direction = attrNode.nodeValue
		elif attrName[1] == "speed":
			speed = attrNode.nodeValue
			
	if speed == "":
		speed = "NORMAL"
	
	#print part,direction,speed
	last_frame = Frame[speed.upper()] + start_frame
	action_script.append([str(part.upper()),str(direction.upper()),start_frame,last_frame])
	
	return last_frame


# Handles the 'par' tag - delegates(jsp mania) the control to appropriate functions
def handleParallel(par_node,start_frame):
	max_length = 0
	last_frame = start_frame
	for childNode in par_node.childNodes:
		if childNode.nodeType == Node.ELEMENT_NODE:
			if childNode.nodeName == "seq":
				last_frame = handleSequence(childNode,start_frame)
			elif childNode.nodeName == "par":
				last_frame = handleParallel(childNode,start_frame)
			elif childNode.nodeName == "body":
				last_frame = handleBody(childNode,start_frame)

	if max_length < last_frame:
		max_length = last_frame

	return max_length


# Handles the 'seq' tag - delegates(jsp mania) the control to appropriate function
def handleSequence(seq_node,start_frame):
	max_length = 0
	last_frame = start_frame
	for childNode in seq_node.childNodes:
		if childNode.nodeType == Node.ELEMENT_NODE:
			if childNode.nodeName == "seq":
				last_frame = handleSequence(childNode,last_frame)
			elif childNode.nodeName == "par":
				last_frame = handleParallel(childNode,start_frame)
			elif childNode.nodeName == "body":
				last_frame = handleBody(childNode,last_frame)

	if max_length < last_frame:
		max_length = last_frame

	return max_length
