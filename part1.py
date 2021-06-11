"""
Part 1 of tasks.
"""

vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']


def create_deck_cards_lambda() -> list:
    """
    Creates 52 cards in a deck, with help of lambda, map, zip and list comprehension,
    all in a single expression
    :return: list of `tuples` containing card combinations
    """

    return list(card for new_suit in
                map(lambda one_suit: list(zip(vals, [one_suit] * len(vals))), suits)
                for card in new_suit)


def create_deck_cards_normal_function() -> list:
    """
    Creates 52 cards in a deck via a simpler approach
    :return: list of tuples containing card combinations
    """
    return [(val, suit) for suit in suits for val in vals]


class Hand:
    def __init__(self, cards):
        self.cards = []
        self.values = []
        for c in cards:
            self.cards.append(Card(c))
        self.set_values()

    def set_values(self):
        for card in self.cards:
            self.values.append(card.value)
        self.values.sort()

    def check_royal_flush(self):
        suit_type = self.cards[0].suit
        for card in self.cards:
            if card.suit != suit_type:
                return False
            suit_type = card.suit
        lowest_value = max(self.values)
        if lowest_value == 14:
            num = len(self.values)
            for i in range(num):
                if not ((lowest_value - i) in self.values):
                    return False
            return True

    def check_straight_flush(self):
        if self.check_straight() and self.cehck_flush():
            return True
        else:
            return False

    def check_four_of_a_kind(self):
        if (len(self.values)) < 4:
            return False
        card_one_count = self.values.count(self.values[0])
        card_two_count = self.values.count(self.values[len(self.values) - 1])
        if card_one_count == 4 or card_two_count == 4:
            return True
        else:
            return False

    def check_full_house(self):
        if (len(self.values)) < 5:
            return False
        card_one_count = self.values.count(self.values[0])
        card_two_count = self.values.count(self.values[len(self.values) - 1])

        if (card_one_count == 2 and card_two_count == 3) or (card_one_count == 3 and card_two_count == 2):
            return True
        else:
            return False

    def cehck_flush(self):
        current_suit = self.cards[0].suit
        for card in self.cards:
            if card.suit != current_suit:
                return False
            current_suit = card.suit
        return True

    def check_straight(self):
        lowest_value = min(self.values)
        num = len(self.values)
        for i in range(num):
            if lowest_value + i not in self.values:
                return False
        return True

    def check_three_of_a_kind(self):
        card_one_count = self.values.count(self.values[0])
        card_two_count = self.values.count(self.values[len(self.values) - 1])

        if card_one_count == 3 or card_two_count == 3:
            return True
        else:
            return False

    def check_two_pair(self):
        if (len(self.values)) < 4:
            return False
        card_one_count = self.values.count(self.values[0])
        card_two_count = self.values.count(self.values[2])
        card_three_count = self.values.count(self.values[len(self.values) - 1])

        if (card_one_count == 2 and card_two_count == 2) or (card_one_count == 2 and card_three_count == 2) or (
                card_two_count == 2 and card_three_count == 2):
            return True
        return False

    def check_one_pair(self):
        card_one_count = self.values.count(self.values[0])
        card_two_count = self.values.count(self.values[2])
        card_three_count = self.values.count(self.values[len(self.values) - 1])

        if (card_one_count == 2 or card_two_count == 2 or card_three_count == 2):
            return True
        return False

    def check_hand_score(self):
        if self.check_royal_flush():
            return 9, 'Royal Flush'
        elif self.check_straight_flush():
            return 8, 'Straight Flush'
        elif self.check_four_of_a_kind():
            return 7, 'Four Of A Kind'
        elif self.check_full_house():
            return 6, 'Full House'
        elif self.cehck_flush():
            return 5, 'Flush'
        elif self.check_straight():
            return 4, 'Straight'
        elif self.check_three_of_a_kind():
            return 3, 'Three Of A Kind'
        elif self.check_two_pair():
            return 2, 'Two Pair'
        elif self.check_one_pair():
            return 1, 'One Pair'
        return 0, 'No Hand'


class Card:
    def __init__(self, card=[]):
        self.value = self.get_value(card[0])
        self.suit = card[1]

    def get_value(self, y):
        return {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'jack': 11,
                'queen': 12, 'king': 13, 'ace': 14}.get(y)


def play_poker_game(hand1: 'cards for player1',
                    hand2: 'cards for player2') -> str:
    """
    Play Poker with the given cards
    :param hand1: Cards for player 1
    :param hand2: Cards for player 2
    :return: win result based on cards
    """
    if len(hand1) != len(hand2) or len(hand1) < 3:
        raise ValueError
    player_ones_hand = Hand(hand1)
    player_twos_hand = Hand(hand2)

    player_one_score = player_ones_hand.check_hand_score()
    player_two_score = player_twos_hand.check_hand_score()

    if player_one_score[0] != 0 or player_two_score[0] != 0:
        if player_one_score[0] > player_two_score[0]:
            result = "Player 1 won! He has a {0}".format(player_one_score[1])
        elif player_one_score[0] == player_two_score[0]:
            result = "It's a draw! Both players have {0}".format(player_one_score[1])
        else:
            result = "Player 2 won! He has a {0}".format(player_two_score[1])
    else:
        if max(player_ones_hand.values) > max(player_twos_hand.values):
            result = "Player 1 won! He has a High Card"
        elif max(player_ones_hand.values) == max(player_twos_hand.values):
            result = "Again it's a draw! Both players have same High Card"
        else:
            result = "Player 2 won! He has a High Card"
    return result
