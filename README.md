DCCV - Dict.Cn Console Version
==============================
Current version: v0.26


Features
---------
It's a simple and convenient tool for Linux and Cygwin users to query words in console bases on the Internet.

Can translate between English and(not only to) Chinese

It can cache the result when you query a word for the first time.
When you query it again, there is no need for the Internet and the speed will go faster.


Depandencies
------------
python 2.3 or upper

For Linux you need xsel to access the clipboard


Installation Instructions
-------------------------
if you use bash:
    $ sh install.sh

or:
    you should know what to do with install.sh


Usage
------
The following command query the word 'hello':
	
	$ d hello

Chineses are the same:

	$ d 你好

For phrases are the same, for instance 'Thanksgiving Day':

	$ d Thanksgiving Day

or:

	$ d "Thanksgiving Day"

If you do not specify what to query, DCCV will get a word from your clipboard.
In this case, all you need is:

	$ d
