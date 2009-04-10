##################################################################################################
#	SCRIPT TO ANIMATE ARMS - LEFT AND RIGHT
#	Created, Invented and Made Alive By : Deepak Shakya
#	Date : 08-April-2008
##################################################################################################

##################################################################################################
#	This function Animates the Arms
#
#	Armature_Object - The Bone Armature from which it selects the Arm Bone to animate
#	direction - The final direction where the Bone has to be moved()
#	endFrame - The final frame at which the Bone has to be moved in the specified direction 
##################################################################################################

from Blender import *
import Blender

# Left Arm
def LEFTARM(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Left Arm
	# first attribute - i am still guessing(nothing happens if changed from 1.0) - rotation in other direction
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["FRONT"] = [1.0,0.75,0.0,0.75]
	Positions["FRONT_UP"] = [1.0,0.25,0.0,1.25]
	Positions["FRONT_DOWN"] = [1.0,1.0,0.0,0.0]
	Positions["BACK"] = [1.0,-0.7,0.0,-0.5]
	Positions["BACK_UP"] = [1.0,-0.7,0.0,0.25]
	Positions["BACK_DOWN"] = [1.0,-0.25,0.0,-1.0]
	Positions["SIDE"] = [1.0,1.25,0.0,0.75]
	Positions["SIDE_UP"] = [1.0,1.25,0.0,2.0]
	Positions["SIDE_DOWN"] = [1.0,1.25,0.0,-0.25]
	Positions["UP"] = [1.0,-0.5,0.0,0.5]
	Positions["LEFT"] = [1.0,0.0,0.0,0.0]
	Positions["LEFT_UP"] = [1.0,-0.25,0.0,0.25]
	Positions["LEFT_DOWN"] = [1.0,0.25,0.0,-0.25]
	Positions["DIAGONAL_FRONT"] = [1.0,0.4,0.0,0.4]
	Positions["DIAGONAL_FRONT_UP"] = [1.0,0.15,0.0,0.5]
	Positions["DIAGONAL_FRONT_DOWN"] = [1.0,0.5,0.0,0.0]
	Positions["DIAGONAL_BACK"] = [1.0,-0.5,0.0,-0.25]
	Positions["DIAGONAL_BACK_UP"] = [1.0,-0.5,0.0,0.0]
	Positions["DIAGONAL_BACK_DOWN"] = [1.0,-0.25,0.0,-0.5]
	Positions["DEFAULT"] = [1.0,0.25,0.0,-0.5]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	LArm = [bone for bone in all_bones if bone.name == "Bone.002_R.001"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	LArm.quat[:] = x,y,z,r
	LArm.insertKey(Armature_Object,endFrame,Object.Pose.ROT)
		
	return endFrame


# Right Arm
def RIGHTARM(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Right Arm
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["FRONT"] = [1.0,0.75,0.0,-0.75]
	Positions["FRONT_UP"] = [1.0,0.25,0.0,-1.25]
	Positions["FRONT_DOWN"] = [1.0,1.0,0.0,0.0]
	Positions["BACK"] = [1.0,-0.7,0.0,0.5]
	Positions["BACK_UP"] = [1.0,-0.7,0.0,-0.25]
	Positions["BACK_DOWN"] = [1.0,-0.25,0.0,1.0]
	Positions["SIDE"] = [1.0,1.25,0.0,-0.75]
	Positions["SIDE_UP"] = [1.0,1.25,0.0,-2.0]
	Positions["SIDE_DOWN"] = [1.0,1.25,0.0,0.25]
	Positions["UP"] = [1.0,-0.5,0.0,-0.5]
	Positions["RIGHT"] = [1.0,0.0,0.0,0.0]
	Positions["RIGHT_UP"] = [1.0,-0.25,0.0,-0.25]
	Positions["RIGHT_DOWN"] = [1.0,0.25,0.0,0.25]
	Positions["DIAGONAL_FRONT"] = [1.0,0.4,0.0,-0.4]
	Positions["DIAGONAL_FRONT_UP"] = [1.0,0.15,0.0,-0.5]
	Positions["DIAGONAL_FRONT_DOWN"] = [1.0,0.5,0.0,0.0]
	Positions["DIAGONAL_BACK"] = [1.0,-0.5,0.0,0.25]
	Positions["DIAGONAL_BACK_UP"] = [1.0,-0.5,0.0,0.0]
	Positions["DIAGONAL_BACK_DOWN"] = [1.0,-0.25,0.0,0.5]
	Positions["DEFAULT"] = [1.0,0.25,0.0,0.5]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	RArm = [bone for bone in all_bones if bone.name == "Bone.002_L.001"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	RArm.quat[:] = x,y,z,r
	RArm.insertKey(Armature_Object,endFrame,Object.Pose.ROT)
	
	return endFrame