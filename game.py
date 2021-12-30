import random
class Card:
    __suits = ('Heart',"Spade","Club","Diamond") # 0, 1, 2, 3 # card - 7 of Diamond 7 of Heart
    __ranks = (None,"Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King")
    
    
    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank
    
    # def print(self):
    #     print(self.rank + ' of ' + self.suit)

    def __str__(self) -> str:
        return Card.__ranks[self.rank] + ' of ' + Card.__suits[self.suit]

    
    def __eq__(self, other) -> bool:
        # self.rank == other.rank and self.suit == other.suit 
        if Card.__ranks[self.rank] == Card.__ranks[other.rank] and Card.__suits[self.suit] == Card.__suits[other.suit]:
            return True
        else:
            return False


# c = Card(1,12)
# print(c)

class Deck():

    def __init__(self) -> None:
        self.deck = [] # d -> deck
    
    def create_deck(self):
        for suit in range(0,4):
            for rank in range(1,14):
                self.deck.append(Card(suit,rank))

    # def print_deck(self):
    #     for card in self.deck:
    #         print(card)

    def remove_a_card(self,card):
        # card(1,13)
        self.deck.remove(card) # remove = [1,2,3] -> 3 == 3

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def isEmpty(self):
        return len(self.deck) == 0

    def deal_card(self, nHandsl, ncards): # list of hand obj
        l = len(nHandsl)
        for i in range(ncards):
            pos = i% l
            nHandsl[pos].add_card(self.deck[i])

    def remove_matches(self):
        de = self.deck # 13 - 2 = 11 # 0,10 # self.deck.copy()

        i = 0
        count = 0
        while i < len(de):  # 0,12 [0,1,0,3] # [1,3]
            # card = de[i]
            match = Card(3-de[i].suit, de[i].rank)
            if match in de:
                # print(match)
                # print(de[i])
                print(self.name + " remove matches\n "+ str(match) + ", " + de[i].__str__())
                self.remove_a_card(de[i])
                self.remove_a_card(match)
                count += 1
            else:
                
                i += 1
        return count    
        
    def __str__(self):
        s = ''
        for card in self.deck:
            s += card.__str__() + '\n'

        return s


# Player
class Hand(Deck):
    def __init__(self,name) -> None:
        self.deck = [] # player - deck
        self.name = name

    def add_card(self,card):
        self.deck.append(card)

    def __str__(self):
        if self.isEmpty():
            return self.name + ' contains Empty card'

        else:
            s = ''
            s += self.name + " contains \n" + super().__str__()
            return s

# d = Deck()
# d.create_deck()
# # d.print_deck()
# # print(d)
# c = Card(1,13)  # __new__
# d.remove_a_card(c)
# d.shuffle_deck()
# # print(d)
# player1 = Hand("Player1")
# player2 = Hand("Player2")

# d.deal_card([player1,player2],20)
# print(player1)
# # print(player2)

# # pair - colour and rank  # 

# player1.remove_matches()
# # player2.remove_matches()
# print(player1)
# # print(player2)


# Game begins

class OldMaidGame():
    def __init__(self, names) -> None:
        self.ddeck = Deck() # obj
        self.names = names

    def print_hands(self):
        for hand in self.hands:
            print(hand)

    def remove_all_matches(self):
        count = 0
        for hand in self.hands:
            count += hand.remove_matches()
        return count

    def find_neighbour(self,turn):
        # turn = 0 -> 
        for next in range(1, len(self.hands)):
            neigh = (turn + next) % len(self.hands)
            if self.hands[neigh].isEmpty():
                continue
            return neigh

    def playturn(self, turn):
        if self.hands[turn].isEmpty():
            return 0
        
        neighbour = self.find_neighbour(turn)
        self.hands[neighbour].shuffle_deck()
        pick_card = self.hands[neighbour].deck.pop()
        self.hands[turn].add_card(pick_card)
        count = self.hands[turn].remove_matches()
        return count


    def play(self):
        self.ddeck.create_deck()
        self.ddeck.remove_a_card(Card(1,12))
        self.ddeck.shuffle_deck()
        self.hands = [] # list hand obj
        for name in self.names:
            self.hands.append(Hand(name)) # list hand obj

        self.ddeck.deal_card(self.hands,51)
        self.print_hands()
        # reove matches
        matches = self.remove_all_matches()
        self.print_hands()

        print("***********Game Begins****************")
        turn = 0
        while matches < 25:
            matches += self.playturn(turn)
            turn = (turn+1) % len(self.hands) # 3 + 1 % 4 - > 1
        self.print_hands()

game = OldMaidGame(["Player1","Player2","PLayer3","Player4"])
game.play() # OldMaidGame.play(game)