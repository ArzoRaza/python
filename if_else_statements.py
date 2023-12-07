# In this file we explore 'if else' statements 
# let's build some intrestiong things 


# Email : arzo@gmail.com
# password : 1234

Email = input("Enter your Email :")
if '@' in Email:
    password = input("Enter your Password :")

    if Email == "arzo@gmail.com" and password == "1234":
        print("Welcome")
    elif Email != "arzo@gmail.com" and password == "1234":
        print("tera Email glt hai")
        Email = input("Fir se Email dal : ")
        if Email == "arzo@gmail.com":
            print("Aa ja sajan")
        else:
            print("abhi bhi tera Email glt hai")
else:
    print("Tera Email glt hai :")
        

