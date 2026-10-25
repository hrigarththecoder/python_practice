import random
computer=random.choice([-1,0,1])
user=input("enter ur choice(r/p/s): ")

dic={
    "r":1,
    "p":0,
    "s":-1
}

reverse={
    -1:"scissor",
    0:"paper",
    1:"rock"
}

user_choice=dic[user]
print("you chose",reverse[user_choice],"And computer chose",reverse[computer])

if user_choice==1 and computer==0:
    print("YOU LOST")
elif user_choice==1 and computer==-1:
    print("YOU WON")
elif user_choice==-1 and computer==0:
    print("YOU won")
elif user_choice==-1 and computer==1:
    print("YOU lost")
elif user_choice==0 and computer==1:
    print("YOU WON")
elif user==0 and computer==-1:
    print("YOU LOST")
elif user_choice==computer:
    print("tied")