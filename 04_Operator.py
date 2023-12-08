# In this file we see about Operators, how many Operators have in python. 

''' 
We have generally several types of Operatos In python. 

1 Arithmetic Operatos 
2 Comparision Operatos 
3 Logical Operatos 
4 Bitwise Operatos 
5 Assignment Operatos
6 Identity Operatos 
7 membership Operatos 
'''



# *************************  1 Arithmetic Operatos *********************************
"""
addition Operators : + 
Subtraction Operatos : -
Multiplication Operators : *
Division Operators : /
Modulus Operators : % 
Exponentiation Operators : **
Floor Division Operators : // 
"""

x = 10
y = 5

print("Addition Operators (+) :", x + y)
#Expected OUTPUT : 15

print("Subtraction Operators (-) :", x - y)
#Expected OUTPUT : 5

print("multiplication Operatos (*) :", x * y)
#Expected OUTPUT : 50

print("Division Operators (/) :", x / y)
#Expected OUTPUT : 2.0

print("Modulus Operators (%) :", x % y)
#Expected OUTPUT : 0

print("Exponentiatio Operators (**) :", x ** y)
#Expected OUTPUT : 100000


print("Floor Division Operators (//) :", x // y)
#Expected OUTPUT : 2

# ****************************************  2 Comparision Operators ******************************************
"""
Equal to                 : == 
Not Equal to             : != 
Greater than             : >
Less than                : <
Greater than or Equal to : >= 
Less than or Equal to    : <=
"""


print("equal (==) :", x == y)
#Expected OUTPUT : False

print("not equal (!=) :", x != y)
#Expected OUTPUT : True

print("Greater than (>) :", x > y)
#Expected OUTPUT : True

print("Less than (<) : ", x < y)
#Expected OUTPUT : False

print("Greater then or equal to (>=) :", x >= y)
#Expected OUTPUT : True

print("Less than or equal to (<=) :", x <= y)
#Expected OUTPUT : False



# ***************************************** 3 Logical Operators ************************************
"""
or Operators : or 
and Operators : and
not Operators : not 
"""


x = True
y = False

print("Only One Value should have true :", x or y)
#Expected OUTPUT : True

print("boths values should have False :", x and y)
#Expected OUTPUT : False

print("Results come Reverse :", not y) # y is False
#Expected OUTPUT : True

print("Results come Reverse :", not x) # x is True
#Expected OUTPUT : False


# *******************************************  4 Bitwise Operators ********************************************

"""
These perform in binary form like 0 and 1
011
110
---
111

& - AND Operators
| - OR Operators 
^ - XOR Operators 
~ - NOT Operators 
<< - left shift Operators 
>> - right shift Operators 
"""

# These perform in binary form. like 0 and 1

a = 2
b = 3

print(a & b)
#Expected OUTPUT : 2

print(a | b)
#Expected OUTPUT : 3
 
print(a ^ b)
#Expected OUTPUT : 1

print(~ a )
#Expected OUTPUT : -3

print(a << b)
#Expected OUTPUT : 16

print(a >> b)
#Expected OUTPUT : 0

# **************************************** 5 Assignment Operators *********************************************
"""
= - assignment Operators 
+= 
-+
*=
/=
%=
**=
//=
&=
|=
^= 
<<=
>>= 

"""

h = "Arzo Raza"
print(h)
 

# ******************************************  6 Identity Operators ********************************************
"""
is - return True when two values are in same memory location 
is not - reverse above example  
"""

c = "Hello"
d = "Hello"
print(c is d)
#Expected OUTPUT : True

e = "Hello world"
f = "lanka kya hal chal mai aa gya hu tumse milne ab tera khair nhi "
print(e is f)
#Expected OUTPUT : False

g = "hello"
f = "Hello"
print(g is not f)
#Expected OUTPUT : True   because g and f boths values not have same location


# ******************************************  7  Membership Operators ******************************************
"""
in - it help to find value, what i want to find value in given value if have then results come True other wise False
not in - it also try to find what values not have in given value, if find then return False if not then return True
"""

z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(100 in z)
#Expected OUTPUT : False

print(500 not in z)
#Expected OUTPUT : True














 




