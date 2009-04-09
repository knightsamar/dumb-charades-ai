#!/usr/bin/env python

#import urllib # I don't think this is being used anywhere anymore...
import urllib2
import re

def getImages(word=None):
	##########################################################
	#	Preparing to get the html data from the Google Image
	##########################################################
	if word is None: word = raw_input("What word to get images for ?");
	response = None
	url = 'http://images.google.com/images?q='+word
	user_agent = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008101315 Ubuntu/8.10 (intrepid) Firefox/3.0.3'
	header = {'User-Agent' : user_agent}

	#######################################################################
	#	Creating a request to the server and open the url to get the data
	#######################################################################

	req = urllib2.Request(url)
	req = urllib2.Request(url,None,header)
	response = urllib2.urlopen(req)

	#######################################################################
	#	HTML response has been received. Use it to get the images from it
	#
	#	result = re.compile('dyn.setResults\((.*)\);').findall(data)
	#
	#	p = result[0].split('],[')
	#
	#	for item in p:
	#		print '\nhttp://tbn0.google.com/images?q=tbn:'+item.split(",")[2][1:-1]
	#	
	#
	#
	#
	#######################################################################
	image = []
	html_data = response.read()
	response.close()

	#######################################################################
	#	This section of code has been removed. It will find img tags in normal web pages, but 
	#	not in google. Google first gets all the image information in a javascript object and then
	#	uses it to generate the page dynamically. So we had to extract the data from the 
	#	javascript object
	#
	#	img_data=re.compile('src="(.*)').findall(html_data)
	#
	#	for item in img_data:
	#		#image.append('<img src="'+url+re.compile('.*?"').findall(item)[0][:-1]+'" />')
	#		image.append(url+re.compile('.*?"').findall(item)[0][:-1])
	#
	#	BELOW IS THE NEWER VERSION THAT WORKS FOR GOOGLE IMAGE SEARCH
	#######################################################################

	image = []

	img_data = re.compile('dyn.setResults\((.*)\);').findall(html_data)
	img_data = img_data[0].split("],[")
	for item in img_data:
		image.append('http://tbn0.google.com/images?q=tbn:'+item.split(',')[2][1:-1])

	#######################################################################
	#	All the image tags have been extracted. Send to the xml file
	#######################################################################
	xml_file_data = '<?xml version="1.0" encoding="utf-8" ?>'
	xml_file_data += '\n<word-images>'
	xml_file_data += '\n\t<word>'+word+'</word>'
	xml_file_data += '\n\t<images>'

	counter = 0
	for item in image:
		counter = counter + 1
		xml_file_data += '\n\t\t<image srlno="' + counter.__str__() + '" url="' + item.__str__() + '" />'

	xml_file_data += '\n\t</images>'
	xml_file_data += '\n</word-images>'

	#######################################################################
	#	Write the xml data into the xml_file
	#######################################################################

	xml_file = open("./word_image_test.xml","w")
	xml_file.write(xml_file_data)
	xml_file.close()
