##################################################################################################
#	SCRIPT TO ANIMATE SHOULDERS - LEFT AND RIGHT
#	Created, Invented and Made Alive By : Deepak Shakya
#	Date : 08-April-2008
##################################################################################################

##################################################################################################
#	This function Animates the Shoulders
#
#	Armature_Object - The Bone Armature from which it selects the Shoulder Bone to animate
#	direction - The final direction where the Bone has to be moved()
#	endFrame - The final frame at which the Bone has to be moved in the specified direction 
##################################################################################################

from Blender import *
import Blender

# Left Shoulder
def LEFTSHOULDER(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Left Shoulder
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["UP"] = [1.0,0.0,0.0,0.15]
	Positions["FRONT"] = [1.0,0.15,0.0,0.0]
	Positions["BACK"] = [1.0,-0.15,0.0,0.0]
	Positions["DOWN"] = [1.0,0.0,0.0,-0.1]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	LShoulder = [bone for bone in all_bones if bone.name == "Bone.002_R"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	LShoulder.quat[:] = x,y,z,r
	LShoulder.insertKey(Armature_Object,endFrame,Object.Pose.ROT)
		
	return endFrame


# Right Shoulder
def RIGHTSHOULDER(Armature_Object, direction, endFrame):
	#Defining all possible positions for the Right Shoulder
	# first attribute - i am still guessing(nothing happens if changed from 1.0)
	# second attribute - it moves the head move up and down
	# third attribute - it is making the bone to rotate on axis (0.5 corresponds to 90 degree rotation)
	# fourth attribute - it is making the bone move left and right
	Positions = {}
	Positions["UP"] = [1.0,0.0,0.0,-0.15]
	Positions["FRONT"] = [1.0,0.15,0.0,0.0]
	Positions["BACK"] = [1.0,-0.15,0.0,0.0]
	Positions["DOWN"] = [1.0,0.0,0.0,0.1]
	Positions["DEFAULT"] = [1.0,0.0,0.0,0.0]
	
	#Get the Bone from the Armature Object
	pose_bones = Armature_Object.getPose()
	all_bones = pose_bones.bones.values()
	RShoulder = [bone for bone in all_bones if bone.name == "Bone.002_L"][0]
		
	#Set the frame in which the Position will be reached
	x = Positions[direction][0]
	y = Positions[direction][1]
	z = Positions[direction][2]
	r = Positions[direction][3]
	RShoulder.quat[:] = x,y,z,r
	RShoulder.insertKey(Armature_Object,endFrame,Object.Pose.ROT)
		
	return endFrame