import re;
import random;

def removeExtraApostropheS(movie_title,tokenized_list):
	'''Function removes extra 's' appearing as word in the tokenized list'''

	original_words = len(movie_title.split());	# original words in the movie title - space separated
	tokenized_words = len(tokenized_list);		# get the total words in the tokenized list

	if (original_words < tokenized_words):
		# the tokenized list contains extra words - lets check for 's words
		apos_s_pattern = re.compile("'s");	# regular expression for finding the 's in the movie title
		apos_s_words = len(apos_s_pattern.findall(movie_title));	# find all the occurrences of 's in the movie title
		
		
		if (apos_s_words > 0):
			for i in range(0,apos_s_words):
				tokenized_list.remove("s");
	
	return tokenized_list;

def debugger(msg):
	'''debugger prints the given debug msg on screen/in debug file log'''
	debugger_output = "con"
	if debugger_output == "con":#console 
		print ("--> %s <--") % (msg)
	else:
		df = open(debugger_output,"a");
		df.write(str(msg));
		df.close();

#just a placeholder func
def findinDatabase(word):
	'''finds a word in the database and returns True/False, action_seq_id and length of action_seq'''
	return (random.choice([True,False]),random.choice(range(0,10)),random.choice(range(9,15))) #simulate existence of a word in database
#function ends here

def error_logger(req,error):
	req.write("Error occured :"+ error);
	return True;
