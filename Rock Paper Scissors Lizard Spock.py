import random;

print("Welcome to paper rock scissors lizard spock.")

user_threw = input("What're ya gonna throw? ")

if (user_threw == "rock"):
    print(user_threw + "! That's a rock!")
elif (user_threw == "paper"):
    print(user_threw + "! That's a paper!")
elif (user_threw == "scissors"):
    print(user_threw + "! That's scissors!")
elif (user_threw == "lizard"):
    print(user_threw + "! That's lizard!")
elif (user_threw == "spock"):
    print(user_threw + "! That's spock!")
else:
    print("You suck...")

computer_threw = random.choices(["rock","paper","scissors","lizard","spock"])[0]

if (user_threw == computer_threw):
    print("It's a tie!")
elif (user_threw == "paper" and (computer_threw == "rock" or computer_threw == "spock")):
    print("Computer threw " + computer_threw + "! You win!")
elif (user_threw == "rock" and (computer_threw == "scissors" or computer_threw == "lizard")):
    print("Computer threw " + computer_threw + "! You win!")
elif (user_threw == "scissors" and (computer_threw == "paper" or computer_threw == "lizard")):
    print("Computer threw " + computer_threw + "! You win!")
elif (user_threw == "lizard" and (computer_threw == "spock" or computer_threw == "paper")):
    print("Computer threw " + computer_threw + "! You win!")
elif (user_threw == "spock" and (computer_threw == "scissors" or computer_threw == "rock")):
    print("Computer threw " + computer_threw + "! You win!")
else:
    print("Computer threw " + computer_threw + "! You lose!")

print("Thank you for playing paper rock scissors lizard spock!")

