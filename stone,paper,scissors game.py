import random

def game(computer,you):
    if computer==you:
        return None
    elif computer=="s":
         if you=="c":
            return False
         elif you=="p":
            return True
    elif computer=="p":
         if you=="s":
            return False
         elif you=="c":
            return True
    elif computer=="c":
         if you=="p":
            return False
         elif you=="s":
            return True
    
        
print('computer turn:stone(s),paper(p)or scissors(c)?')
randno=random.randint(1,3)
if randno==1:
    computer="s"
elif randno==2:
    computer="p"
else:
    computer="c"
                    

you=input("player's turn:stone(s),paper(p)or scissors(c)?")
a=game(computer,you)
print(f'computer choose:{computer}')
print(f'you choose:{you}')

if a==None:
    print('game tied')
elif a:
    print('you won')
else:
    print("you lose")