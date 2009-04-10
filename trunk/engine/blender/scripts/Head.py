##################################################################################################
#	SCRIPT TO ANIMATE HEAD
#	Created, Invented and Made Alive By : Deepak Shakya
#	Date : 08-April-2008
##################################################################################################

##################################################################################################
#	This function Animates the Head Bone
#	Armature_Object - The Bone Armature from which it selects the Head Bone to animate
#	direction - The final direction where the Bone has to be moved()
#	endFrame - The final frame at which the Bone has to be moved in the specified direction 
##################################################################################################

from Blender import *
import Blender
	
def HEAD(Armature_Object, direction, endFrame):
	# Defining all possible positions for the Head movements
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["LEFT"] = [1.0,0.0,0.5,-0.8]
	Positions["RIGHT"] = [1.0,0.0,-0.5,0.8]
	Positions["BACK"] = [1.0,-0.35,0.0,0.0]
	Positions["FRONT"] = [1.0,0.4,0.0,0.0]
	Positions["FRONT_LEFT"] = [1.0,0.3,0.0,0.35]
	Positions["FRONT_RIGHT"] = [1.0,0.3,0.0,-0.35]
	Positions["BACK_LEFT"] = [1.0,-0.15,0.0,0.35]
	Positions["BACK_RIGHT"] = [1.0,-0.15,0.0,-0.35]
	Positions["TILT_LEFT"] = [1.0,0.0,-0.25,-0.25]
	Positions["TILT_RIGHT"] = [1.0,0.0,0.25,0.25]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	Positions["STRAIGHT_LEFT"] = [1.0,0.0,0.20,-0.3]
	Positions["STRAIGHT_RIGHT"] = [1.0,0.0,-0.20,0.3]

	#Get the Head Bone from the Armature Objects
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	HeadBone = [bone for bone in all_bones if bone.name == "Bone.004"][0]	
	
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	HeadBone.quat[:] = x,y,z,r
	HeadBone.insertKey(Armature_Object,endFrame,Object.Pose.ROT)
	
	return endFrame