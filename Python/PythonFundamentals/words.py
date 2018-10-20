from urllib.request import urlopen


def fetch_words():
	with urlopen('http://sixty-north.com/c/t.txt') as story:
		story_words = []
		for line in story:
		    line_words = line.decode('utf-8').split()
		    for word in line_words:
		        story_words.append(word)

	for word in story_words:
		print(word)




# inside python REPL

"""
rango@bluehost:~/Coding-Practice/Python/PythonFundamentals$ python3
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import words
>>> words.fetch_words()
It
was
the
best
+ many words below

>>> 
"""

"""
we can also import this in REPL as 
>>> from words import fetch_words
"""



print(__name__) # evaluate to module name i.e. "words"

# after adding the above line we get this in REPL
"""
rango@bluehost:~/Coding-Practice/Python/PythonFundamentals$ python3
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import words
words
>>> 
"""

# as a script
"""
rango@bluehost:~/Coding-Practice/Python/PythonFundamentals$ python3 words.py 
__main__
"""

