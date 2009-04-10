##################################################################################################
#	SCRIPT TO ANIMATE ELBOWS - LEFT AND RIGHT
#	Created, Invented and Made Alive By : Deepak Shakya
#	Date : 08-April-2008
##################################################################################################

##################################################################################################
#	This function Animates the Elbows
#
#	Armature_Object - The Bone Armature from which it selects the Elbow Bone to animate
#	direction - The final direction where the Bone has to be moved()
#	endFrame - The final frame at which the Bone has to be moved in the specified direction 
##################################################################################################

from Blender import *
import Blender

# Left Elbow
def LEFTELBOW(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Left Elbow
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["LESS_BEND"] = [2.5,0.5,0.0,-1.0]
	Positions["BEND"] = [1.0,0.5,0.0,-1.0]
	Positions["FULL_BEND"] = [0.25,0.5,0.0,-1.0]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Head Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	LElbow = [bone for bone in all_bones if bone.name == "Bone.002_R.002"][0]

	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	LElbow.quat[:] = x,y,z,r
	LElbow.insertKey(Armature_Object,endFrame,Object.Pose.ROT)
		
	return endFrame


# Right Elbow
def RIGHTELBOW(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Right Elbow
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["LESS_BEND"] = [2.5,0.5,0.0,1.0]
	Positions["BEND"] = [1.0,0.5,0.0,1.0]
	Positions["FULL_BEND"] = [0.25,0.5,0.0,1.0]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Head Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	RElbow = [bone for bone in all_bones if bone.name == "Bone.002_L.002"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	RElbow.quat[:] = x,y,z,r
	RElbow.insertKey(Armature_Object,endFrame,Object.Pose.ROT)

	return endFrame