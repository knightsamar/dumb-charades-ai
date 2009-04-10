##################################################################################################
#	SCRIPT TO ANIMATE REAR PART OF FINGERS
#	Created, Invented and Made Alive By : Deepak Shakya
#	Date : 08-April-2008
##################################################################################################

##################################################################################################
#	This function Animates the Rear Part of Finger Bones - All of them
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

# Left Thumb - Rear Part
def LEFTTHUMBREAR(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Left Thumb - Rear Part
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["UP"] = [1.0,-0.3,0.0,0.0]
	Positions["DOWN"] = [1.0,0.6,0.0,0.0]
	Positions["LEFT"] = [1.0,0.0,0.0,-0.15]
	Positions["RIGHT"] = [1.0,0.0,0.0,0.5]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	LThumbRear = [bone for bone in all_bones if bone.name == "Bone.002_R.004"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	LThumbRear.quat[:] = x,y,z,r
	LThumbRear.insertKey(Armature_Object,endFrame,Object.Pose.ROT)
	
	return endFrame


# Left Index Finger - Rear Part
def LEFTINDEXFINGERREAR(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Left Index Finger - Rear Part
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["UP"] = [1.0,0.3,0.0,0.3]
	Positions["DOWN"] = [1.0,-0.3,0.0,-0.3]
	Positions["LEFT"] = [1.0,-0.05,0.0,0.05]
	Positions["RIGHT"] = [1.0,0.3,0.0,-0.3]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	LIndexFingerRear = [bone for bone in all_bones if bone.name == "Bone.002_R.010"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	LIndexFingerRear.quat[:] = x,y,z,r
	LIndexFingerRear.insertKey(Armature_Object,endFrame,Object.Pose.ROT)

	return endFrame
		

# Left Middle Finger - Rear Part
def LEFTMIDDLEFINGERREAR(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Left Middle Finger - Rear Part
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["UP"] = [1.0,-0.1,0.0,0.3]
	Positions["DOWN"] = [1.0,0.1,0.0,-0.3]
	Positions["LEFT"] = [1.0,-0.1,0.0,0.0]
	Positions["RIGHT"] = [1.0,0.1,0.0,0.0]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	LMiddleFingerRear = [bone for bone in all_bones if bone.name == "Bone.002_R.006"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	LMiddleFingerRear.quat[:] = x,y,z,r
	LMiddleFingerRear.insertKey(Armature_Object,endFrame,Object.Pose.ROT)

	return endFrame


# Left Small Finger - Rear Part
def LEFTSMALLFINGERREAR(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Left Small Finger - Rear Part
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["UP"] = [1.0,0.1,0.0,0.3]
	Positions["DOWN"] = [1.0,0.0,0.0,-0.4]
	Positions["LEFT"] = [1.0,-0.3,0.0,0.0]
	Positions["RIGHT"] = [1.0,0.1,0.0,0.0]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	LSmallFingerRear = [bone for bone in all_bones if bone.name == "Bone.002_R.008"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	LSmallFingerRear.quat[:] = x,y,z,r
	LSmallFingerRear.insertKey(Armature_Object,endFrame,Object.Pose.ROT)

	return endFrame



###########################################
#	ALL RIGHT BONES ARE SCRIPTED BELOW   #
###########################################

# Right Thumb - Rear Part
def RIGHTTHUMBREAR(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Right Thumb - Rear Part
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["UP"] = [1.0,-0.3,0.0,0.0]
	Positions["DOWN"] = [1.0,0.6,0.0,0.0]
	Positions["LEFT"] = [1.0,0.0,0.0,0.15]
	Positions["RIGHT"] = [1.0,0.0,0.0,-0.5]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	RThumbRear = [bone for bone in all_bones if bone.name == "Bone.002_L.004"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	RThumbRear.quat[:] = x,y,z,r
	RThumbRear.insertKey(Armature_Object,endFrame,Object.Pose.ROT)
	
	return endFrame


# Right Index Finger - Rear Part
def RIGHTINDEXFINGERREAR(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Right Index Finger - Rear Part
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["UP"] = [1.0,0.3,0.0,-0.3]
	Positions["DOWN"] = [1.0,-0.3,0.0,0.3]
	Positions["LEFT"] = [1.0,0.3,0.0,0.3]
	Positions["RIGHT"] = [1.0,-0.05,0.0,-0.05]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	RIndexFingerRear = [bone for bone in all_bones if bone.name == "Bone.002_L.010"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	RIndexFingerRear.quat[:] = x,y,z,r
	RIndexFingerRear.insertKey(Armature_Object,endFrame,Object.Pose.ROT)
	
	return endFrame


# Right Middle Finger - Rear Part
def RIGHTMIDDLEFINGERREAR(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Right Middle Finger - Rear Part
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["UP"] = [1.0,-0.1,0.0,-0.3]
	Positions["DOWN"] = [1.0,0.1,0.0,0.3]
	Positions["LEFT"] = [1.0,0.1,0.0,0.0]
	Positions["RIGHT"] = [1.0,-0.1,0.0,0.0]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	RMiddleFingerRear = [bone for bone in all_bones if bone.name == "Bone.002_L.006"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	RMiddleFingerRear.quat[:] = x,y,z,r
	RMiddleFingerRear.insertKey(Armature_Object,endFrame,Object.Pose.ROT)
	
	return endFrame


# Right Small Finger - Rear Part
def RIGHTSMALLFINGERREAR(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Right Small Finger - Rear Part
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["UP"] = [1.0,0.1,0.0,-0.3]
	Positions["DOWN"] = [1.0,-0.1,0.0,0.3]
	Positions["LEFT"] = [1.0,0.05,0.0,0.0]
	Positions["RIGHT"] = [1.0,-0.3,0.0,-0.1]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	RSmallFingerRear = [bone for bone in all_bones if bone.name == "Bone.002_L.008"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	RSmallFingerRear.quat[:] = x,y,z,r
	RSmallFingerRear.insertKey(Armature_Object,endFrame,Object.Pose.ROT)
	
	return endFrame