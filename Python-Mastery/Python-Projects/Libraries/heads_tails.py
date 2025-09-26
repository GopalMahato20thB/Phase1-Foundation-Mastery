from random import choice

coin = choice(["heads", "tails"])

user_dict = {"heads": "h", "tails": "t"}

user_choice =  input("Enter option(h/t): ")


if user_dict[coin] == user_choice:
    print("You won the toss!")
else:
    print("You lost the toss!")
