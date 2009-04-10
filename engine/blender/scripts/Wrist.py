##################################################################################################
#	SCRIPT TO ANIMATE WRISTS - LEFT AND RIGHT
#	Created, Invented and Made Alive By : Deepak Shakya
#	Date : 08-April-2008
##################################################################################################

##################################################################################################
#	This function Animates the Wrists
#
#	Armature_Object - The Bone Armature from which it selects the Wrist Bone to animate
#	direction - The final direction where the Bone has to be moved()
#	endFrame - The final frame at which the Bone has to be moved in the specified direction 
##################################################################################################

from Blender import *
import Blender

# Left Wrist
def LEFTWRIST(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Left Wrist
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["UP"] = [1.0,-0.8,0.0,0.0]
	Positions["DOWN"] = [1.0,0.5,0.0,0.05]
	Positions["LEFT"] = [1.0,0.0,0.0,-0.4]
	Positions["RIGHT"] = [1.0,0.0,0.0,0.35]
	Positions["FLIP"] = [1.0,0.0,-1.0,0.0]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Head Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	LWrist = [bone for bone in all_bones if bone.name == "Bone.002_R.003"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	LWrist.quat[:] = x,y,z,r
	LWrist.insertKey(Armature_Object,endFrame,Object.Pose.ROT)

	return endFrame


# Right Wrist
def RIGHTWRIST(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Right Wrist
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["UP"] = [1.0,-0.8,0.0,0.0]
	Positions["DOWN"] = [1.0,0.5,0.0,0.05]
	Positions["LEFT"] = [1.0,0.0,0.0,-0.4]
	Positions["RIGHT"] = [1.0,0.0,0.0,0.35]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Head Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	RWrist = [bone for bone in all_bones if bone.name == "Bone.002_L.003"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	RWrist.quat[:] = x,y,z,r
	RWrist.insertKey(Armature_Object,endFrame,Object.Pose.ROT)
	
	return endFrame