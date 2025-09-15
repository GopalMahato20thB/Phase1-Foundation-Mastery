import random

"""
## Working with random module

#print(random.random()) # Random float: 0.0 <= x <= 1.0

#print(random.uniform(1.0, 5.0)) # Random float: 1.0 <= x <= 5.0

#print(random.expovariate(1/5)) # Interval between aarrivals averaging 5 seconds

#print(random.randrange(10)) # Integer from 0 to 9 inclusive

#print("You ", random.choice(["win", "lose", "draw"]))

deck = 'ace two three four'.split()
random.shuffle(deck) # Shuffle a list
print(deck)

"""

coin = random.choice(["heads", "tails"])

user_dict = {"heads": "h", "tails": "t"}

user_choice =  input("Enter option(h/t): ")


if user_dict[coin] == user_choice:
    print("You won the toss!")
else:
    print("You lost the toss!")



