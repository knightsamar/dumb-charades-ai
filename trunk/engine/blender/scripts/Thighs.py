##################################################################################################
#	SCRIPT TO ANIMATE TIGHS - LEFT AND RIGHT
#	Created, Invented and Made Alive By : Deepak Shakya
#	Date : 08-April-2008
##################################################################################################

##################################################################################################
#	This function Animates the Tighs
#
#	Armature_Object - The Bone Armature from which it selects the Tigh Bone to animate
#	direction - The final direction where the Bone has to be moved()
#	endFrame - The final frame at which the Bone has to be moved in the specified direction 
##################################################################################################

from Blender import *
import Blender

# Left Thigh
def LEFTTHIGH(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Left Thigh
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["FRONT"] = [1.0,-0.4,0.0,0.0]
	Positions["BACK"] = [1.0,0.4,0.0,0.0]
	Positions["SIDE"] = [1.0,0.0,0.0,-0.35]
	Positions["SIDE_UP"] = [1.0,0.0,0.0,-0.65]
	Positions["FRONT_LEFT"] = [1.0,-0.35,0.0,-0.4]
	Positions["FRONT_RIGHT"] = [1.0,-0.35,0.0,0.4]
	Positions["FRONT_UP"] = [1.0,-0.8,0.0,0.0]
	Positions["FRONT_LEFT_UP"] = [1.0,-0.8,0.0,-0.4]
	Positions["FRONT_RIGHT_UP"] = [1.0,-0.8,0.0,0.4]
	Positions["BACK_LEFT"] = [1.0,0.4,0.0,-0.3]
	Positions["BACK_RIGHT"] = [1.0,0.4,0.0,0.3]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	LThigh = [bone for bone in all_bones if bone.name == "Bone_R.001"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	LThigh.quat[:] = x,y,z,r
	LThigh.insertKey(Armature_Object,endFrame,Object.Pose.ROT)
		
	return endFrame


# Right Thigh
def RIGHTTHIGH(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Right Thigh
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["FRONT"] = [1.0,-0.4,0.0,0.0]
	Positions["BACK"] = [1.0,0.4,0.0,0.0]
	Positions["SIDE"] = [1.0,0.0,0.0,0.35]
	Positions["SIDE_UP"] = [1.0,0.0,0.0,0.65]
	Positions["FRONT_LEFT"] = [1.0,-0.35,0.0,-0.4]
	Positions["FRONT_RIGHT"] = [1.0,-0.35,0.0,0.4]
	Positions["FRONT_UP"] = [1.0,-0.8,0.0,0.0]
	Positions["FRONT_LEFT_UP"] = [1.0,-0.8,0.0,-0.4]
	Positions["FRONT_RIGHT_UP"] = [1.0,-0.8,0.0,0.4]
	Positions["BACK_LEFT"] = [1.0,0.4,0.0,-0.3]
	Positions["BACK_RIGHT"] = [1.0,0.4,0.0,0.3]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	RThigh = [bone for bone in all_bones if bone.name == "Bone_L.001"][0]
	
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	RThigh.quat[:] = x,y,z,r
	RThigh.insertKey(Armature_Object,endFrame,Object.Pose.ROT)

	return endFrame