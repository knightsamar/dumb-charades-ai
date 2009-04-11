'''sensor -- senses user response, determines the 'right' thing to do, does it and RECORDS the action taken.

	TO DO : How actually will these sensors be fired ? -- what technically will make these sensors fire ?
	SUGGESTION: we have a central AJAX-CGI file which interacts to user events WHILE the game is ON.
				Find something better than AJAX-CGI...mod-python ? --- IMPLEMENTED
				
	can we just show a green halo for the  words rightly guessed, red for wrong and orange for nearly ?
	
	CONVENTION:
	all the sensors will take dataString and respond back with dict{actuator_name:{},responseString:{},responseType:'ok/nok'}
	
	written by samar - 060321011 and gayatri - 060321032
	
	This file is under Apache License.
'''
from orderDeterminer.py import *
from nltk import *;
from nltk.corpus import wordnet as wn ;
from accessDb.py import *;

def userEnteredWordSensor(user_input):
	#what stage are we currently in ? -- whether AS,IM or WI ?
	#what response did user enter ?
	if exactly_right: 
			#save our total action plan.	
			cursor.executeQuery("insert into path values('',session['uid'],session['wordid']")
			pathid=cursor.executeQuery("select pathid from path where wordid = session['wordid']")	
			cursor.executeQuery("insert into waypoint values('',pathid,session['type'],session['waypoint_info'])")
			#LOG the path
			#procede to the next word.
			perform()
			pass;
	elif nearly_right:
			#nearly right means -->
				#one of the tags
				wid=cursor.executeQuery("Select wordid from words where word like 'session['word']'")
				tags=cursor.executeQuery("Select tags from words where wordid=wid")
				for tag in tags:
					if ( tag == word )
						#perform action sequence for NEXT
						break;
					#its synonym
					for s in wn.synsets('session['word']'):
								if( s == user_input )
									#perform action sequence for NEXT
									break;
					else:
					#tags's synonym...?	
							for s in wn.synsets('tag'):
								if( s == user_input )
									#perform action sequence for NEXT
									break;
				
						  
			#do the 'next' action.
			
			#update the waypoints information --- how much NEXTS did an action/image/wi require ?
			#give control to the client
			pass;
	elif not_at_all_right:
			ac_seq_flag1=1;
			while(ctr<len(ac_seq_list))
				ctr=ctr+1;
				ac_seq=session['ac_seq_list[ctr]'];
			
				if( ac_seq = NONE ):
					#call getImage.py
					if( ctr>0 )
						#store waypoint(ctr-1)
					img_seq = executeQuery("");
			else
				
				#perform ac_seq
			#so, what stage are we currently in ? 
			#if AS, procede to IM 
			#if IM, procede to WI.
			#if WI, procede to next word.
			#LOG the action, update the waypoints information.
			print 'Hey dude, you dont seem to guess this word...Lets go to the next one';
 elif time_up:
 			
 	
def userIdleForLongTimeSensor():
	#how long is long ? 2 minutes was the norm
	#reset the game thing
	pass;

def userEnteredNonPerformedWordSensor(nonperformed_word):
	#user entered a word which is yet to be performed
	#what stage are we currently in ? -- is the current word action complete?
	'''can we just show a green halo for the right words ?'''
	userEnteredWordSensor(unperformed_word);
	
def userGuessedtheMovieTitle():
	#applause!...?
	pass;
