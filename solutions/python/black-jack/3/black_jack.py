def value_of_card(card):
    face_cards='JQK'
    if card in face_cards:
        return 10
    if card=='A':
        return 1
    return int(card)
def higher_card(card_one, card_two):
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    if value_of_card(card_one)==value_of_card(card_two):
        return card_one , card_two
    return card_two
def value_of_ace(card_one, card_two):
    if value_of_card(card_one) + value_of_card(card_two) > 11:
        return 1
    if card_one=='A' or card_two=='A':
        return 1
    return 11
def is_blackjack(card_one, card_two):
    if card_one=='A' and value_of_card(card_two)==10:
        return True
    if card_two=='A' and value_of_card(card_one)==10:
        return True
    if value_of_card(card_one) + value_of_card(card_two)==21:
        return True
    return False
def can_split_pairs(card_one, card_two):
    if value_of_card(card_one)==value_of_card(card_two):
        return True
    return False
def can_double_down(card_one, card_two):
    if value_of_card(card_one) + value_of_card(card_two)<=11 and value_of_card(card_one) + value_of_card(card_two) >=9:
        return True
    return False