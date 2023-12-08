import random
jackpot = random.randint(1, 100)

guess = int(input("Guess the number :"))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print("Guess Higher")
    else:
        print("Guess Lower ")
    guess = int(input("fir se try kar :"))
    counter += 1

print("CORRECT & You take attempt", counter, "times ")