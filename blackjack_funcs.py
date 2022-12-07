import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def card_hand():
    hand = [int(random.choice(cards)), int(random.choice(cards))]
    return hand


def add_card(player_hand):
    player_hand.append(random.choice(cards))
    return player_hand



def card_counting(hand):
    # Get the total for the given hand
    card_total = 0
    for card in hand:
        card_total += card
    return card_total
