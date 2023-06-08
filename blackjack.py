import random


# Returns random card from Cards, Deals card.
def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Checks if either user or dealer has an ace in their cards and if does it returns 0 which means the dealer or user wins
# Second if checks if the user or dealer has an ace but if their sum is greater than 21 than the ace becomes = 1 instead
# of 11. Check for ace.


def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# Check who wins, compares the sum of both the user and dealer. Check for every possibility that the user or dealer can
# win from.


def compare(user_score, dealers_score):
    if user_score == dealers_score:
        print("Draw")
    elif dealers_score == 0:
        print("You lose, dealer wins with Blackjack!")
    elif user_score == 0:
        print("You win with Blackjack")
    elif user_score > 21:
        print("You lose, you went over 21.")
    elif dealers_score > 21:
        print("You win, dealer went over 21.")
    elif user_score > dealers_score:
        print("You win")
    else:
        return "You lose"


def play_game():  # Have one function that we can put all the code on to start the "game".
    user_cards = []
    dealer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        dealer_cards.append(deal_cards())

    while not game_over:
        user_score = calculate_score(user_cards)
        dealers_score = calculate_score(dealer_cards)

        print(f"Your cards: {user_cards}\n")
        print(f"Dealers first card: {dealer_cards[0]}\n")

        if user_score == 0 or dealers_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'Y' to get another card, type 'N' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_cards())
            else:
                game_over = True

    while dealers_score != 0 and dealers_score < 17:
        dealer_cards.append(deal_cards())
        dealers_score = calculate_score(dealer_cards)

    compare(user_score, dealers_score)


while input("Do you want to play a game of Blackjack? Type 'y': ") == 'y':
    play_game()

