# In this file we discouse about recursion 

def mul (a,b):
    if b==1:
        return a
    else:
        return a + mul(a,b-1)
# print(mul(3,4))

# Palindrom 

# def palin(text):
#     if len(text) == 1:
        # print("palindrome")
    # else:
        # if text[0] == text[-1]:
        #     palin(text[1:-1])
        # else:
#             print("Not Palin")
# palin("madam")
# palin("malayalam")
# palin("python")


#  Fibonaci Program 

# def fib(m):
#     if m==0 or m==1:
#         return 1
#     else:
#         return fib(m-1) + fib(m-2)
# print(fib(36))


# Memogaization 

import time
def memo(m,d):
    if m in d:
        return d[m]
    else:
        d[m] = memo(m-1,d)+ memo(m-2,d)
        return d[m]
start = time.time()
d = {0:1, 1:1}
print(memo(480,d))
print(time.time()-start)
print(d)
