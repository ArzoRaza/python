# nested Loop is actually loop in for loop 

# let's see example 

for i in range(1, 5):
    for j in range(0, i):
        print("*", end=" ")
    print(" ")
