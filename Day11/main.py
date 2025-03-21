import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    """"Function to draw random card from cards deck"""
    return random.choice(cards)

def calculate_score(hand):
    """Function to calculate score"""
    if sum(hand) == 21 and len(hand) == 2:
        return 0

    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)

def blackjack_game():
    """Function how to play blackjack game"""
    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]

    game_over = False

    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        if player_score == 0:
            print("Blackjack! You win!")
            return
        elif player_score > 21:
            print("You went over 21. You lose!")
            return

        should_continue = input("Type 'y' to draw another card, type 'n' to pass: ").lower()
        if should_continue == 'y':
            player_hand.append(draw_card())
        else:
            game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(draw_card())
        dealer_score = calculate_score(dealer_hand)

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")

    if dealer_score > 21:
        print("Dealer went over 21. You win!😎")
    elif dealer_score == 0:
        print("Dealer has Blackjack! You lose.😢")
    elif player_score > dealer_score:
        print("You win!🥳")
    elif player_score < dealer_score:
        print("You lose!😖😖")
    else:
        print("It's a draw!😒")


def play_blackjack():
    stop_game = False
    while not stop_game:
        continue_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if continue_play == 'y':
            print(art.logo)
            blackjack_game()
        else:
            stop_game = True


play_blackjack()
