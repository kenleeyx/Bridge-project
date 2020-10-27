#for OOP pertaining to deck, cards, player

import random

valuedict = {x:x for x in range(2,11)}
valuedict.update({"J":11, "Q":12, "K":13, "A":14})
suits = ("Clubs", "Diamonds", "Hearts", "Spades")

class Player:
	def __init__(self, name, score=0, cards=[])
		self.name = name
		self.score = score
		self.cards = cards
	def 
class Card:
    def __init__(self, number, suit):
        self.suit = suit
        self.number = number
        self.value = valuedict[self.number]
        self.location = []
        self.owner = []
        self.name = "{} of {}".format(self.number, self.suit)

class Deck:
    def __init__(self):
        self.cards = []
        for x in valuedict:
            for y in suits:
                self.cards.append(Card(x,y))

	def shuffle(self, num=1):
			length = len(self.cards)
			for _ in range(num):
				# This is the fisher yates shuffle algorithm - shuffle (num) times
				for i in range(length-1, 0, -1):
					randi = random.randint(0, i)
					#generate a random number between 0 and i for each ith card in the deck, counting from the end
					#the idea is to swap a random card in the range(0,i) to the end(i-1th) position. decrease i by 1 and then repeat
					if i == randi:
						continue
					self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]
					#swap the position of the cards in the position i and random number
				# You can also use the build in shuffle method
				# random.shuffle(self.cards)

class Bid:
    def __init__(self, bidder, bid_suit, bid_number):
        self.bid = [bid_suit, int(bid_number)]
        self.bid_suit = bid_suit
        self.bid_number = int(bid_number)
        self.bidder = bidder
    
# class Deck:


#deck
#deck.sequence
#Draw(x) - takes the cards in deck with sequence 1-x and changes their location to Hand and Owner to player drawing)
	#Print("Y has drawn X cards")
#Deal(x) - selects X random cards with location in Deck and deals them to a player. Repeat for each player.
	#Print("Y has dealt X cards to each player")
#Reshuffle - takes all cards, changes owner to null, location to deck, sequence to random
	#Print("Y has reshuffled the deck")



#card
#Name(Jack of Spades)(Tuple)
#Number(J=11,Q=12,K=13, A=14)(Tuple)
#Suit(Club/Diamond/Heart/Spade)(Tuple)
#Location(Deck, play, trick X, hand)
#Deck sequence(used for ordering deck)
#Owner(can be null)

#player
#name
#points









    #Play(x) - if a card's location is in hand and owner is self, changes location to Play)
	#Print("Y has played the Name")
