###TO DO --->
''' 1. Write a wrapper for wrapping the list of tuple(word,complete_plan,priority_points) and returning this list of tuples
	back to the actuator/AppY
	2. Write determineImages properly so that images can be actually used by AppY -- take in consideration the 
		nature of the web and better save the images in a temporary table.
	3. Write the statistical and probability calc part to determine the right actionSEQ in determineActionSeq
		-- a question, how important is it actually in the current scenario where there seems to be only one actionSeq?
		-- we shouldn't postpone writing it(being the best of our creations), but we should accomodate todays situation.
	4. Integrate the chkSyn.txt in here.
		-- if we use a synonym, lets record it.
	5. It would be better if we save the action plan for any word AFTER its completely and successfully performed --> this
		is for the sensor...but I want to write it down, lest I forget.
	6. Write good database code -- integrate Gayatri's DBConnector(with Deepak) in here.
	7. Better rename this file to orderDeterminerAndPlanner or something like that because we PLAN all the things to do here.
	8. TEST!TEST!TEST!
	
	IMP--> 9. Please have a LOGIC-CHECK On this.
'''

from manywords import breakinWords;	#for the word decomposer and recognizer
from getimages import getImages
from functions import debugger
complete_plan = [] #a list of ActionSequence,IMage,WordInfo to be used for this word.
action_sequence = image_sequence = word_info = []; #will store the relevant things in it.
mini_words = []	#for letting everyone access the constituent words inside the Word

def determineOrder(word_list):
	'''determines the order in which the words in a movie title are to be performed'''
	'''	we assign weights to words so that we know how 'easy' or 'difficult' they are to perform.
		the heavier a word, the easier it is to perform.
		-1 means very difficult.
	'''
	
	debugger('Determining order of performance of the words')
	#IDEA --> this needs to be converted into a try-catch-except chain
	for w in word_list:
		#first check whether the word exists in the KB
		complete_plan = checkWord(w);
		if complete_plan == None: #this is a NEW word!
			debugger('''%s is a NEW word''' % (w))
			#okay, whether we can determine an action sequence for this word using NLP ?
			action_sequence = determineActionSeq(w);
			if action_sequence == None: #we can't determine an action sequence for this word using NLP
				#the word doesn't have an action sequence directly...maybe we need a better idea -- break into two words and perform
				action_sequence = breakinWordsandDetermine(w);
				if action_sequence == None:#we can't determine an action sequence even after breaking it
					print ("I give up! I can't enact %s :(" % w)
					#we can't act, so lets try to get Pictures to display and make the user guess
					image_sequence = determineImages(w) 
					if image_sequence == None:
						print ("Can't show any photo for this word");
						word_info = getWordInfo();
						if word_info == None:
							print ("Can't DO ANYTHING FOR THIS word!");
							debugger("How the hell do I perform %s ?" % w); 
							points = -1; 
						else:#we found word info for this word
							debugger("Using word info...");
							complete_plan = word_info;
							points = 2;
					else:#we found images for this word
						debugger("Using images...");
						complete_plan = image_sequence;
						points = 3;
				else:#we determined action sequence by breaking into constituent words.
					debugger("Using decomposed-words action-sequences...");
					complete_plan = action_sequence
					points = 4;
			else:
				#we got an action sequence directly for this word using synonyms and tags
				debugger("Using direct(synonym and tags) action sequence...");
				complete_plan = action_sequence;
				points = 5;
		else:#we KNOW this word!
			points = 6;
			return complete_plan;
			#can we make an action sequence based on meanings ? --- the AI THINGY!	
				#else if canLearnANewSequence(w):
					#if yes +4 points gained.
					

def checkWord(w):
	'''check whether we know this word already and if yes, how do we perform it ?'''
	'''will return the total plan for the word'''
	debugger('''checking for the word in Knowledge Base''');
	
	action_plan = queryKB("select word from words where word like '%s'" % (w))
	if action_plan:
		return action_plan;
	else:
		return None;
	
'''**********the probability and statistics wala part goes here**********'''
def determineActionSeq(passedWord):
	'''checks whether the action sequence for a particular word exists in the KB and if yes which one is the best'''
	debugger("Trying to determine an action sequence for %s " (passedWord))
	#import accessDb
	#openConnection
	strTags = executeQuery("Select tags from words where word like passedWord")
	lstTags = strTags.split(',')
	for i in range(len(lstTags)):
		query="Select action_sequence from action_sequence where tags like 'lstTags[i]'" 
		strActionSeq = executeQuery(query)
		if( strActionSeq != ""):
			return None;
		else:
			return strActionSeq

def breakinWordsandDetermine(w):
	'''break the word in constituents words which may possibly have an action sequence.'''
	'''if we can determine the action sequence of only one of the words, we will still perform it.'''
	
	mini_words = breakinWords(w);#uses the function from manywords module
	mini_words_action_sequences = []; #stores the action sequence
	i = 0;
	for w in mini_words:
		mini_words_action_sequences = [determineActionSeq(w)]; #will either return the 'right' and 'best' action sequence or return None;
		#if we don't determine an action sequence for this word, don't fill None for it.
		if mini_words_action_sequences[i] == None:
			del(mini_words_action_sequences[i]) #remvoe the None element
		i = i + 1;
	
	return mini_words_action_sequences

def determineImages(w):
	'''determine the right images(courtesy: Google Image Search) to be displayed for the word'''
	debugger("determining the right images to be displayed for %s" % w)
	getImages(w);
