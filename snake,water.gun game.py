
import random

def game(computer,you):
    if computer==you:
        return None
    elif computer=="s":
         if you=="w":
            return False
         elif you=="g":
            return True
    elif computer=="w":
         if you=="g":
            return False
         elif you=="s":
            return True
    elif computer=="g":
         if you=="s":
            return False
         elif you=="w":
            return True
    
        
print('computer turn:snake(s),water(w)or gun(g)?')
randno=random.randint(1,3)
if randno==1:
    computer="s"
elif randno==2:
    computer="w"
else:
    computer="g"
                    

you=input("player's turn:snake(s),water(w)or gun(g)?")
a=game(computer,you)
print(f'computer choose:{computer}')
print(f'you choose:{you}')

if a==None:
    print('game tied')
elif a:
    print('you won')
else:
    print("you lose")