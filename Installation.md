# Introduction #

  * Apache and mod-python
> > Install mod-python (www.mod-python.org)


> Inside apache's virtual hosts file, add
```
        #for appy -- added for AppY
        #appy is the dumb-charades-game.
        <Directory "/var/www/appy/engine/">
                AddHandler mod_python .py
                PythonHandler AJAXSensor #no .py extension for this
                PythonDebug On
        </Directory>
```
  * MySQL database
> > Create a database called 'appy'
> > Import the appy.sql script
> > Create a user 'appy' and password 'dumb\_charades\_ai' and grant all on appy.**from localhost.
> > Install python support for MySQL -- MySQLdb extension.**

  * NLTK and nltk\_data
> > Download and install nltk. (www.nltk.org)
> > Start nltk.download() and download the wordnet corpora.

# Details #

Add your content here.  Format your content with:
  * Text in **bold** or _italic_
  * Headings, paragraphs, and lists
  * Automatic links to other wiki pages