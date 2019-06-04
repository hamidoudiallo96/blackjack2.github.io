import random # IMPORTING RANDOM, WILL BE USED LATER TO SHUFFLE THE DECK

# Global Variable
# CONTAINS ALL THE NECCESSARY INGREDIENTS TO CREATE THE DECK.
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True

# BLACKJACK OR 21 GAME
# THE PLANNING PHASE

# Create a deck of 52 cards: Completed


class Card: # CREATING THE CARD TYPES
	
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return f'{self.rank} of {self.suit}.'

# TEST FILES FOR  ADMIN USE ONLY:
	#A = Card('Hearts', 'Nine')
	#print(A.__str__())


class Deck:  #CREATING THE DECK
	def __init__(self): # This creates the deck, we put in in the init method because we want it to stay constant
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))

	def __str__(self): # lists the deck 
		deck_comp = ""
		for card in self.deck:
			deck_comp += '\n'+ card.__str__()
		return f"The deck has {deck_comp}"

	def shuffle(self): #Shuffle the deck
		random.shuffle(self.deck)
	
	def deal(self): # After a player chooses a card, the card is removed from the deck
		single_card = self.deck.pop()
		return single_card



# TEST FILES FOR  ADMIN USE ONLY:
	#B = Deck()
	#B.shuffle()
	#print(B.__str__())




# Players hand

class Hand:

	def __init__(self):
		self.cards = [] # empty list to collect the cards in the players hand
		
		self.value = 0 # keeps track of the value of the players hand
		
		self.aces = 0 # keeps track of the aces that we have

	def add_card(self,card): # adds cards from the deal method in the Deck class
		self.cards.append(card) 
		self.value += values[card.rank]

		if card == 'Ace':
			self.aces += 1 # add 1 ace to hour ace attribute to know that we have one in our hand

	def adjust_for_ace(self):

		while self.value > 21 and self.aces: # in this instance self.aces is the same as self.aces > 0. 
			self.value -=10 # if it contains an ace, then that ace becomes a 1
			self.aces -=1   # this prevents us from having more than one ace at a time 
		
			

# TEST FILES FOR  ADMIN USE ONLY:


	#test_deck = Deck()
	#test_deck.shuffle()
	#test_1 = Hand()
	#test_1.add_card(test_deck.deal())
	#test_1.add_card(test_deck.deal())
	#test_1.adjust_for_ace()
	#print(test_1.value)

	#for i in test_1.card:
		#print(i)




	
	#Ask the Player for their bet
	#Make sure that the Player's bet does not exceed their available chips

class Chips: # keeps track of players starting chips before and after bets

	def __init__(self):
		self.total = int(input("Enter in a value: "))
		self.bet = 0

	def win_bet(self):
		self.total += self.bet # if the player wins the bet, then the bet is added to their total


	def lose_bet(self):
		self.total -= self.bet # if the player loses the bet, then its subtracted from their total




def take_bet(chips):

	while True:

		try:
			chips.bet = int(input('Enter in your bet: '))

		except ValueError:
			print("You did not enter in an integer. ")

		else:
			if chips.bet > chips.total:
				print('Sorry try again, you do not have enough chips to make this bet.'. chips.total)

			else:
				break




def hit(deck,hand): # allows both players to take hits from the deck
# changed print
    print(hand.add_card(deck.deal())) # same funtion used to get the single_card from the deal method
    hand.adjust_for_ace() # adjust for the amount of aces that you have.




def hit_or_stand(deck,hand): # asks the player if they want to draw another card or not
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break
     
    

def show_some(player,dealer): # this function will be passed through the Hand class
	print("Dealers Card")
	print("<Card is hidden>", dealer.cards[1], sep = "\n")
	#print(dealer.cards[1])
	print("Player Hand:",* player.cards, sep = "\n") # * prints out all the items in a collection or list

def show_all(player,dealer):
	print("Dealers hand: ", *dealer.cards, sep= '\n') # sep statement seperates the two collections in the print statement
	print("Dealers hand: ", dealer.value)
	print("Players hand: ", *player.cards, sep= '\n')
	print("Players hand: ", player.value)





def player_busts(player,dealer,chips): # if player loses
	print("Player Busts!")
	chips.lose_bet()
    

def player_wins(player,dealer,chips): # if player wins
	print("Player Wins!")
	chips.win_bet()
    

def dealer_busts(player,dealer,chips): # if computer loses
	print("Dealer Busts!")
	chips.win_bet()
    
    
def dealer_wins(player,dealer,chips): # if computer wins
	print("Dealer Wins!")
	chips.lose_bet()
    
def push(player,dealer):
	print("Woah! This is a tie!") # in cases of a tie, the player will be given the option to push(get another card) or refuse, after a 2 sessions the player with 17 or more will win the game
    





# Final Script:



while True:
    # Print an opening statement
    print('Welcome, we will be playing Black Jack!')

    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    
        
    # Set up the Player's chips
    player_chips = Chips()
	
	# Prompt the Player for their bet
    take_bet(player_chips)

    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)

    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        print('\n')
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
        	player_busts(player_hand,dealer_hand,player_chips)
       		break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value < 17:
            (deck,dealer_hand)
           
            
        print('\n')
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        print('\n')
    
        # Run different winning scenarios
        if dealer_hand.value > 21:
            	dealer_busts(player_hand,dealer_hand,player_chips)
                
        elif  player_hand.value > 21:
            	player_busts(player_hand,dealer_hand,player_chips)


        elif player_hand.value > dealer_hand.value:
            dealer_busts(player_hand,dealer_hand,player_chips)
            player_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            player_busts(player_hand,dealer_hand,player_chips)
            dealer_wins(player_hand,dealer_hand,player_chips)

        else:
            	push(player_hand,dealer_hand)

        
    print('\n')
    # Inform Player of their chips total 
    print("Player hands stand at: ", player_chips.total)
    
    # Ask to play again
    new_game = input("Do you want to continue: y or n ")
    

    if new_game[0].lower() ==  'y': # in case the player fails to follow the original directions, the default value will be a lowercase y regardless of the input.
    	playing = True
    	continue

    else:
    	print("Thanks for playing")
    	break


# Control Number: 8451781 
        
    
# Driver function for further use
"""
if __name__ == __main__:
    player_1 = 'x'
    dealer = 'y'


"""
