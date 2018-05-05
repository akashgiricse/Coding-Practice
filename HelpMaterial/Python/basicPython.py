#! Python3.6
""" Python basic tutorial 
	Learned from : https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

"""

#############################################################
              Strings
#############################################################
first_name = 'Akash'
last_name = 'Giri'

full_name = f'{first_name} {last_name}'
print(full_name) # Akash Giri
---------------------------
print(dir(first_name))
# will print all methods that can be applied to the strings
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__',
  '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
   '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 
   'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal',
    'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
     'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
      'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

------------------------------
print(help(str))
# will print all the methods that can be applied to the "str" with their description
print(help(str.lower))
# prints
Help on method_descriptor:

lower(...)
    S.lower() -> str
    
    Return a copy of the string S converted to lowercase.
-------------------------------------

#############################################################
Integers and Floats - Working with Numeric Data
#############################################################

num = 3.4
num1 = 5
print(type(num))
print(type(num1))
# print
# <class 'float'>
# <class 'int'>
---------------------------------
# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2


# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2
---------------------------------
num = -3.56

print(abs(num))
print(round(num))
print(round(4.56, 1)) # round for the first decimal num
# 3.56
# -4
# 4.6

--------------------------------
num1 = '100'
num2 = '200'

print(int(num1) + int(num2)) # casting of datatype
# 300


#############################################################
Lists, Tuples, and Sets
#############################################################

----------------------------------
List [ ]
---------------------------------
# list are mutable  means they can be modified
list_1 = ['cat', 'rat', 'bat', 'mat', 'pat']
list_2 = ['ham', 'cam', 'maam']

list_1.append('chat')
list_1.insert(0, 'vat')
list_1.insert(0, list_2)

print(list_1)
# insert list_2 to list_1
# [['ham', 'cam', 'maam'], 'vat', 'cat', 'rat', 'bat', 'mat', 'pat', 'chat']

extended_list = list_1.extend(0, list_2)
print(extended_list)

------------------------------------
list_1 = ['cat', 'rat', 'bat', 'mat', 'pat']
list_2 = ['ham', 'cam', 'maam']
list_1.extend(list_2)
print(list_1)
# ['cat', 'rat', 'bat', 'mat', 'pat', 'ham', 'cam', 'maam']

-----------------------------
list_1 = ['cat', 'rat', 'bat', 'mat', 'pat']
llist_2 = [2, 5, 6, 9, 10, 77]

list_1.pop() # by default it will pop last item
list_1.remove('cat') # will remove cat from the list
list_1.reverse() # will reverse the list
list_1.sort() # will short alphabatically
list_1.sort(reverse = True) # will sort in reverse order
print(min(list_2)) # will print 2
print(sum(list_2)) # 109

print(list_1.index('bat')) # 2
print('NotInList' in list_1) # False

for index, animal in enumerate(list_1, start=1):
	print(index, animal)
# prnts
# 1 cat
# 2 rat 
# 3 bat
# 4 mat
# 5 pat


list_1 = ['cat', 'rat', 'bat', 'mat', 'pat']
list_1_srt = ' - '.join(list_1)
print(list_1_srt)
# cat - rat - bat - mat - pat
new_list_1 = list_1_srt.split(' - ')
print(new_list_1)
# ['cat', 'rat', 'bat', 'mat', 'pat']

-------------------------------
Tuples ( )
--------------------------------
# Tuples are immutable, they can't be modified
# We can use tuples for looping through them but can't modify them
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)
# Traceback (most recent call last):
#   File "test.py", line 7, in <module>
#     tuple_1[0] = 'Art'
# TypeError: 'tuple' object does not support item assignment
-------------------------------
Sets { }
-------------------------------
# Sets don't allow duplicates

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

print(cs_courses)
# {'Math', 'History', 'CompSci', 'Physics'}

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math', 'CompSci', 'History'}
print(cs_courses)
# {'Math', 'Physics', 'CompSci', 'History'}

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = { 'History', 'Art', 'Bio', 'CompSci'}
print(cs_courses.intersection(art_courses))
# {'CompSci', 'History'}
print(cs_courses.difference(art_courses))
# {'Physics', 'Math'}
print(cs_courses.union(art_courses))
# {'Math', 'Bio', 'Physics', 'CompSci', 'Art', 'History'}

---------------------------------
Creating empty list, set, tuple
----------------------------------
# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict (dictionary) , hence this is not an empty set
empty_set = set() # correct empty set



#############################################################
Dictionaries - Working with Key-Value Pairs
#############################################################

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

for key, value in student.items():
    print(key, value)

# name John
# age 25
# courses ['Math', 'CompSci']
rint(student.keys()) 
# dict_keys(['name', 'age', 'courses'])
print(student.values())
# dict_values(['John', 25, ['Math', 'CompSci']])
print(student.items()) 
# dict_items([('name', 'John'), ('age', 25), ('courses', ['Math', 'CompSci'])])


--------
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student.get('ThisKeyIsNotInTheDict', 'Not found')) # if second arg is not given(i.e. Not found,) then it will print none
# Not found
--------------------
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

student['name'] = 'Akash'
print(student)
# {'name': 'Akash', 'age': 25, 'courses': ['Math', 'CompSci']}
-------------------
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

student.update({'name': 'Akash', 'age': 22, 'phone': 2252-5586})
print(student)
# {'name': 'Akash', 'age': 22, 'courses': ['Math', 'CompSci'], 'phone': -3334}
--------------------
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
age = student.pop('name')
del student['age']
print(student)
# {'courses': ['Math', 'CompSci']}
print(age)
# 25

#############################################################
Conditionals and Booleans - If, Else, and Elif Statements
#############################################################
# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

# for concatination of conditions
	# and (All conditions true)
	# or (any of the conditions true)
	# not (reverse condition)
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
	print('Welcome admin')
else:
	print('Not logged_in')
# Welcome admin

-------------------------------
a = [1,2,3]
b = [1,2,3]
print(a == b) # True
print(a is b) # False, because the "is" operator checks the id of memory location of the variable, which is not same in this case
print(id(a))
# 140224571356168
print(id(b))
# 140224571358088


#############################################################
 Loops and Iterations - For/While Loops
 ############################################################
------------------
break
-------------------
 nums = [1,3,7,5,6]

for num in nums:
	if num == 7:
		print('Found')
		break
	print(num)
# 1
# 3
# Found
---------------
continue
-------------
nums = [1,3,7,5,6]

for num in nums:
	if num == 7:
		print('Found')
		continue
	print(num)
# 1
# 3
# Found
# 5
# 6
--------
for i in range(1, 11):
	print(i)
# prints 1 to 10 digits
-------------------

i = 0

while True:
	if i == 3:
		break
	print(i)
	i += 1
# 0
# 1
# 2

#############################################################
Functions
 ############################################################

def hello_fun(greeting):
	return '{} Function'.format(greeting)

print(hello_fun('Hi'))
# Hi Function
-------------------
def student_info(*args, **kwargs):
	print(args)
	print(kwargs)

courses = ['math', 'Science']
info = {'name': 'Akash', 'age': 55}

student_info(*courses, **info)
# ('math', 'Science')
# {'name': 'Akash', 'age': 55}
--------------------
# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2017, 2))
# 28

