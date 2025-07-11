import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)

def dealer():
      
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare(user_score, comp_score):
    if user_score == comp_score:
        return "Draw "
    elif comp_score == 0:
        return "Computer has Blackjack. You lose "
    elif user_score == 0:
        return "You have Blackjack! You win "
    elif user_score > 21:
        return "You went over. You lose "
    elif comp_score > 21:
        return "Computer went over. You win "
    elif user_score > comp_score:
        return "You win "
    else:
        return "You lose "
    
def start_game():
    user_cards = []
    comp_cards = []

    for _ in range(2):
        user_cards.append(dealer())
        comp_cards.append(dealer())

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21 or comp_score>21:
            game_over = True
        else:
            draw = input("Type 'y' to draw another card, 'n' to pass: ").lower()
            if draw == 'y':
                user_cards.append(dealer())
            else:
                game_over = True


    while calculate_score(comp_cards) < 17:
        comp_cards.append(dealer())

    final_user_score = calculate_score(user_cards)
    final_comp_score = calculate_score(comp_cards)

    print(f"\nYour final hand: {user_cards}, final score: {final_user_score}")
    print(f"Computer's final hand: {comp_cards}, final score: {final_comp_score}")
    print(compare(final_user_score, final_comp_score))

start_game()
