############### Our Blackjack House Rules #####################
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo

# start the game
print(logo)

choice = input("Do you want to play a game of Blackjack? Type 'y' for yes and 'n' for no:")
if choice != "y":
    print("See you when you're ready!")
    quit()
# our cards for the game
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# deal players with two random cards
user_cards = [random.choice(cards), random.choice(cards)]
computer_cards = [random.choice(cards), random.choice(cards)]


# we have a blackjack function for the entire game
def blackjack():
    # get sum
    def calculate_sum(cards_picked):
        total = sum(cards_picked)
        return total

    # to print the final scores of players after a round
    def final_score():
        print(f"Your final hand: {user_cards}, final score : {user_total}")
        print(f"Computer's final hand is {computer_cards}, final score : {computer_total}")

    user_total = calculate_sum(user_cards)
    computer_total = calculate_sum(computer_cards)
    print(f"Your cards: {user_cards}, score : {user_total}")
    print(f"Computer's first hand is {computer_cards[0]}")  # we only show the dealer's first hand in the game
    if computer_cards == [11, 10]:
        final_score()
        print("You lose, opponent won with a blackjack")
    elif user_cards == [11, 10]:
        final_score()
        print("You win with a blackjack !")
    elif user_total == 21:
        final_score()
        print("You win!")
    elif user_total > 21:
        if 11 not in user_cards:
            final_score()
            print("You lose, you went overboard")
        else:  # replace ace with 1 to see if they'll be over 21
            ace = user_cards.index(11)
            user_cards[ace] = 1
            user_total = calculate_sum(user_cards)
            if user_total > 21:
                final_score()
                print("You went over, you lose")
            else:
                print("=" * 50)
                print("Your ace was replaced ")
                print("=" * 50)
                blackjack()
    else:
        user_play = input("Do you want to draw another card? type 'y' for yes and 'n' otherwise: ")
        if user_play == "y":
            user_cards.append(random.choice(cards))
            blackjack()
        else:
            while computer_total < 17:
                computer_cards.append(random.choice(cards))
                computer_total = calculate_sum(computer_cards)
            if computer_total > 21:
                final_score()
                print("You win! Opponent went over ")
            elif user_total < computer_total:
                final_score()
                print("You lose")
            elif user_total > computer_total:
                final_score()
                print("You win ")
            elif user_total == computer_total:
                final_score()
                print("You draw")


blackjack()
