import random

#Snake Water Gun Game

def gameWin(comp, you):

    if comp == you:
        return None
    
    #when computer chose s
    elif comp == 's':
        if you == 'p': #snake drinks water so you lose
            return False
        elif you == 'r': #gun kills the snake so you win
            return True
        
    #when computer chose w
    elif comp == 'p':
        if you == 'r': #gun drowns in water so you lose
            return False
        elif you == 's': #snake drinks water so you win
            return True
    
    #when computer chose g
    elif comp == 'r':
        if you == 's': #gun kills the snake so you lose
            return False
        elif you == 'p': #gun drowns in water so you win
            return True

print("Computer Turn: Scissor(s) Paper(p) Rock(r)?")
randNo = random.randint(1, 3) #random number from 1-3 is generated  
# print(randNo)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 'r'

you = input("Your Turn: Scissor(s) Paper(p) Rock(r)?\n")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The Game Is A Tie")
elif a:
    print("You Win!")
else:
    print("You Lose!")
