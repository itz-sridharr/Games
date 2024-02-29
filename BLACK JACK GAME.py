########### BLACK JACK GAME ###########

import random

def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card



def compare(user_score,computer_score):
    """To compare the score between computer and the user"""
    if user_score==computer_score:
        return "Draw"
    elif computer_score==0:
        return "Lose, opponent has BlackJack"
    elif user_score==0:
        return "Win with a BlackJack"
    elif user_score>21:
        return " You went over. You lose"
    elif computer_score>21:
        return "Opponent went over, you won"
    elif user_score>computer_score:
        return " You win"
    else:
        return " You lose"

def calculate_score(cards):
    """Take a list of cards and return the score."""
    if sum(cards)==21 and len(cards)==2:
        return 0
    
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
                
    return sum(cards)
# def playgame():
#     user_card=[]
#     computer_card=[]
#     is_game_over=False

#     for _ in range(2):
#         user_card.append(deal_card())
#         computer_card.append(deal_card())
#     while not is_game_over:  
#         user_score=calculate_score(user_card)
#         computer_score=calculate_score(computer_card)
#         print(f" Yours cards:{user_card},current score:{user_score}") 
#         print(f" Computer's first card:{computer_card[0]}")   
#         if user_score==0 or computer_score==0 or user_score>21:
#             is_game_over=True
#         else:
#             user_should_deal=input("Type 'y' to get another card ,type 'n' to pass :")

#             if user_should_deal=="y":
#                 user_card.append(deal_card())
#             else:
#                 is_game_over=True
            
#     while computer_score!=0 and computer_score>17:
#         computer_card.append(deal_card())
#         computer_score=calculate_score(computer_card)
        
#     print(f"Your final hand{user_card}, final score:{user_score}")  
#     print(f"Computer final hand{computer_card}, computer final score:{computer_score}") 
#     print(compare(user_score,computer_score))

# while input("Do you want to play a game of BlackJack? Type 'y' for yes or 'n' for no :\n")=="y":
#     playgame()

user_card=[]
computer_card=[]
is_game_over=False

for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())
while not is_game_over:  
    user_score=calculate_score(user_card)
    computer_score=calculate_score(computer_card)
    print(f" Yours cards:{user_card},current score:{user_score}") 
    print(f" Computer's first card:{computer_card[0]}")   
    if user_score==0 or computer_score==0 or user_score>21:
        is_game_over=True
    else:
        user_should_deal=input("Type 'y' to get another card ,type 'n' to pass :")

        if user_should_deal=="y":
                user_card.append(deal_card())
        else:
                is_game_over=True
            
while computer_score!=0 and computer_score>17:
    computer_card.append(deal_card())
    computer_score=calculate_score(computer_card)
        
print(f"Your final hand{user_card}, final score:{user_score}")  
print(f"Computer final hand{computer_card}, computer final score:{computer_score}") 
print(compare(user_score,computer_score))
    

         
