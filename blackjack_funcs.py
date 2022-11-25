import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def card_hand():
    hand = [random.choice(cards), random.choice(cards)]
    return hand


def add_card(player_hand):
    return player_hand.append(random.choice(cards))


def card_counting(hand):
    # Get the total for the given hand
    card_total = 0
    for card in hand:
        card_total += card
    print(card_total)
    return card_total
