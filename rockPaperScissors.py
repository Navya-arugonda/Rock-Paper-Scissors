import random
import enum

class Choice(enum.Enum):
    Rock=1
    Paper=2
    Scissors=3

def userVsComp():
    ch='y'
    while(ch=='y'):
        targetScore=int(input("Enter the target score:"))
        user=comp=0
        
        while(user!=targetScore and comp!=targetScore):
            print("1.Rock\n2.Paper\n3.Scissors")
            userChoice=int(input("Enter your choice:"))
            if(userChoice<1 or userChoice>3):
                print('Enter valid choice!!\n')
                continue
            compChoice=random.randint(1,3)
            print('\nUser selected ',Choice(userChoice).name)
            print('Computer selected ',Choice(compChoice).name,'\n')
            if((userChoice==1 and compChoice==1) or (userChoice==2 and compChoice==2) or (userChoice==3 and compChoice==3)):
                print('User and computer selected same choice\n')
                continue
            elif(userChoice==1 and compChoice==2):
                comp+=1
                print('Computer scored\n')
            elif(userChoice==1 and compChoice==3):
                user+=1
                print('User scored\n')
            elif(userChoice==2 and compChoice==1):
                user+=1
                print('User scored\n')
            elif(userChoice==2 and compChoice==3):
                comp+=1
                print('Computer scored\n')
            elif(userChoice==3 and compChoice==1):
                comp+=1
                print('Computer scored\n')
            elif(userChoice==3 and compChoice==2):
                user+=1
                print('User scored\n')

        if(user==targetScore):
            print('User won the game\n')
        elif(comp==targetScore):
            print('Computer won the game\n')

        ch=input(('Do you want to continue(y/n)?'))

userVsComp()
    
    

