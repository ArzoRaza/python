# Let's start about SRTING. 

# in pyhon specifically, string are a sequence of unicode characters. 

'''we see string some popular steps

Creating string
Accessing string 
Adding chars to string 
Deleting string 
Operation on string 
String function 

'''

# **********************************  Creating string ********************************************
# we have 3 option to create string 
#  1 
a = 'Hello'
a = "Hello"
a = '''Hello'''
# print(a)

# *********************************  Accessing String ********************************************
# we have two types of indexing Option 
# positive Indexing:-  It's start from 1 
# Negative Indexing:- It's start from -1
# slicing 

b = "Arzo Raza"
# print(b[0])   # Positive string
# print(b[1])   # Positive string
# print(b[2])   # Positive string
# print(b[-1])  # Negative string 

#  ***************    slicing 

# print(b[0:5])
# Expected OUTPUT: 
# Arzo

# print(b[1 : 5 : 2])
# Exp OUTPUT: ro

# print(b[-4:-2])

# print(b[2: 9])

# print(b[::-1])

# print(b[:])

# print(b[1:9: 3])


# ************************************  Deletion on string ********************************

# string is immutable that reason we connot change string and also add chars in string 
# but we can delete intaire string. 



# *************************************  Operation on string **********************************
'''
Arithmetic Operators 
Relational Operators 
Logical Operators 
Loops on Operators 
membership Operators

'''

# Arithmetic Operators:- ( + , * )  only two arithmetic Operators for apply on string

c = "Hello" + "-" + "World"
# print(c)

# print((c)*5)
# Expected OUTPUT: Hello-WorldHello-WorldHello-WorldHello-WorldHello-World


# Relational Operators 
d = "punjab"
e = " bihar"

# print(d > e)
#Epx OUTPUT: True      because of Lexiographically, that come first in dictionary 1 and that come last that 100

f = "B" > "b"
# print(f)

# Loop in string 

g = "Hello Arzo"
# for i in g[::-1]:
    # print(i)


# Membership Operators

h = "Arzo Raza"
# print("k" in h) 
# Exp OUTPUT: False

# print("k" not in h)
# Exp OUTPUT: True


# **************************************  Function on string ****************************
"""
command function 

len 
max
min
sorted

"""

i = "arzo roshan vivek"
# print(len(i))     # OUTPUT: 9 
# print(max(i))     # OUTPUT: z
# print(min(i))     # OUTPUT: A
# print(sorted(i))  # OUTPUT: ['A', 'R', 'a', 'a', 'o', 'r', 'z', 'z']

# **********************************   Capitlize/title/Upper/Lower/Swapcase  ***********************
# Capitlize 

k = "lakjdf;ld"
# print(i.capitalize())
# print(i.title())
# print(i.upper())
# print(i.lower())
# print(k.swapcase()) 

# ************************************  count/find/index *****************************************************
# print(k.count("f"))  
# print(k.find("la"))  # 0
# print(k.index("d"))  # 4

# **************************************  formt  ****************************************

# print("Hey my friends I'm {name}. and I'm {age} years old".format(name="Arzo", age=20))
print("Hello my friends this is {1} and I'm a {0}".format("roshan", "Arzo"))


# ***************************************  replace ****************************************
l = " Hey my name is Arzo"
print(l.replace("Arzo", "Akbar"))

# ***************************************  strip ********************************************

name = "                            arzo                "
name += "akbar"
print(name.strip())