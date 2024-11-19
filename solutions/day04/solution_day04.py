import re

def winning_numbers(card):
    _, both_nums = re.split(r':\s+', card)

    winning, current = re.split("\s+\|\s+", both_nums)
    winning = list(map(int, re.split(r'\s+', winning)))
    current = list(map(int, re.split(r'\s+', current)))
    # return count of current that are on a list of winning
    return len([number for number in current if number in winning])

def card_value(card):
    number_of_winning = winning_numbers(card)
    if number_of_winning > 0:
        return 2 ** (number_of_winning - 1)
    else:
        return 0


def sum_card_values(cards):
    return sum([card_value(card) for card in cards])


def sum_cards(cards):
    card_amounts = [1] * len(cards)
    for i in range(len(cards)):
        won_cards = winning_numbers(cards[i])
        current_card_amount = card_amounts[i]
        for k in range(i, i+won_cards):
            card_amounts[k+1] = card_amounts[k+1] + current_card_amount

    return sum(card_amounts)
