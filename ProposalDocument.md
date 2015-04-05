# Introduction #

This is the document that was submitted to the Course Incharge describing our intent and the project in more detail than the words "_AI-wala dumb charades_"

# Aim #
A program which can enact a given movie title so that the person in front can easily guess it.

# Model #
dumb charades(dum-sheraz) game

# Short Description #
Like a dumb actor in the dumb charades games, the program will enact graphically(without sound) or display the verbose text which highly HINTS the movie name (but does not contain it in anyway), making it easier for the user to guess it. The program will use an actor (a stick figure) -- intelligent agent -- which acts in graphical mode and prints sentences in verbose/command-line mode.

# Method #
We shall use
  1. visual signs(both animated and static), symbols(graphics) for the graphical representation
    * Will search for names with similar sounds(Eg. soundex() in oracle)
    * Every action is divided into steps(describing the angle,motion,direction)
    * Signs(sign language) are fed to show letters, if enactment is not possible.
  1. verbose text describing the (acting)/(hints)
  1. a knowledge-base which will be made of and be upgraded by
    * pre-defined action sequences(videos), graphic symbols(images) and hints which are "natural" to the maximum audience.
    * google-based image and video search(using audio-transcription facility) so that new knowledge can be acquired or "new" words can be easily enacted.
    * a user-based teaching mechanism where the user rates each and every attempt at dumb-charades by the computer and can also "suggest" (by uploading a stored video/image or writing code for action sequences to be performed).

# Features #
  1. You can choose from a variety of characters - Male,Female
  1. Audio - Eg. Applause on winning
  1. There will be multiple difficulty levels, depending on the no. of hints and timing.
  1. Response time, profiling, top scorer/level are recorded.
  1. User can ask for a change of movie while playing and start again.
  1. Words will be broken into nouns and/or verb, thesaurus will be used to search for synonyms.
  1. Time limit for playing the game.

# Technologies #
  1. <strike>Adobe Flex</strike>
  1. Python

# WHY AND HOW DO WE WANT TO DO THIS PROJECT ? #
In creating the above program, we intend to explore and learn the following sub-fields in AI:
  1. Deduction/Reasoning/Problem solving
  1. Knowledge representation
  1. Machine Learning -- supervised
  1. Search and optimization -- using heurisitcs
  1. Logic -- fuzzy ('if nearly this')

Thus, it would require a basic study of each of these highly acclaimed fields and a deep understanding of the game of dumb charades and the human mind -- which is what fascinates us and drives towards this goal. Practically, we see an application in the field of education using sign languages and other fields where visual signs are easy-to-use and significant (eg. traffic control).


# REFERENCE MATERIAL (Realized uptill now) #
  1. en.wikipedia.org/wiki/AI
  1. John McCarthy's AI FAQ -- http://www-formal.stanford.edu/jmc/whatisai/whatisai.html
  1. Artificial Intelligence: A Modern Approach by Russell and Norvig
  1. What Computers still can't do -- MIT Press
  1. John McCarthy's 'Advice Taker'
  1. J. Alan Robinson's alogrithm for logical deduction, 1963.
  1. Marvin Minsky and Seymour Papert

# Tests #
It should be able to easily represent the following movie titles, (in increasing order of 'difficulty'):
  1. 'I Love You'		-- by 15th of Jan
  1. 'Rumour has it' 		-- by 20th of Jan
  1. 'Terminator'		-- by 1st of Feb
  1. 'Clueless'			-- by 10th of March
  1. 'Schindler's List'		-- by 20th of March