from game_data import data
from art import logo, vs
import random

# create a function for the game
def game():
    print(logo)
    from game_data import data
    data = data 

    # make a while loop to keep the game going till lives = 0
    lives = 1
    while lives == 1:
        a = random.choice(data)
        b = random.choice(data)

        
        print("Compare A: " + a['name'], ", from" ,a['country'], ", a" , a['description'])
        print(vs)
        print("Compare B: " + b['name'], ", from" ,b['country'], ", a" , b['description'])
    
        user = input('Who has more followers? Type "a" or "b"')
        if user == 'a' and a['follower_count'] > b['follower_count']:
            print("Thats Corrrect!")
        elif user == 'b' and b['follower_count'] > a['follower_count']:
            print("Thats Corrrect!")
        else:
            print("Sorry, that was not correct!")
            lives -= 1
    
game()