print("Welcome to my computer quiz!")

user_choice = input("Do you want to play (y/n)? ").lower()
if user_choice != "y":
    quit()

print("Okay, let's play!\n")

score = 0  # keep track of correct answers

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input("Who invented the telephone? ").lower()
if answer in ["alexander graham bell", "alexander", "mr bell", "graham bell"]:
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input("Which festival is known as the Festival of Lights? ").lower()
if answer == "diwali":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input("Who is known as the Missile Man of India? ").lower()
if answer in ["dr. apj abdul kalam", "apj abdul kalam", "abdul kalam"]:
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input("What is the largest desert in the world? ").lower()
if answer in ["sahara", "sahara desert", "the sahara desert"]:
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

print(f"\nYou got {score} out of 5 correct!")
