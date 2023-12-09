#  What is the diffrence between Break, continue and pass. 

# Break:- We use break to stop task when we achive our goals.
# continue :- it help to skip, what we want to skip then we use Continue statements.
# pass :-  we declare some logic but we don't want to complete that then their we need pass statements.

  

# ************************************  break ***************************************
for i in range(1, 10):
    if i == 5:
        break
    print("Hello")
# Expected OUTPUT: 
# Hello
# Hello
# Hello
# Hello

# *************************************  continue  **************************************
for k in range(1, 11):
    if k == 7:
        continue
    print("yes No -", k )
# Expected OUTPUT: 
# yes No - 1
# yes No - 2
# yes No - 3
# yes No - 4
# yes No - 5
# yes No - 6
# yes No - 8
# yes No - 9
# yes No - 10


# **************************************  pass   *****************************************

for i in range(1, 10):
    pass
