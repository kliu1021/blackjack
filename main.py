from art import logo
import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(list):
    if sum(list) == 21:
        return 0
    elif sum(list) > 21 and 11 in list:
        list.remove(11)
        list.append(1)
        return sum(list)
    else:
        return sum(list)


def compare(my_score, computer_score):
    if my_score > 21 and computer_score > 21:
        return 'You went over. You lose 😤'
    elif my_score == computer_score:
        return 'Draw 🙃'
    elif computer_score == 0:
        return 'Lose, opponent has Blackjack 😱'
    elif my_score == 0:
        return 'Win with a Blackjack 😎'
    elif my_score > 21:
        return 'You went over. You lose 😭'
    elif computer_score > 21:
        return 'Opponent went over. You win 😁'
    elif computer_score > my_score:
        return 'You lose 😤'
    else:
        return 'You win 😃'


def blackjack():
    print(logo)

    end_game = False

    my_cards = []
    computer_cards = []

    for x in range(2):
        my_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not end_game:
        my_score = calculate_score(my_cards)
        computer_score = calculate_score(computer_cards)
        print(f'    Your cards: {my_cards}, current score: {my_score}')
        print(f'    Computer\'s first cards: {computer_cards[0]} \n')

        if my_score == 0 or computer_score == 0:
            end_game = True
        elif my_score > 21 or computer_score > 21:
            end_game = True
        else:
            if input('Type \'y\' to get another card, type \'n\' to pass: ') == 'y':
                my_cards.append(deal_card())
            else:
                end_game = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f'    Your final hand: {my_cards}, final score: {my_score}')
    print(f'    Computer final hand: {computer_cards}, final score: {computer_score} \n')
    print(compare(my_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print('\nThe deck is unlimited in size.\n'
          'There are no jokers.\n'
          'The Jack/Queen/King all count as 10.\n'
          'The the Ace can count as 11 or 1.\n'
          'The cards in the list have equal probability of being drawn.\n'
          'Cards are not removed from the deck as they are drawn.\n'
          'The computer is the dealer.')
    blackjack()
