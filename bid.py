
class Bid(object)
    def __init__(self, bidder, bid_suit, bid_number):
        self.bid = [bid_suit, int(bid_number)]
        self.bid_suit = bid_suit
        self.bid_number = int(bid_number)

class Bidround(object)
    def __init__(self):
        self.winner = []
        # winner of Bidround
        self.bid = winner.bid

