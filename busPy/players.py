players = []

class Player:
    def __init__(self, username):
        self.username = username
        self.drinks = 0
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

    def getCards(self):
        return self.cards


def addPlayer(username):
    try:
        newPlayer = Player(username)
        players.append(newPlayer)
        return f"{username} has been added to the players list!"
    except:
        return "An error occured"

def getAllPlayers():
    dicto =  {}
    for i, player in enumerate(players):
        obj = {
            'username': player.username,
            'drinks': player.drinks,
            'cards': player.cards
        }
        dicto[i] = obj
    return dicto