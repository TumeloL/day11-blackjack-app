import sys     # PROVIDES SYSTEM-SPECIFIC FUNCTIONS (E.G., SYS.EXIT() TO SAFELY QUIT THE PROGRAM)
import random  # ALLOWS RANDOM SELECTION OF CARDS FROM THE DECK
from blackjack_logo import blackjack_art  # IMPORTS THE ASCII ART LOGO FOR THE BLACKJACK GAME TITLE
def main():
    print(blackjack_art)
    main_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user = []
    dealer = []

    def deal_initial_cards():
        for _ in range(2):
            user.append(random.choice(main_deck))
            dealer.append(random.choice(main_deck))
        print(f"You: {user}")
        print(f"Dealer: [{dealer[0]}, ?]")  # HIDE ONE DEALER CARD 
        print("-" * 30)

    def calculate_score(hand):
        # CHANGE ACE (11) TO 1 IF OVEER 21
        while sum(hand) > 21 and 11 in hand:
            hand[hand.index(11)] = 1
        return sum(hand)

    def player_turn():
        while True:
            print(f"\nYour current hand: {user} | Total: {calculate_score(user)}")
            hit_or_stand = input("Do you want another card? Y/N\n").strip().lower()

            if hit_or_stand in ["n", "no"]:
                # DEALER DRAWS UNTIL 17 OR HIGHER
                while calculate_score(dealer) < 17:
                    dealer.append(random.choice(main_deck))
                break

            elif hit_or_stand in ["y", "yes"]:
                user.append(random.choice(main_deck))
                if calculate_score(user) > 21:
                    print(f"\nYour hand: {user} | Total: {calculate_score(user)}")
                    print(f"Dealer's hand: {dealer} | Total: {calculate_score(dealer)}")
                    print("Bust! You went over 21.")
                    break

            else:
                print("Please enter Y or N only.")
        
        print("-" * 30)

    def final_result():
        total_user = calculate_score(user)
        total_dealer = calculate_score(dealer)
        print(f"\nYour final hand: {user}, total = {total_user}")
        print(f"Dealer's final hand: {dealer}, total = {total_dealer}")
        print("-" * 30)

        if total_user > 21 and total_dealer <= 21:
            print("BUST! YOU LOSE!")
        elif total_dealer > 21 and total_user <= 21:
            print("DEALER BUST, YOU WIN!")
        elif total_user > total_dealer and total_user <= 21:
            print("You win!")
        elif total_dealer > total_user and total_dealer <= 21:
            print("Dealer wins!")
        else:
            print("DRAW!")

    def restart_game(): 
        while True:
            play_again = input("DO YOU WANT TO PLAY AGAIN?\n").strip().lower()
            if play_again in ["n", "no"]: 
                print("THANK YOU FOR PLAYING BLACKJACK!!")
                sys.exit() # THIS CLEANLY STOPS THE ENTIRE PROGRAM
            elif play_again in ["y", "yes"]:
                main()
                break
            else:
             print("Please enter Y or N only.")

    # ALL THESE FUNCTION CALLS PLAYS THE GAME IN THE CORRECT SEQUENCE 
    deal_initial_cards()
    player_turn()
    final_result()
    restart_game()
 
if __name__ == "__main__":
    main()
