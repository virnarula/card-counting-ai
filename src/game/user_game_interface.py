import game_model as model

def getBet(game):
    print("You have " + str(game.money) + " dollars")
    bet = int(input("How much would you like to bet? "))
    return bet

def print_deal(game):
    print("The dealer shows a " + str(game.dealer_cards[0]))
    print("You have a " + str(game.player_cards[0]))
    print("You have a " + str(game.player_cards[1]))

def get_move(game):
    move = int(input("Enter 0 to stay, 1 to hit: "))
    if move == 1:
        game.hit()
        print_hit(game)
    elif move == 0:
        game.dealer_hit()
        print_dealer_hit(game)
    else:
        get_move(game)

def print_hit(game):
    card = game.player_cards[len(game.player_cards) - 1]
    print("You got a " + str(card))
    print()
    get_move(game)

def print_dealer_hit(game):
    print()
    print("The dealer shows: ")
    for card in game.dealer_cards:
        print(str(card.value) + " of " + str(card.suit))
    print("Dealers hand is worth " +  str(model.Game.evaluateHand(game.dealer_cards)))
    print()
    print("You have: ")
    for card in game.player_cards:
        print(str(card.value) + " of " + str(card.suit))
    print("Your hand is worth " + str(model.Game.evaluateHand(game.player_cards)))
    game.end_round()
    print()
    
if __name__ == "__main__":
    game = model.Game(1, 500)
    while game.money > 0:
        game.make_bet(getBet(game))
        game.deal_cards()
        print_deal(game)
        get_move(game)
    print()
    print("You ran out of money :(")


        
