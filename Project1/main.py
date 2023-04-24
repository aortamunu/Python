import random

#Snake Water Gun Game

def gameWin(comp, you):

    if comp == you:
        return None
    
    #when computer chose s
    elif comp == 's':
        if you == 'w': #snake drinks water so you lose
            return False
        elif you == 'g': #gun kills the snake so you win
            return True
        
    #when computer chose w
    elif comp == 'w':
        if you == 'g': #gun drowns in water so you lose
            return False
        elif you == 's': #snake drinks water so you win
            return True
    
    #when computer chose g
    elif comp == 'g':
        if you == 's': #gun kills the snake so you lose
            return False
        elif you == 'w': #gun drowns in water so you win
            return True

print("Computer Turn: Snake(s) Water(w) Gun(g)?")
randNo = random.randint(1, 3) #random number from 1-3 is generated  
# print(randNo)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your Turn: Snake(s) Water(w) Gun(g)?\n")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The Game Is A Tie")
elif a:
    print("You Win!")
else:
    print("You Lose!")
