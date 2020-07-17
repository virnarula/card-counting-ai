import enum
import random

class Suit(enum.Enum):
    CLUBS = 1
    SPADES = 2
    DIAMONDS = 3
    HEARTS = 4

class Value(enum.Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def getSuit(self):
        return self.suit

    def getValue(self):
        return self.value

    def getName(self):
        return str(self.value) + " of " + str(self.suit)

    def __eq__(self, other):
        if self.suit == other.suit and self.value == other.value:
            return True
        return False

class Deck:
    def __init__(self, decks):
        self.deck = []
        self.used_deck = []
        self.decks = decks
        for i in range(0, decks):
            for suit in Suit:
                for value in Value:
                    self.deck.append(Card(suit, value))

    def draw(self):
        to_return = self.deck.pop()
        used_cards.append(used_cards)
        if len(self.deck) < 8:
            self.__init__(self.decks)
        return to_return

    def size(self):
        return len(self.deck)

    def swap(self, i, j):
        if i > self.size() - 1 or i < 0 or j > self.size() - 1 or j < 0:
            raise Exception("value was out of range")

        temp = self.deck[i]
        self.deck[i] = self.deck[j]
        self.deck[j] = temp

    def shuffle(self):
        j = 0
        deck_length = len(self.deck)
        for i in range(0, deck_length):
            j = random.randint(i, deck_length - 1)
            self.swap(i, j)

    def printDeck(self):
        for card in self.deck:
            print(card.getName())

class Game:
    def __init__(self, decks, money):
        self.decks = decks
        self.deck = Deck(decks)
        self.money = money
        self.starting_money = money
        self.bet = 0
        self.player_cards = []
        self.dealer_cards = []
    
    def make_bet(self, bet):
        if bet <= 0 and bet > starting_money:
            raise Exception("Bet is not in acceptable range")
    
    def deal_cards(self):
        assert not self.player_cards
        assert not self.dealer_cards
        self.dealer_cards.append(deck.draw())
        self.dealer_cards.append(deck.draw())
        self.player_cards.append(deck.draw())
        self.player_cards.append(deck.draw())

    def hit(self):
        value = evaluateHand(self.player_cards)
        if value == -1 or value >= 21:
            raise Exception("Cannot hit. Current hand value: " + str(value))
        self.player_cards.append(deck.draw())
    
    def dealer_hit(self):
        value = evaluateHand(self.dealer_cards)
        while value < 16 and value != -1:
            self.dealer_cards.append(deck.draw())
            value = evaluateHand(self.dealer_cards)

    def end_round(self):
       players_hand = evaluateHand(self.player_cards)
       dealers_hand = evaluateHand(self.dealer_cards)

        if players_hand == dealers_hand:
           clear_round()
        elif players_hand > dealers_hand:
            self.money += bet
            clear_round()
        else:
            self.money -= bet
            clear_round()

    def clear_round(self):
        self.dealer_cards.clear()
        self.player_cards.clear()
        self.bet = 0

    def isBlackjack(hand):
        if len(hand) != 2:
            return False
        
        if hand[0].value > 10 and hand[1].value == 1:
            return True
        
        hand.reverse()

        if hand[0].value > 10 and hand[1].value == 1:
            return True

        return False

    def evaluateHand(hand):
        if isBlackjack(hand):
            return 22

        sum = 0
        aces = 0

        for card in hand:
            if card.getValue().value > 10:
                sum += 10
            elif card.getValue() == Value.ACE:
                sum += 1
                aces += 1
            else:
                sum += card.getValue().value

        while aces > 0 and sum <= 11:
            sum += 10
            aces -= 1

        if sum > 21:
            return -1

        return sum