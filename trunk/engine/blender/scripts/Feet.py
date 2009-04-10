##################################################################################################
#	SCRIPT TO ANIMATE FEETS - LEFT AND RIGHT
#	Created, Invented and Made Alive By : Deepak Shakya
#	Date : 08-April-2008
##################################################################################################

##################################################################################################
#	This function Animates the Feets
#
#	Armature_Object - The Bone Armature from which it selects the Feet Bone to animate
#	direction - The final direction where the Bone has to be moved()
#	endFrame - The final frame at which the Bone has to be moved in the specified direction 
##################################################################################################

from Blender import *
import Blender

# Feet Left
def LEFTFEET(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Left Feet
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["LEFT"] = [1.0,0.0,0.0,-0.5]
	Positions["RIGHT"] = [1.0,0.0,0.0,0.5]
	Positions["UP"] = [1.0,-0.15,0.0,0.0]
	Positions["DOWN"] = [1.0,0.25,0.0,0.0]
	Positions["LEFT_DIAGONAL"] = [1.0,0.0,0.0,-0.25]
	Positions["RIGHT_DIAGONAL"] = [1.0,0.0,0.0,0.25]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	LFeet = [bone for bone in all_bones if bone.name == "Bone_R.003"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	LFeet.quat[:] = x,y,z,r
	LFeet.insertKey(Armature_Object,endFrame,Object.Pose.ROT)
		
	return endFrame


# Feet Right
def RIGHTFEET(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Right Feet
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["LEFT"] = [1.0,0.0,0.0,-0.5]
	Positions["RIGHT"] = [1.0,0.0,0.0,0.5]
	Positions["UP"] = [1.0,-0.15,0.0,0.0]
	Positions["DOWN"] = [1.0,0.25,0.0,0.0]
	Positions["LEFT_DIAGONAL"] = [1.0,0.0,0.0,-0.25]
	Positions["RIGHT_DIAGONAL"] = [1.0,0.0,0.0,0.25]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	RFeet = [bone for bone in all_bones if bone.name == "Bone_L.003"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	RFeet.quat[:] = x,y,z,r
	RFeet.insertKey(Armature_Object,endFrame,Object.Pose.ROT)
	
	return endFrame