import random

class Card:

    deckcount = 0

    def __init__(self, value, cardtype):
        self.value = value
        self.cardtype = cardtype
        Card.deckcount += 1

    def compare(self, card):
        if self.value > card.value:
            print("Your card ({}) is greater than theirs ({}).".format((str(self.value) + " " + self.cardtype), (str(card.value) + " " + card.cardtype)))
        elif self.value < card.value:
            print("Their card ({}) is greater than yours ({}).".format((str(card.value) + " " + card.cardtype), (str(self.value) + " " + self.cardtype)))
        else:
            print("The cards are equal. " + str(self.value))

deck = []

for i in range(12): #make da cards
    types = {1:"hearts",
             2:"clubs",
             3:"spades",
             4:"diamonds"
             }
    deck.append(Card(random.randint(0,12), types[random.randint(1,4)]))
    
for i in deck: 
    print(i.value, i.cardtype) #unshuffled print

def shuffle(deck): #what do you think it does bud
    returndeck = []
    print("now shuffling deck... :3")
    while len(deck) > 0:
        card = random.randint(0, len(deck)) #this is an indice not an actual object dummy
        returndeck.append(deck[card-1])
        del deck[card-1]
    print("deck shuffed ! >.<")
    for i in returndeck:
        print(i.value, i.cardtype)
    return(returndeck)

deck = shuffle(deck)

card1a, card1b, card1c, card2a, card2b, card2c = deck.pop(0), deck.pop(1), deck.pop(2), deck.pop(3), deck.pop(4), deck.pop(5)

card1a.compare(card2a)
card1b.compare(card2b)
card1c.compare(card2c)
