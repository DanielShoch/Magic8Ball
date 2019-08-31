import random
import time

# List of potential answers the Magic 8 Ball will give
answersList = ["Definitely!", "Forget about it", "I'm not sure", "Yes!", "No!", "Ask again later.", "It is certain.", "Most likely.", "Probably not.", "Doubtful.", "You can rely on it.", "Without a doubt!", "My sources say no."]

# Welcome message
print("Welcome to Magic 8 Ball!")
time.sleep(1)

def magicEightBall():
    while True:
        
        # Receiving user question
        userQuestion = input("What is your question? \n")
        time.sleep(1)

        # Thematic pause
        print("Mmmmh... ")
        time.sleep(2)

        # Magic 8 Ball answer 
        print(random.choice(answersList))
        time.sleep(1)

        # Checking if user wants to ask another question
        continueGame = input("Would you like to ask another question? (y/n) \n")
        time.sleep(1)

        # Repeat function or break
        if continueGame == "y":
            continue
        else:
            break

magicEightBall()
