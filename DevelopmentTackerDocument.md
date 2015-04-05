# Development Tracker Document #



## Date : 12th March 2009 ##
Written By Deepak Shakya

Following software have been installed for setting up the server environment. The server environment is Linux based.<br />
1. [Python 2.5](http://www.python.org/download/)<br />
2. [Natural Language Toolkit](http://www.nltk.org/download)<br />
3. [NumPy](http://sourceforge.net/projects/numpy) - Numerical Python adds a fast and sophisticated array facility to the Python language. NumPy is the most recent and most actively supported package.<br />
4. [MatPlotLib](http://sourceforge.net/projects/matplotlib/) - Matplotlib is a pure python plotting library with the goal of making publication quality plots using a syntax familiar to matlab users. The library uses numpy for handling large data sets and supports a variety of output backends<br />
5. [Prover9](http://www.cs.unm.edu/~mccune/mace4/) - Prover9 is an automated theorem prover for first-order and equational logic, and Mace4 searches for finite models and counter examples.<br />
6. [PyBrain](http://pybrain.org/) - yBrain is a modular Machine Learning Library for Python. It's goal is to offer flexible, easy-to-use yet still powerful algorithms for Machine Learning Tasks and a variety of predefined environments to test and compare your algorithms.<br />
7. [VPython](http://vpython.org/) -


---

### Python 2.5 ###
One can compile the source code for Python 2.5. For debian systems, type following command<br />

`sudo apt-get install python`<br /><br />



### Natural Language Toolkit (NLTK) ###
Obtain the zip file from [here](http://nltk.googlecode.com/files/nltk-0.9.8.zip). Extract and install the toolkit by running `setup.py`<br /><br />
To get the NLTK data -
  * `python -m nltk.downloader`<br />
  * Select `wordnet` and `words` to fetch the list of words in the toolkit



### NumPy - ###
`sudo apt-get install python-numpy` -- debian based systems<br />
Download and compile the tar.gz for others<br /><br />



### MatPlotLib ###
`sudo apt-get install python-matplotlib` -- debian based systems<br />
Download and compile the tar.gz for others.<br /><br />


### Prover9 ###
`sudo apt-get install prover9` -- debian based systems<br />
Download the tar.gz [here](http://www.cs.unm.edu/%7Emccune/prover9/gui/p9m4-v05.tar.gz) and compile it.<br /><br />

### PyBrain ###
[Here](http://pybrain.org/docs/quickstart/installation.html) you would find the steps to install the PyBrain library.<br />
We preferred the zip version to compile the code. Got some error with g++<br />
Here is the error looks like --<br />
`distutils.errors.CompileError: command 'g++' failed with exit status 1`<br />
<br />
Exact details of the error are --<br />
`arac/src/c/layers/common.c: In function 'void make\_layer(Layer**, int, int)':**<br />
arac/src/c/layers/common.c:12: error: ‘malloc’ was not declared in this scope<br />
arac/src/c/layers/common.c: In function 'Layer**make\_layer(int, int)':**<br />
arac/src/c/layers/common.c:40: error: 'malloc' was not declared in this scope`
<br /><br />

So, got the patch [here](http://mglab.blogspot.com/2009/03/pythonpybrain-0.html). Its in Japanese and was not getting translated. But, i guess the solution was pretty simple so my very good friends knightsamar phrased it out... ;) Kudos to you. Here is what he did.<br />
  * open this file in the extracted folder - arac/src/c/common.h
  * insert `#include<stdlib.h>` in the file and save it.
  * `sudo python setup.py build` and then `sudo python setup.py install`
The same steps are available at that Japanese site.<br /><br />


### VPython ###
This one is trickier. You have to get some other stuff before you can compile this one.<br />
--GtkGLExt
  * <strike><a href='http://www.sgi.com/products/software/opensource/glx/'>GLX</a> - you will need this. So download and extract it. Copy the folder into the gtkglext folder. And copy the header files in the top level directory</strike>
  * Install `libgl1-mesa-glx`, `mesa-dev`, and `mesa-common-dev`
  * Then install this `sudo apt-get install freeglut3 freeglut3-dev`.
  * Now the `make` create the problem. Anyways, commented the line 41 in following file - `gtkglext-1.2.0/gdk/x11/gdkglglxext.h`.
  * `make install` - if you're lucky enough, you might get the stuff done.
--GtkGLExtmm
  * [GtkGLExt - OpenGL Extension to GTK+](http://gtkglext.sourceforge.net/) - Get  and gtkglextmm packages.<br />
  * It gives following errors.<br />
<pre>
`No package 'gtkmm-2.4' found<br>
No package 'gdkmm-2.4' found<br>
No package 'pangomm-1.4' found`<br>
</pre>
So we installed the gtkmm (`libgtkmm-2.4-dev`) - (sudo apt-get install libgtkmm-2.4-dev) package which i guess has gdkmm and pango as their dependent packages. Anyways, the package got compiled. Kudos to the knightsamar once again...;)
<br />
<br />
<br />
  * Finally the `./configure` was successful.
  * Another problem with the `make` command.
  * Figured it out that it needs some boosting dosages (libraries like libboost-python-dev, libboost-signals-dev, and libboost-thread-dev). It might say for other dependencies as well. Go ahead and install them too. May be they boost the performance of the system.
  * So, `make` is done.
  * And `make install` too. Hurray...


Day Close Note -
  * Still have to compile vpython
  * Checked the nltk for synonyms - chapter 2 of the book (Got synonyms, definition, examples)



---