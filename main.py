import blackjack_funcs as bf

# Score count
wins = 0

# Play more games
continue_game = True

while continue_game:
    # Initializing to start game
    dealer_hand = bf.card_hand()
    shown_dealer_hand = (dealer_hand[0], 'X')
    player_hand = bf.card_hand()

    dealer_total = bf.card_counting(dealer_hand)
    player_total = bf.card_counting(player_hand)

    # Initial check for 21
    if dealer_total == 21:
        print("Game over!\nDealer has 21!")
        print("Dealer hand:")
        print(dealer_hand)
        print("Your hand:")
        print(player_hand)

    elif player_total == 21:
        print("You win!\nYou got 21!")
        print("Dealer hand:")
        print(dealer_hand)
        print("Your hand:")
        print(player_hand)
        wins += 1

    # No 21 in initial hands
    else:
        print("Dealer's hand:")
        print(shown_dealer_hand)
        print("\nYour hand:")
        print(player_hand)
        player_stay = False

        # Check if player wants more cards
        while player_total < 21 and player_stay is False:
            print("\nWill you hit or stay")
            player_decision = input("Type h to hit or s to stay: ").lower()
            if player_decision == 'h':
                player_hand = bf.add_card(player_hand)
                player_total = bf.card_counting(player_hand)
                print(player_hand)
            else:
                player_stay = True

        # Check if player won with 21
        if player_total == 21:
            print("You win!\nYou got 21!")
            print("Dealer hand:")
            print(dealer_hand)
            print("Your hand:")
            print(player_hand)
            wins += 1

        # Check if player busted
        elif player_total > 21:
            print("Busted!\nYou went over 21!")
            print("Dealer hand:")
            print(dealer_hand)
            print("Your hand:")
            print(player_hand)

        # Dealer getting more cards
        else:
            while dealer_total < 18:
                print("\nDealer hits.")
                dealer_hand = bf.add_card(dealer_hand)
                dealer_total = bf.card_counting(dealer_hand)
                print(dealer_hand)

            if dealer_total == 21:
                print("Dealer got blackjack!\nYou lost!")
                print("Dealer hand:")
                print(dealer_hand)
                print("Your hand:")
                print(player_hand)

            elif dealer_total >= 21:
                print("Dealer busted!\nYou win!")
                print("Dealer hand:")
                print(dealer_hand)
                print("Your hand:")
                print(player_hand)
                wins += 1

            else:
                if dealer_total > player_total:
                    print("You lost!")
                    print("Dealer hand:")
                    print(dealer_hand)
                    print("Your hand:")
                    print(player_hand)

                elif dealer_total < player_total:
                    print("You win!")
                    print("Dealer hand:")
                    print(dealer_hand)
                    print("Your hand:")
                    print(player_hand)
                    wins += 1

                else:
                    print("It's a tie!")
                    print("Dealer hand:")
                    print(dealer_hand)
                    print("Your hand:")
                    print(player_hand)

    continue_question = input("Play another game?\ny for yes, n for no: ").lower()
    if continue_question != "y" and continue_question != "yes":
        continue_game = False

print("\nThank you for playing.")
print(f"You won a total of {wins} times.")
print("Hope to sca.. I mean, play you again soon. Bye.")