import random

cards = ('S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'SA')
card_values = {
    'S2': 2, 'S3': 3, 'S4': 4, 'S5': 5, 'S6': 6,
    'S7': 7, 'S8': 8, 'S9': 9, 'S10': 10,
    'SJ': 11, 'SQ': 12, 'SK': 13, 'SA': 14
}


# generates 6 random cards from cards tuple
def get_card_draw(tuple_name: tuple):
    new_hand = random.choices(tuple_name, k=6)
    return new_hand


# generates 'left_hand' as first 3 cards of new_hand
def get_left_hand(some_list):
    left_hand = some_list[:3]
    return left_hand


# generates 'right_hand' from last 3 cards of new_hand
def get_right_hand(some_list):
    right_hand = some_list[3:]
    return right_hand


# Uses card_values dict to assign values to cards in player's hands
def get_card_values(player_cards):
    hand_values = [card_values[x] for x in player_cards]
    return hand_values


def check_straight(some_list: list):
    if sorted(some_list) == list(range(min(some_list), max(some_list)+1)):
        player_score = max(some_list)
        return player_score
    else:
        player_score = 0
        return player_score


def check_3ofa_kind(some_list: list) -> int:
    if all(i == some_list[0] for i in some_list):
        player_score = some_list[0]
        return player_score
    else:
        player_score = 0
        return player_score


def check_royal_flush(score: int) -> int:
    if score == 14:
        return True
    else:
        return False


# Runs through all game checks to determine the player's total score
def play_cards(some_list):
    final_score = check_straight(some_list)
    if check_royal_flush(final_score):
        player_final_score = 14
        return player_final_score
    elif final_score > 0:
        player_final_score = final_score
        return player_final_score
    else:
        player_final_score = check_3ofa_kind(some_list)
        return player_final_score


# Compares total scores from left and right player to determine winner
def determine_winner(left_score, right_score):
    if left_score > right_score:
        end_game_total = -1
        print(f'Left player wins: {end_game_total}')
    elif left_score < right_score:
        end_game_total = 1
        print(f'Right player wins: {end_game_total}')
    else:
        print('The game was a tie: 0')


def main():
    new_draw = get_card_draw(cards)
    left_cards = get_left_hand(new_draw)
    right_cards = get_right_hand(new_draw)
    left_values = get_card_values(left_cards)
    right_values = get_card_values(right_cards)
    print(f'The cards drawn for this game are: {new_draw}')
    print(f"The left player's cards are: {left_cards}")
    print(f"The right player's cards are: {right_cards}")
    left_player_turn = play_cards(left_values)
    right_player_turn = play_cards(right_values)
    determine_winner(left_player_turn, right_player_turn)


if __name__ == '__main__':
    main()

