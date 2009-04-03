#!/usr/bin/env python
#
#       manywords.py
#       
#       Copyright 2009 Live session user <ubuntu@ubuntu>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import nltk

word = "slumdog"
split_word_list = []
#Deepak - single words ki bhi ahmiyat hoti hai

i = 0	# i - traverses from begining to end
k = 0	# k - used to extract all characters k characters from ith position ahead
j = len(word) # j - used for termination condition


while (i<=j):
	k = i+1
	while (k<=j):
		word_part = word[i:k]
		#print word_part," ==> ",len(nltk.corpus.wordnet.synsets(word_part))
		if (len(nltk.corpus.wordnet.synsets(word_part)) > 0):
			split_word_list.append(word_part)
		k = k+1
		
	i = i+1

i=0
total = len(split_word_list)

while (i<total):
	split_word_list[i] = [split_word_list[i],len(split_word_list[i])]
	print split_word_list[i]
	i = i + 1


