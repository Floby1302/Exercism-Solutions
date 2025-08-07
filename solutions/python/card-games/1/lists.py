def get_rounds(number):
    return list((number,number+1,number+2))
def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2
def list_contains_round(rounds, number):
    for i in rounds:
        if i == number:
            return True
    return False
def card_average(hand):
    return sum(hand) / len(hand)
def approx_average_is_average(hand):
    if (sum(hand) / len(hand))==(hand[0]+hand[-1])/2 or (sum(hand) / len(hand))==hand[int(len(hand)/2)]:
        return True
    return False
def average_even_is_average_odd(hand):
    if sum(hand[::2]) / len(hand[::2]) == sum(hand[1::2]) / len(hand[1::2]):
        return True
    return False
def maybe_double_last(hand):
    if hand[-1]==11:
        hand[-1]=22
        return hand
    return hand
