##################################################################################################
#	SCRIPT TO ANIMATE WAIST
#	Created, Invented and Made Alive By : Deepak Shakya
#	Date : 08-April-2008
##################################################################################################

##################################################################################################
#	This function Animates the Waist
#
#	Armature_Object - The Bone Armature from which it selects the Waist Bone to animate
#	direction - The final direction where the Bone has to be moved()
#	endFrame - The final frame at which the Bone has to be moved in the specified direction 
##################################################################################################

from Blender import *
import Blender

# Body
def WAIST(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Waist
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["LEFT"] = [1.0,0.0,0.0,-0.1]
	Positions["FRONT"] = [1.0,0.5,0.0,0.0]
	Positions["BACK"] = [1.0,-0.5,0.0,0.0]
	Positions["RIGHT"] = [1.0,0.0,0.0,0.1]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	BoneWaist = [bone for bone in all_bones if bone.name == "Bone"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	BoneWaist.quat[:] = x,y,z,r
	BoneWaist.insertKey(Armature_Object,endFrame,Object.Pose.ROT)
		
	return endFrame