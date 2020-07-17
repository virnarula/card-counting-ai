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
        self.assertNotEqual(deck.draw(), temp)

    def test_reshuffles_deck(self):
        deck = model.Deck(1)
        for i in range(0,52-8):
            deck.draw()
        self.assertEqual(deck.size(), 8)
        deck.draw()
        self.assertEqual(deck.size(), 52)

class game_test(unittest.TestCase):
    def test_constructor(self):
        game = model.Game(1, 500)
        self.assertEqual(game.decks, 1)
        self.assertEqual(game.bet, 0)

    def test_bet(self):
        game = model.Game(1, 500)
        game.make_bet(40)
        self.assertEqual(game.bet, 40)
    
    def test_deal_cards(self):
        game = model.Game(1, 500)
        game.make_bet(40)
        game.deal_cards()

        self.assertEqual(len(game.dealer_cards), 2)
        self.assertEqual(len(game.player_cards), 2)
    
    def test_hit(self):
        game = model.Game(1, 500)
        game.make_bet(40)
        game.player_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.TWO))
        game.player_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.THREE))
        game.dealer_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.TWO))
        game.dealer_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.THREE))
        game.hit()
        
        self.assertEqual(len(game.dealer_cards), 2)
        self.assertEqual(len(game.player_cards), 3)
    
    def test_dealer_hit(self):
        game = model.Game(1, 500)
        game.make_bet(40)
        game.player_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.TWO))
        game.player_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.THREE))
        game.dealer_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.TWO))
        game.dealer_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.THREE))
        game.dealer_hit()

        self.assertNotEqual(len(game.dealer_cards), 2)

    def test_end_round_draw(self):
        game = model.Game(1, 500)
        game.make_bet(40)
        game.player_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.TWO))
        game.player_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.THREE))
        game.dealer_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.TWO))
        game.dealer_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.THREE))
        game.end_round()

        self.assertEqual(game.money, 500)

    def test_end_round_win(self):
        game = model.Game(1, 500)
        game.make_bet(40)
        game.player_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.TWO))
        game.player_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.FIVE))
        game.dealer_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.TWO))
        game.dealer_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.THREE))
        game.end_round()

        self.assertEqual(game.money, 540)

    def test_end_round_loss(self):
        game = model.Game(1, 500)
        game.make_bet(40)
        game.player_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.TWO))
        game.player_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.THREE))
        game.dealer_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.TWO))
        game.dealer_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.KING))
        game.end_round()

        self.assertEqual(game.money, 460)

    def test_clear_round(self):
        game = model.Game(1, 500)
        game.make_bet(40)
        game.player_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.TWO))
        game.player_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.THREE))
        game.dealer_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.TWO))
        game.dealer_cards.append(model.Card(model.Suit.DIAMONDS, model.Value.KING))
        game.end_round()

        self.assertEqual(game.money, 460)
        self.assertEqual(len(game.dealer_cards) == 0, True)
        self.assertEqual(len(game.player_cards) == 0, True)
        self.assertEqual(game.bet == 0, True)
        self.assertEqual(game.starting_money, 500)

    def test_is_blackjack(self):
        blackjack = []
        blackjack.append(model.Card(model.Suit.DIAMONDS, model.Value.ACE))
        blackjack.append(model.Card(model.Suit.DIAMONDS, model.Value.QUEEN))
        self.assertEqual(model.Game.isBlackjack(blackjack), True)

        blackjack.reverse()
        self.assertEqual(model.Game.isBlackjack(blackjack), True)

        not_blackjack = []
        not_blackjack.append(model.Card(model.Suit.DIAMONDS, model.Value.QUEEN))
        not_blackjack.append(model.Card(model.Suit.DIAMONDS, model.Value.TEN))
        self.assertFalse(model.Game.isBlackjack(not_blackjack))
        not_blackjack.reverse()
        self.assertFalse(model.Game.isBlackjack(not_blackjack))

    def test_evaluate_hand(self):
        blackjack = []
        blackjack.append(model.Card(model.Suit.DIAMONDS, model.Value.ACE))
        blackjack.append(model.Card(model.Suit.DIAMONDS, model.Value.QUEEN))
        self.assertEqual(model.Game.evaluateHand(blackjack), 22)
        blackjack.reverse()
        self.assertEqual(model.Game.evaluateHand(blackjack), 22)

        single_ace = []
        single_ace.append(model.Card(model.Suit.DIAMONDS, model.Value.ACE))
        single_ace.append(model.Card(model.Suit.SPADES, model.Value.SEVEN))
        self.assertEqual(model.Game.evaluateHand(single_ace), 18)
        single_ace.reverse()
        self.assertEqual(model.Game.evaluateHand(single_ace), 18)

        double_ace = []
        double_ace.append(model.Card(model.Suit.DIAMONDS, model.Value.ACE))
        double_ace.append(model.Card(model.Suit.CLUBS, model.Value.ACE))
        double_ace.append(model.Card(model.Suit.HEARTS, model.Value.EIGHT))
        self.assertEqual(model.Game.evaluateHand(double_ace), 20)
        double_ace.reverse()
        self.assertEqual(model.Game.evaluateHand(double_ace), 20)

        bust = []
        bust.append(model.Card(model.Suit.SPADES, model.Value.ACE))
        bust.append(model.Card(model.Suit.SPADES, model.Value.TEN))
        bust.append(model.Card(model.Suit.SPADES, model.Value.KING))
        bust.append(model.Card(model.Suit.SPADES, model.Value.FIVE))
        self.assertEqual(model.Game.evaluateHand(bust), -1)
        bust.reverse()
        self.assertEqual(model.Game.evaluateHand(bust), -1)
        
if __name__ == '__main__':
    unittest.main()