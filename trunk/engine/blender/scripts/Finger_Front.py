##################################################################################################
#	SCRIPT TO ANIMATE FRONT PART OF FINGERS
#	Created, Invented and Made Alive By : Deepak Shakya
#	Date : 08-April-2008
##################################################################################################

##################################################################################################
#	This function Animates the Front Part of Finger Bones - All of them
#
#	Armature_Object - The Bone Armature from which it selects the Finger Bone to animate
#	direction - The final direction where the Bone has to be moved()
#	endFrame - The final frame at which the Bone has to be moved in the specified direction 
##################################################################################################

##########################################
#	ALL LEFT BONES ARE SCRIPTED BELOW   #
##########################################

from Blender import *
import Blender

# Left Thumb - Front Part
def LEFTTHUMBFRONT(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Left Thumb - Front Part
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["FOLD"] = [1.0,0.8,0.0,0.0]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	LThumbFront = [bone for bone in all_bones if bone.name == "Bone.002_R.005"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	LThumbFront.quat[:] = x,y,z,r
	LThumbFront.insertKey(Armature_Object,endFrame,Object.Pose.ROT)
	
	return endFrame
	

# Left Index Finger - Front Part
def LEFTINDEXFINGERFRONT(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Left Index Finger - Front Part
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["FOLD"] = [1.0,0.0,0.0,-1.5]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the  Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	LIndexFingerFront = [bone for bone in all_bones if bone.name == "Bone.002_R.011"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	LIndexFingerFront.quat[:] = x,y,z,r
	LIndexFingerFront.insertKey(Armature_Object,endFrame,Object.Pose.ROT)

	return endFrame


# Left Middle Finger - Front Part
def LEFTMIDDLEFINGERFRONT(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Left Middle Finger - Front Part
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["FOLD"] = [1.0,0.0,0.0,-1.5]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	LMiddleFingerFront = [bone for bone in all_bones if bone.name == "Bone.002_R.007"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	LMiddleFingerFront.quat[:] = x,y,z,r
	LMiddleFingerFront.insertKey(Armature_Object,endFrame,Object.Pose.ROT)

	return endFrame


# Left Small Finger - Front Part
def LEFTSMALLFINGERFRONT(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Left Small Finger - Front Part
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["FOLD"] = [1.0,0.0,0.0,-0.8]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	LSmallFingerFront = [bone for bone in all_bones if bone.name == "Bone.002_R.009"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	LSmallFingerFront.quat[:] = x,y,z,r
	LSmallFingerFront.insertKey(Armature_Object,endFrame,Object.Pose.ROT)

	return endFrame


###########################################
#	ALL RIGHT BONES ARE SCRIPTED BELOW   #
###########################################

# Right Thumb - Front Part
def RIGHTTHUMBFRONT(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Right Thumb - Front Part
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["FOLD"] = [1.0,0.8,0.0,0.0]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	RThumbFront = [bone for bone in all_bones if bone.name == "Bone.002_L.005"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	RThumbFront.quat[:] = x,y,z,r
	RThumbFront.insertKey(Armature_Object,endFrame,Object.Pose.ROT)

	return endFrame


# Right Index Finger - Front Part
def RIGHTINDEXFINGERFRONT(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Right Index Finger - Front Part
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["FOLD"] = [1.0,0.0,0.0,1.5]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	RIndexFingerFront = [bone for bone in all_bones if bone.name == "Bone.002_L.011"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	RIndexFingerFront.quat[:] = x,y,z,r
	RIndexFingerFront.insertKey(Armature_Object,endFrame,Object.Pose.ROT)

	return endFrame


# Right Middle Finger - Front Part
def RIGHTMIDDLEFINGERFRONT(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Right Middle Finger - Front Part
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["FOLD"] = [1.0,0.0,0.0,1.5]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	RMiddleFingerFront = [bone for bone in all_bones if bone.name == "Bone.002_L.007"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	RMiddleFingerFront.quat[:] = x,y,z,r
	RMiddleFingerFront.insertKey(Armature_Object,endFrame,Object.Pose.ROT)
	
	return endFrame


# Right Small Finger - Front Part
def RIGHTSMALLFINGERFRONT(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Right Small Finger - Front Part
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["FOLD"] = [1.0,0.0,0.0,0.8]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	RSmallFingerFront = [bone for bone in all_bones if bone.name == "Bone.002_L.009"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	RSmallFingerFront.quat[:] = x,y,z,r
	RSmallFingerFront.insertKey(Armature_Object,endFrame,Object.Pose.ROT)
	
	return endFrame