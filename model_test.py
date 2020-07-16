import unittest
import src.game.game_model as model

class setup(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

class card_test(unittest.TestCase):
    def test_constructor(self):
        card = model.Card(model.Suit.HEARTS, model.Value.JACK)
        self.assertEqual(card.suit, model.Suit.HEARTS)
        self.assertEqual(card.value, model.Value.JACK)

    def test_eq_overide(self):
        card1 = model.Card(model.Suit.HEARTS, model.Value.FIVE)
        card2 = model.Card(model.Suit.HEARTS, model.Value.FIVE)
        card3 = model.Card(model.Suit.CLUBS, model.Value.SEVEN)
        self.assertEqual(card1, card2)
        self.assertNotEqual(card1, card3)


class deck_test(unittest.TestCase):
    def test_constructor_card_generation(self):
        deck = model.Deck(1)
        self.assertNotEqual(deck.draw(), model.Card(model.Suit.CLUBS, model.Value.ACE))

    def test_constructor_deck_size(self):
        deck = model.Deck(3)
        self.assertEqual(deck.size(), 156)

    def test_swap(self):
        deck = model.Deck(1)
        temp1 = deck.deck[0]
        temp2 = deck.deck[51]
        deck.swap(0, 51)
        self.assertEqual(deck.deck[0], temp2)
        self.assertEqual(deck.deck[51], temp1)
        
    def test_shuffle(self):
        deck = model.Deck(3)
        temp = deck.deck[deck.size() - 1]
        deck.shuffle()
        self.assertNotEqual(deck.draw().suit, temp.getSuit())

    def test_reshuffles_deck(self):
        deck = model.Deck(1)
        for i in range(0,52-8):
            deck.draw()
        self.assertEqual(deck.size(), 8)
        deck.draw()
        self.assertEqual(deck.size(), 52)

if __name__ == '__main__':
    unittest.main()