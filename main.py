 
from art import logo, vs
from game_data import data
import random
print(logo)

score = 0

game_should_continue = True

account_b = random.choice(data)

while game_should_continue:
    """we want the game to repeat its self. The code below all needs to 
    be repeated"""

    def format_data(account):# take in an account parameter
        """takes the account data and returns printable format"""
        account_name = account["name"]
        account_descr = account["description"]
        account_country = account["country"]
        return f"{account_name}, a {account_descr}, from {account_country}"

    def check_answer(user_guess,a_followers,b_followers):
        """take the users guess and the follower accounts of a and b
        and return if they got it right"""
        if a_followers > b_followers:
            return user_guess == "a"
        else:
            return user_guess == "b"

    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:# making sure they don't have the same choice
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers A or B:").lower()

    #clear the screen
    print("\n" * 20)
    print(logo)

    a_follower_acc = account_a["follower_count"]
    b_follower_acc = account_b["follower_count"]

    is_correct = check_answer(guess,a_follower_acc,b_follower_acc)

    if is_correct:
        score += 1
        print(f"You are right!!!, Current score:{score}")
    else:
        print(f"Sorry you are wrong😑, your final score:{score}")
        game_should_continue = False


        
    