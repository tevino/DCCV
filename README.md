DCCV - Dict.Cn Console Version
==============================
Current version: v0.25
Author: mail2tevin@gmaill.com


Features
---------
It's a simple and convenient tool for Linux and Cygwin users to query words in console bases on the Internet.

Can translate between English and(not only to) Chinese

It can cache the result when you query a word for the first time.
When you query it again, there is no need for the Internet and the speed will go faster.


Depandencies
------------
python 2.5 or upper
sqlite3

For Linux you need xsel to access the clipboard


Installation Instructions
-------------------------
Run install.sh


Usage
------
The following command query the word 'hello':
	
	$ d hello

Chineses are the same:

	$ d 你好

For phrases, for instance 'Thanksgiving Day':

	$ d "Thanksgiving Day"

or:

	$ d "Thanksgiving Day"

If you do not specify the word to query, DCCV will get word from your clipboard.
In this case, you just need to:

	$ d
