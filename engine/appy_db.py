##############################################################################
#	This is the database connector class file that appy uses to make 
#	transactions with the mysql database.
#
#	Created By : Gayatri Venugopal
#	Date : 02-04-2009
#
#	Modified By : Deepak Shakya & Samarendra Manohar Hedaoo
##############################################################################

class accessDb:
	########################## All important members #########################
	connection = None				# stores the connection
	cursor = None					# makes all transactions with the database
	host = 'localhost'				# MySQL server host
	username = 'appy'				# MySQL server username
	password = 'dumb_charades_ai'	# MySQL server password
	database = 'appy'				# MySQL server database
	debug_mode = False				# Determines the mode of operation. If true, details messages are returned 
									#for various operations

	####################################################################
	#	openConnection - Opens the connection to the MySQL database
	#		In debug mode - returns the explanatory information
	#		In normal mode - returns True if successfully connected, False otherwise
	####################################################################
	def openConnection:
		try:
			connection = MySQLdb.connect(host,username,password,database)
			cursor = connection.cursor()
			if (debug_mode)
				return "Successfully connected to the database"
			else
				return True
		except MySQLdb.Error e
			if (debug_mode)
				return "Unable to connect to the database - Error %d: %s" % (e.args[0], e.args[1])
			else
				return False
		else:
			connection.close()


	####################################################################
	#	closeConnection - terminates the connection to the MySQL database
	#		In debug mode - returns the explanatory information
	#		In normal mode - returns True if successfully connected, False otherwise
	####################################################################

	def closeConnection:
		try:
			cursor.close()			# close the cursor
			connection.commit()		# commit database changes
			connection.close()		# close the connection to the database
			if (debug_mode)
				return "Successfully connected to the database"
			else
				return True
		except MySQLdb.Error e
			if (debug_mode)
				return "Unable to connect to the database - Error %d: %s" % (e.args[0], e.args[1])
			else
				return False
		else:
			connection.close()


	def setDebugMode(mode):
		debug_mode = mode

	def getDebugMode(mode):
		return debug_mode

	def executeQuery(sqlString):
		openConnection()
		try:
			cursor.execute(sqlString)
			result_set = cursor.fetchall ()
   		#for row in result_set:
     	#	print "%s, %s" % (row["name"], row["category"])
   		#	print "Number of rows returned: %d" % cursor.rowcount
		#if(debug_mode):
				#return "query executed successfully"
			return result_set;
		except MySQLdb.Error e:
			if (debug_mode
			return False
		else:
			closeConnection()

	def createAcSeq:
		cursor.execute("DROP TABLE IF EXISTS `action_sequence`")
		cursor.execute("""
		CREATE TABLE `action_sequence`
		(  `actionseqid` int(10) NOT NULL,
		  `actionseq` blob NOT NULL,
		 `tags` varchar(500) NOT NULL,
		 PRIMARY KEY  (`actionseqid`)
		 ENGINE=MyISAM DEFAULT CHARSET=latin1
		""")


	def createMovPath:
		cursor.execute("DROP TABLE IF EXISTS `movie_path'")
		cursor.execute("""
		CREATE TABLE `movie_path`
		(  `movieid` int(10) NOT NULL,
		 `wordid` int(10) NOT NULL,
		 `pathid` int(10) NOT NULL)
		 ENGINE=MyISAM DEFAULT CHARSET=latin1
		""")


	def createMovTitles:
		cursor.execute("DROP TABLE IF EXISTS `movie_titles`")
		cursor.execute("""
		CREATE TABLE `movie_titles`
		( `movieid` int(10) NOT NULL,
		 `movietitle` varchar(300) NOT NULL,
		 PRIMARY KEY  (`movieid`)) 
		ENGINE=MyISAM DEFAULT CHARSET=latin1
		""")


	def createPath:
		cursor.execute("DROP TABLE IF EXISTS `path`")
		cursor.execute("""
		CREATE TABLE `path` 
		( `pathid` int(10) NOT NULL,
		  `userid` int(10) NOT NULL,
		  `wordid` int(10) NOT NULL,
		  `successrate` float(5,2) NOT NULL,
		  PRIMARY KEY  (`pathid`)
		) ENGINE=MyISAM DEFAULT CHARSET=latin1
		""")


	def createTags:
		cursor.execute("DROP TABLE IF EXISTS `tags`")
		cursor.execute("""
		CREATE TABLE `tags` 
		( `tagid` int(10) NOT NULL,
		  `tag` varchar(100) NOT NULL,
		  PRIMARY KEY  (`tagid`)
		) ENGINE=MyISAM DEFAULT CHARSET=latin1
		""")



	def createTime:
		cursor.execute("DROP TABLE IF EXISTS `time`")
		cursor.execute("""
		CREATE TABLE `time` 
		( `userid` int(10) NOT NULL,
		  `responsetime` time NOT NULL
		) ENGINE=MyISAM DEFAULT CHARSET=latin1
		""")


	def createUsers:
		cursor.execute("DROP TABLE IF EXISTS `users`")
		cursor.execute("""
		CREATE TABLE `users` 
		( `userid` int(10) NOT NULL,
		  `username` varchar(100) NOT NULL,
		  `location` int(90) NOT NULL,
		  PRIMARY KEY  (`userid`))
		 ENGINE=MyISAM DEFAULT CHARSET=latin1
		""")



	def createWayPt:
		cursor.execute("DROP TABLE IF EXISTS `waypoint`")
		cursor.execute("""
		CREATE TABLE `waypoint` 
		( `pathid` int(10) NOT NULL,
		  `type` enum('AS','Image','WI') NOT NULL COMMENT 'AS-ActionSequence, Image - ImageNo, WI - Word Info',
		  `waypointinfo` varchar(10) NOT NULL COMMENT 'ASid/ImageNo/WordId',
		  `responsetime` time NOT NULL COMMENT 'time for correst response or to go to next waypoint'
		) ENGINE=MyISAM DEFAULT CHARSET=latin1
		""")



	def createWords:
		cursor.execute("DROP TABLE IF EXISTS `words`")
		cursor.execute("""
		CREATE TABLE `words`
		( `wordid` int(10) NOT NULL,
		  `word` varchar(100) NOT NULL,
		  `category` varchar(50) NOT NULL,
		  `tags` varchar(500) NOT NULL,
		  PRIMARY KEY  (`wordid`)
		) ENGINE=MyISAM DEFAULT CHARSET=latin1
		""")



	def updateAcSeq:
		cursor.execute("""
		update action_sequence set = where
		""")


	def updateMovPath:
		cursor.execute("""
		update movie_path set = where
		""")



	def updateMovTitles:
		cursor.execute("""
		update movie_titles set = where
		""")



	def updatePath:
		cursor.execute("""
		update path set = where
		""")



	def updateTags:
		cursor.execute("""
		update tags set = where
		""")



	def updateTime:
		cursor.execute("""
		update time set = where
		""")



	def updateUsers:
		cursor.execute("""
		update users set = where
		""")



	def updateWayPt:
		cursor.execute("""
		update waypoint set = where
		""")



	def updateWords:
		cursor.execute("""
		update words set = where
		""")




	def insertAcSeq:
		cursor.execute("""
		INSERT INTO action_sequence (cols) VALUES ('')
		""")



	def insertMovPath:
		cursor.execute("""
		INSERT INTO movie_path (cols) VALUES ('')
		""")


	def insertMovTitles:
		cursor.execute("""
		INSERT INTO movie_titles (cols) VALUES ('')
		""")



	def insertPath:
		cursor.execute("""
		INSERT INTO path (cols) VALUES ('')
		""")



	def insertTags:
		cursor.execute("""
		INSERT INTO tags (cols) VALUES ('')
		""")




	def insertTime:
		cursor.execute("""
		INSERT INTO time (cols) VALUES ('')
		""")



	def insertUsers:
		cursor.execute("""
		INSERT INTO users (cols) VALUES ('')
		""")



	def insertWayPt:
		cursor.execute("""
		INSERT INTO waypoint (cols) VALUES ('')
		""")




	def insertWords:
		cursor.execute("""
		INSERT INTO words (cols) VALUES ('')
		""")



	def delete:
		pass;

	def alter:
		pass;

	
