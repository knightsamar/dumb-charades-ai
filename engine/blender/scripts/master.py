##############################################################################################
#
#	This is the master script that creates the frames for the actions read by it in the 
#	XML file<here is the XML file genrated by the AI engine>.
#
#	Created By :- Deepak Shakya
#	Moderated and Coordinated By :- Gayatri Venugopal and Samarendra Manohar Hedaoo
#	Date :- 09 March 2009
##############################################################################################


########################################################
#   Getting all the import modules used by the script  #
########################################################

# Importing the packages required - Following are used for processing xml file
from xml.dom.ext.reader import Sax2
from xml.dom import minidom,Node

# Importing the packages required - Following are used for Blender and its internal working
import Blender
from Blender import *

# Importing scripts that we have created
import Head		# Animates the Head Bone
import Finger_Front	# Animates the Front Part of Finger Bones
import Finger_Rear	# Animates the Rear Part of Finger Bones
import Feet		# Animates the Feet Bones
import Elbow		# Animates the Elbow Bones
import Body		# Animates the Body Bones
import Arm		# Animates the Arm Bones
import Wrist		# Animates the Wrist Bones
import Waist		# Animates the Waist Bones
import Toes		# Animates the Toe Bones
import Thighs		# Animates the Thigh Bones
import Shoulder	# Animates the Shoulder Bones
import Knees		# Animates the Kness Bones

# Import script that contains the node processing functions in xml file
import Process_XML


################################################################################
#   LETS FIRST READ THE XML FILE AND GET THE ACTIONS THAT ARE TO BE PERFORMED  #
################################################################################

# Open the file that contains the action sequence specification
f = open("/home/anubhav/Desktop/blender/xml/walk.xml","r")

# Read the data from the file
data = f.read()

# Convert the case to lower case to account for improper case formation in the XML file
data = data.lower()

# Close the file
f.close()

# Create the XML reader to parse the XML data
reader = Sax2.Reader()

# Get the documentNode
docnode = reader.fromString(data)

# Get the root Element
root = docnode.documentElement

# Traverse the xml data to process and nodes and prepare the action script list
# Action Script object that stores the whole action sequence
action_script = Process_XML.traverseNodes(root.childNodes,1)

###########################################################################################
#	AT THIS POINT THE action_seq[] LIST IS POPULATED WITH THE ACTIONS TO BE PERFORMED	#
###########################################################################################


###########################################################################################
#	LETS START PUTTING THE KEYFRAMES BY GETTING THE RELEVANT OBJECTS & CALLING FUNCTIONS	#
###########################################################################################

# Get current Scence
scene_obj = Blender.Scene.GetCurrent()

# Get the JoOngle Armature so that we can have all the bones in it
armature_obj = scene_obj.objects[6]

# Get the Pose instance so that we can pose the JoOngle
pose = armature_obj.getPose()

# Get all the bones in the Pose of the JoOngle Armature
pose_bones = pose.bones.values()

#Get the action being performed by the JoOngle
action = armature_obj.getAction()

if not action:
	action = Armature.NLA.NewAction()
	action.setActive(armature_obj)

# Initialize all the Bones so that we can start fresh
State = {}
State["HEAD"] = "DEFAULT"
State["LEFTTHUMBREAR"] = "DEFAULT"
State["LEFTINDEXFINGERREAR"] = "DEFAULT"
State["LEFTMIDDLEFINGERREAR"] = "DEFAULT"
State["LEFTSMALLFINGERREAR"] = "DEFAULT"
State["RIGHTTHUMBREAR"] = "DEFAULT"
State["RIGHTINDEXFINGERREAR"] = "DEFAULT"
State["RIGHTMIDDLEFINGERREAR"] = "DEFAULT"
State["RIGHTSMALLFINGERREAR"] = "DEFAULT"
State["LEFTTHUMBFRONT"] = "DEFAULT"
State["LEFTINDEXFINGERFRONT"] = "DEFAULT"
State["LEFTMIDDLEFINGERFRONT"] = "DEFAULT"
State["LEFTSMALLFINGERFRONT"] = "DEFAULT"
State["RIGHTTHUMBFRONT"] = "DEFAULT"
State["RIGHTINDEXFINGERFRONT"] = "DEFAULT"
State["RIGHTMIDDLEFINGERFRONT"] = "DEFAULT"
State["RIGHTSMALLFINGERFRONT"] = "DEFAULT"
State["LEFTFEET"] = "DEFAULT"
State["RIGHTFEET"] = "DEFAULT"
State["LEFTELBOW"] = "DEFAULT"
State["RIGHTELBOW"] = "DEFAULT"
State["BODY"] = "DEFAULT"
State["LEFTARM"] = "DEFAULT"
State["RIGHTARM"] = "DEFAULT"
State["LEFTWRIST"] = "DEFAULT"
State["RIGHTWRIST"] = "DEFAULT"
State["WAIST"] = "DEFAULT"
State["LEFTTOE"] = "DEFAULT"
State["RIGHTTOE"] = "DEFAULT"
State["LEFTTHIGH"] = "DEFAULT"
State["RIGHTTHIGH"] = "DEFAULT"
State["LEFTSHOULDER"] = "DEFAULT"
State["RIGHTSHOULDER"] = "DEFAULT"
State["LEFTKNEE"] = "DEFAULT"
State["RIGHTKNEE"] = "DEFAULT"


#Head.HEAD(armature_obj,"DEFAULT",1)
#Finger_Rear.LEFTTHUMBREAR(armature_obj,"DEFAULT",1)
#Finger_Rear.LEFTINDEXFINGERREAR(armature_obj,"DEFAULT",1)
#Finger_Rear.LEFTMIDDLEFINGERREAR(armature_obj,"DEFAULT",1)
#Finger_Rear.LEFTSMALLFINGERREAR(armature_obj,"DEFAULT",1)
#Finger_Rear.RIGHTTHUMBREAR(armature_obj,"DEFAULT",1)
#Finger_Rear.RIGHTINDEXFINGERREAR(armature_obj,"DEFAULT",1)
#Finger_Rear.RIGHTMIDDLEFINGERREAR(armature_obj,"DEFAULT",1)
#Finger_Rear.RIGHTSMALLFINGERREAR(armature_obj,"DEFAULT",1)
#Finger_Front.LEFTTHUMBFRONT(armature_obj,"DEFAULT",1)
#Finger_Front.LEFTINDEXFINGERFRONT(armature_obj,"DEFAULT",1)
#Finger_Front.LEFTMIDDLEFINGERFRONT(armature_obj,"DEFAULT",1)
#Finger_Front.LEFTSMALLFINGERFRONT(armature_obj,"DEFAULT",1)
#Finger_Front.RIGHTTHUMBFRONT(armature_obj,"DEFAULT",1)
#Finger_Front.RIGHTINDEXFINGERFRONT(armature_obj,"DEFAULT",1)
#Finger_Front.RIGHTMIDDLEFINGERFRONT(armature_obj,"DEFAULT",1)
#Finger_Front.RIGHTSMALLFINGERFRONT(armature_obj,"DEFAULT",1)
#Feet.LEFTFEET(armature_obj,"DEFAULT",1)
#Feet.RIGHTFEET(armature_obj,"DEFAULT",1)
#Elbow.LEFTELBOW(armature_obj,"DEFAULT",1)
#Elbow.RIGHTELBOW(armature_obj,"DEFAULT",1)
#Body.BODY(armature_obj,"DEFAULT",1)
#Arm.LEFTARM(armature_obj,"DEFAULT",1)
#Arm.RIGHTARM(armature_obj,"DEFAULT",1)
#Wrist.LEFTWRIST(armature_obj,"DEFAULT",1)
#Wrist.RIGHTWRIST(armature_obj,"DEFAULT",1)
#Waist.WAIST(armature_obj,"DEFAULT",1)
#Toes.LEFTTOE(armature_obj,"DEFAULT",1)
#Toes.RIGHTTOE(armature_obj,"DEFAULT",1)
#Thighs.LEFTTHIGH(armature_obj,"DEFAULT",1)
#Thighs.RIGHTTHIGH(armature_obj,"DEFAULT",1)
#Shoulder.LEFTSHOULDER(armature_obj,"DEFAULT",1)
#Shoulder.RIGHTSHOULDER(armature_obj,"DEFAULT",1)
#Knees.LEFTKNEE(armature_obj,"DEFAULT",1)
#Knees.RIGHTKNEE(armature_obj,"DEFAULT",1)

for action in action_script:
	print action
	if action[0] == "HEAD":
		Head.HEAD(armature_obj,State["HEAD"],State["HEAD"][1])
		Head.HEAD(armature_obj,action[1],action[3])
		State["HEAD"][0] = action[1]
		State["HEAD"][1] = action[3]
		print "Head",State["HEAD"]
		
	elif action[0] == "LEFTTHUMBREAR":
		Finger_Rear.LEFTTHUMBREAR(armature_obj,State["LEFTTHUMBREAR"],action[2])
		Finger_Rear.LEFTTHUMBREAR(armature_obj,action[1],action[3])
		State["LEFTTHUMBREAR"] = action[1]
		print "Left Thumb Rear",State["LEFTTHUMBREAR"]
		
	elif action[0] == "LEFTINDEXFINGERREAR":
		Finger_Rear.LEFTINDEXFINGERREAR(armature_obj,State["LEFTINDEXFINGERREAR"],action[2])
		Finger_Rear.LEFTINDEXFINGERREAR(armature_obj,action[1],action[3])
		State["LEFTINDEXFINGERREAR"] = action[1]
		print "Left Index Finger Rear",State["LEFTINDEXFINGERREAR"]
		
	elif action[0] == "LEFTMIDDLEFINGERREAR":
		Finger_Rear.LEFTMIDDLEFINGERREAR(armature_obj,State["LEFTMIDDLEFINGERREAR"],action[2])
		Finger_Rear.LEFTMIDDLEFINGERREAR(armature_obj,action[1],action[3])
		State["LEFTMIDDLEFINGERREAR"] = action[1]
		print "Left Middel Finger Rear",State["LEFTMIDDLEFINGERREAR"]
		
	elif action[0] == "LEFTSMALLFINGERREAR":
		Finger_Rear.LEFTSMALLFINGERREAR(armature_obj,State["LEFTSMALLFINGERREAR"],action[2])
		Finger_Rear.LEFTSMALLFINGERREAR(armature_obj,action[1],action[3])
		State["LEFTSMALLFINGERREAR"] = action[1]
		print "Left Small Finger Rear",State["LEFTSMALLFINGERREAR"]
		
	elif action[0] == "RIGHTTHUMBREAR":
		Finger_Rear.RIGHTTHUMBREAR(armature_obj,State["RIGHTTHUMBREAR"],action[2])
		Finger_Rear.RIGHTTHUMBREAR(armature_obj,action[1],action[3])
		State["RIGHTTHUMBREAR"] = action[1]
		print "Right Thumb Rear",State["RIGHTTHUMBREAR"]
		
	elif action[0] == "RIGHTINDEXFINGERREAR":
		Finger_Rear.RIGHTINDEXFINGERREAR(armature_obj,State["RIGHTINDEXFINGERREAR"],action[2])
		Finger_Rear.RIGHTINDEXFINGERREAR(armature_obj,action[1],action[3])
		State["RIGHTINDEXFINGERREAR"] = action[1]
		print "Right Index Finger Rear",State["RIGHTINDEXFINGERREAR"]
		
	elif action[0] == "RIGHTMIDDLEFINGERREAR":
		Finger_Rear.RIGHTSMALLFINGERREAR(armature_obj,State["RIGHTMIDDLEFINGERREAR"],action[2])
		Finger_Rear.RIGHTSMALLFINGERREAR(armature_obj,action[1],action[3])
		State["RIGHTMIDDLEFINGERREAR"] = action[1]
		print "Right Small Finger Rear",State["RIGHTMIDDLEFINGERREAR"]
		
	elif action[0] == "RIGHTSMALLFINGERREAR":
		Finger_Rear.RIGHTSMALLFINGERREAR(armature_obj,State["RIGHTSMALLFINGERREAR"],action[2])
		Finger_Rear.RIGHTSMALLFINGERREAR(armature_obj,action[1],action[3])
		State["RIGHTSMALLFINGERREAR"] = action[1]
		print "Right Small Finger Rear",State["RIGHTSMALLFINGERREAR"]
		
	elif action[0] == "LEFTTHUMBFRONT":
		Finger_Front.LEFTTHUMBFRONT(armature_obj,State["LEFTTHUMBFRONT"],action[2])
		Finger_Front.LEFTTHUMBFRONT(armature_obj,action[1],action[3])
		State["LEFTTHUMBFRONT"] = action[1]
		print "Left Thumb Front",State["LEFTTHUMBFRONT"]
		
	elif action[0] == "LEFTINDEXFINGERFRONT":
		Finger_Front.LEFTINDEXFINGERFRONT(armature_obj,State["LEFTINDEXFINGERFRONT"],action[2])
		Finger_Front.LEFTINDEXFINGERFRONT(armature_obj,action[1],action[3])
		State["LEFTINDEXFINGERFRONT"] = action[1]
		print "Left Index Finger Front",State["LEFTINDEXFINGERFRONT"]
		
	elif action[0] == "LEFTMIDDLEFINGERFRONT":
		Finger_Front.LEFTMIDDLEFINGERFRONT(armature_obj,State["LEFTMIDDLEFINGERFRONT"],action[2])
		Finger_Front.LEFTMIDDLEFINGERFRONT(armature_obj,action[1],action[3])
		State["LEFTMIDDLEFINGERFRONT"] = action[1]
		print "Left Middle Finger Front",State["LEFTMIDDLEFINGERFRONT"]
		
	elif action[0] == "LEFTSMALLFINGERFRONT":
		Finger_Front.LEFTSMALLFINGERFRONT(armature_obj,State["LEFTSMALLFINGERFRONT"],action[2])
		Finger_Front.LEFTSMALLFINGERFRONT(armature_obj,action[1],action[3])
		State["LEFTSMALLFINGERFRONT"] = action[1]
		print "Left Small Finger Front",State["LEFTSMALLFINGERFRONT"]
		
	elif action[0] == "RIGHTTHUMBFRONT":
		Finger_Front.RIGHTTHUMBFRONT(armature_obj,State["RIGHTTHUMBFRONT"],action[2])
		Finger_Front.RIGHTTHUMBFRONT(armature_obj,action[1],action[3])
		State["RIGHTTHUMBFRONT"] = action[1]
		print "Right Thumb Front",State["RIGHTTHUMBFRONT"]
		
	elif action[0] == "RIGHTINDEXFINGERFRONT":
		Finger_Front.RIGHTMIDDLEFINGERFRONT(armature_obj,State["RIGHTINDEXFINGERFRONT"],action[2])
		Finger_Front.RIGHTMIDDLEFINGERFRONT(armature_obj,action[1],action[3])
		State["RIGHTINDEXFINGERFRONT"] = action[1]
		print "Right Middle Finger Front",State["RIGHTINDEXFINGERFRONT"]
		
	elif action[0] == "RIGHTMIDDLEFINGERFRONT":
		Finger_Front.RIGHTMIDDLEFINGERFRONT(armature_obj,State["RIGHTMIDDLEFINGERFRONT"],action[2])
		Finger_Front.RIGHTMIDDLEFINGERFRONT(armature_obj,action[1],action[3])
		State["RIGHTMIDDLEFINGERFRONT"] = action[1]
		print "Right Middle Finger Front",State["RIGHTMIDDLEFINGERFRONT"]
		
	elif action[0] == "RIGHTSMALLFINGERFRONT":
		Finger_Front.RIGHTSMALLFINGERFRONT(armature_obj,State["RIGHTSMALLFINGERFRONT"],action[2])
		Finger_Front.RIGHTSMALLFINGERFRONT(armature_obj,action[1],action[3])
		State["RIGHTSMALLFINGERFRONT"] = action[1]
		print "Right Small Finger Front",State["RIGHTSMALLFINGERFRONT"]
		
	elif action[0] == "LEFTFEET":
		Feet.LEFTFEET(armature_obj,State["LEFTFEET"],action[2])
		Feet.LEFTFEET(armature_obj,action[1],action[3])
		State["LEFTFEET"] = action[1]
		print "Left Feet",State["LEFTFEET"]
		
	elif action[0] == "RIGHTFEET":
		Feet.RIGHTFEET(armature_obj,State["RIGHTFEET"],action[2])
		Feet.RIGHTFEET(armature_obj,action[1],action[3])
		State["RIGHTFEET"] = action[1]
		print "Right Feet",State["RIGHTFEET"]
		
	elif action[0] == "LEFTELBOW":
		Elbow.LEFTELBOW(armature_obj,State["LEFTELBOW"],action[2])
		Elbow.LEFTELBOW(armature_obj,action[1],action[3])
		State["LEFTELBOW"] = action[1]
		print "Left Elbow",State["LEFTELBOW"]
		
	elif action[0] == "RIGHTELBOW":
		Elbow.RIGHTELBOW(armature_obj,State["RIGHTELBOW"],action[2])
		Elbow.RIGHTELBOW(armature_obj,action[1],action[3])
		State["RIGHTELBOW"] = action[1]
		print "Right Elbow",State["RIGHTELBOW"]
		
	elif action[0] == "BODY":
		Body.BODY(armature_obj,State["BODY"],action[2])
		Body.BODY(armature_obj,action[1],action[3])
		State["BODY"] = action[1]
		print "Body",State["BODY"]
		
	elif action[0] == "LEFTARM":
		Arm.LEFTARM(armature_obj,State["LEFTARM"],action[2])
		Arm.LEFTARM(armature_obj,action[1],action[3])
		State["LEFTARM"] = action[1]
		print "Left Arm",State["LEFTARM"]
		
	elif action[0] == "RIGHTARM":
		Arm.RIGHTARM(armature_obj,State["RIGHTARM"],action[2])
		Arm.RIGHTARM(armature_obj,action[1],action[3])
		State["RIGHTARM"] = action[1]
		print "Right Arm",State["RIGHTARM"]
		
	elif action[0] == "LEFTWRIST":
		Wrist.LEFTWRIST(armature_obj,State["LEFTWRIST"],action[2])
		Wrist.LEFTWRIST(armature_obj,action[1],action[3])
		State["LEFTWRIST"] = action[1]
		print "Left Arm",State["LEFTWRIST"]
		
	elif action[0] == "RIGHTWRIST":
		Wrist.RIGHTWRIST(armature_obj,State["RIGHTWRIST"],action[2])
		Wrist.RIGHTWRIST(armature_obj,action[1],action[3])
		State["RIGHTWRIST"] = action[1]
		print "Right Wrist",State["RIGHTWRIST"]
		
	elif action[0] == "WAIST":
		Waist.WAIST(armature_obj,State["WAIST"],action[2])
		Waist.WAIST(armature_obj,action[1],action[3])
		State["WAIST"] = action[1]
		print "Waist",State["WAIST"]
		
	elif action[0] == "LEFTTOE":
		Toes.LEFTTOE(armature_obj,State["LEFTTOE"],action[2])
		Toes.LEFTTOE(armature_obj,action[1],action[3])
		State["LEFTTOE"] = action[1]
		print "Left Toe",State["LEFTTOE"]
		
	elif action[0] == "RIGHTTOE":
		Toes.RIGHTTOE(armature_obj,State["RIGHTTOE"],action[2])
		Toes.RIGHTTOE(armature_obj,action[1],action[3])
		State["RIGHTTOE"] = action[1]
		print "Right Toe",State["RIGHTTOE"]
		
	elif action[0] == "LEFTTHIGH":
		Thighs.LEFTTHIGH(armature_obj,State["LEFTTHIGH"],action[2])
		Thighs.LEFTTHIGH(armature_obj,action[1],action[3])
		State["LEFTTHIGH"] = action[1]
		print "Left Thigh",State["LEFTTHIGH"]
		
	elif action[0] == "RIGHTTHIGH":
		Thighs.RIGHTTHIGH(armature_obj,State["RIGHTTHIGH"],action[2])
		Thighs.RIGHTTHIGH(armature_obj,action[1],action[3])
		State["RIGHTTHIGH"] = action[1]
		print "Right Thigh",State["RIGHTTHIGH"]
		
	elif action[0] == "LEFTSHOULDER":
		Shoulder.LEFTSHOULDER(armature_obj,State["LEFTSHOULDER"],action[2])
		Shoulder.LEFTSHOULDER(armature_obj,action[1],action[3])
		State["LEFTSHOULDER"] = action[1]
		print "Left Shoulder",State["LEFTSHOULDER"]
		
	elif action[0] == "RIGHTSHOULDER":
		Shoulder.RIGHTSHOULDER(armature_obj,State["RIGHTSHOULDER"],action[2])
		Shoulder.RIGHTSHOULDER(armature_obj,action[1],action[3])
		State["RIGHTSHOULDER"] = action[1]
		print "Right Shoulder",State["RIGHTSHOULDER"]
		
	elif action[0] == "LEFTKNEE":
		Knees.LEFTKNEE(armature_obj,State["LEFTKNEE"],action[2])
		Knees.LEFTKNEE(armature_obj,action[1],action[3])
		State["LEFTKNEE"] = action[1]
		print "Left Knee",State["LEFTKNEE"]
		
	elif action[0] == "RIGHTKNEE":
		Knees.RIGHTKNEE(armature_obj,State["RIGHTKNEE"],action[2])
		Knees.RIGHTKNEE(armature_obj,action[1],action[3])
		State["RIGHTKNEE"] = action[1]
		print "Right Knee",State["RIGHTKNEE"]
