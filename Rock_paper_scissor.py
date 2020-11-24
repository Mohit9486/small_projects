from random import randint

print("Welcome to game")
user = input("Hey what's your name: ")
user.capitalize()

#Game Rules
print("Game Rules:")
print("There will be 5 rounds")
print("Paper beats Rock")
print("Rock beats scissor")
print("Scissor beats paper")
print("Winner will get 10 points for each round")

#Game Design
sample = ["rock","paper","scissor"]
user_score = 0
comp_score = 0

i = 1;
while i<=5:
    choice = randint(0,2)
    print("Round : ",i)
    comp = sample[choice]
    user_entry = input(f"Hey {user}, enter one of rock,paper,scissor : ")
    user_entry.lower()
    print(f"computer chois is {comp}")
    if (user_entry=="rock" and comp=="scissor") or (user_entry=="paper" and comp=="rock") or (user_entry=="scissor" and comp=="paper"):
        print(f"congrats {user}, you get 10 points.")
        user_score+=10
    elif (comp=="rock" and user_entry=="scissor") or (comp=="paper" and user_entry=="rock") or (comp == "scissor" and user_entry=="paper"):
        print("OOPS! computer gets 10 points.")
        comp_score+=10
    elif user_entry==comp:
        print("No one get points.")
    i+=1
# winner
print(f"{user} : {user_score}")
print(f"Computer : {comp_score}")

if user_score>comp_score:
    print(f"Congrats {user}, You won.")
elif user_score<comp_score:
    print('OOps computer won, try AGAIN!!')
else:
    print('GAME TIED, NICE TRY.')