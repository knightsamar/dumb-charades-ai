import re;
import nltk;
from functions import *;

###take the movie title 
#movie_title = raw_input("Enter Movie Title ==>")
file = open("../test_data/movie_250","r")	#take it from the top 250 db of IMDB
#read the movie title
movie_title = file.readline()

###start processing.
print 'Shh! I am going to enact-->', movie_title;

#where is the user from ? -- take this from client.html
user_location = raw_input("Where are you from ?");

#have we already performed this movie title ?

#start individual word processing
while True:
	#get the intividual words
	word_list = nltk.word_tokenize(movie_title)
	
	#remove the extraApostrophes
	word_list = removeExtraApostropheS(movie_title,word_list);
	print "After removeExtraApostropheS -->", word_list
	
	#scan the list for determining the EASIEST one and so on... -- the order of performance
	#this is an ordered tuple(word, priority(default 0), action_seq_id)
	ordered_list = []
	t = 0;
	
	ordered_list = determineOrder(word_list)
	for w in ordered_list:
		#convert to singular --> no need, nltk CAN process plurals as well.
		print "Processing %s" % w
		
		#do we have a corresponding action sequence in db ?
		
		#database search --
		#somethign like --> if x in databaseList():
		#if yes, assign +1 
		#if no, assign -1
		
		
		inDatabase, action_seq_id, length = findinDatabase(w)	#tuple unpacking
		
		if inDatabase:
			ordered_list += [w, +1, action_seq_id, length]
		else:
			ordered_list += [w, -1, None, None]
		
		#sort on the basis of length of action sequence 
		
	print ordered_list;
	break;

print "Done"
