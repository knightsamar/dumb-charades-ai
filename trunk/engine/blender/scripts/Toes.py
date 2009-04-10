##################################################################################################
#	SCRIPT TO ANIMATE TOES - LEFT AND RIGHT
#	Created, Invented and Made Alive By : Deepak Shakya
#	Date : 08-April-2008
##################################################################################################

##################################################################################################
#	This function Animates the Toes
#
#	Armature_Object - The Bone Armature from which it selects the Toe Bone to animate
#	direction - The final direction where the Bone has to be moved()
#	endFrame - The final frame at which the Bone has to be moved in the specified direction 
##################################################################################################

from Blender import *
import Blender

# Left Toe
def LEFTTOE(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Toe movements
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["UP"] = [1.0,-0.5,0.0,0.0]
	Positions["DOWN"] = [1.0,0.5,0.0,0.0]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]

	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	ToeBoneL = [bone for bone in all_bones if bone.name == "Bone_R.004"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	ToeBoneL.quat[:] = x,y,z,r
	ToeBoneL.insertKey(Armature_Object,endFrame,Object.Pose.ROT)
	
	return endFrame


#Right Toe
def RIGHTTOE(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Toe movements
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["UP"] = [1.0,-0.5,0.0,0.0]
	Positions["DOWN"] = [1.0,0.5,0.0,0.0]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]

	#Get the Head Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	ToeBoneR = [bone for bone in all_bones if bone.name == "Bone_L.004"][0]

	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	ToeBoneR.quat[:] = x,y,z,r
	ToeBoneR.insertKey(Armature_Object,endFrame,Object.Pose.ROT)
	
	return endFrame