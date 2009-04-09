'''sensor -- senses user response, determines the 'right' thing to do, does it and RECORDS the action taken.

	TO DO : How actually will these sensors be fired ? -- what technically will make these sensors fire ?
	SUGGESTION: we have a central AJAX-CGI file which interacts to user events WHILE the game is ON.
				Find something better than AJAX-CGI...mod-python ?
				
	can we just show a green halo for the  words rightly guessed, red for wrong and orange for nearly ?
'''

def userEnteredWordSensor(user_input):
	#what stage are we currently in ? -- whether AS,IM or WI ?
	#what response did user enter ?
	if exactly_right:
			#save our total action plan.
			#LOG the path
			#procede to the next word.
			pass;
	elif nearly_right:
			#nearly right means -->
				#one of the tags
				#its a synonym
				#tags's synonym...?
			#do the 'next' action.
			#update the waypoints information --- how much NEXTS did an action/image/wi require ?
			#give control to the client
			pass;
	elif not_at_all_right and time_up:
			#so, what stage are we currently in ? 
			#if AS, procede to IM 
			#if IM, procede to WI.
			#if WI, procede to next word.
			#LOG the action, update the waypoints information.
			print 'Hey dude, you dont seem to guess this word...Lets go to the next one';

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
