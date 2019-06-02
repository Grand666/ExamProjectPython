import sys
import os
import random
import time
from Player import Player

def youAsPlayer():
    playerHand = []
    dealerHand = []
    cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
    player = Player(2000, playerHand)

    while True:
        if len(player.playerHand) > 0:
            player.playerHand.clear()
            dealerHand.clear()

        player.playerHand.append(random.choice(cards))
        player.playerHand.append(random.choice(cards))
        dealerHand.append("X")
        dealerHand.append(random.choice(cards))

        insuranceBet = 0

        #players turn
        print("You have", player.saldo, "$ worth of chips left")
        print("Choose your bet?")

        validBet = False
        while not validBet:
            bet = input("50, 100, 150 or 200 \n")
            if bet.lower() == "quit":
                sys.exit()
            if bet == "50" or bet == "100" or bet == "150" or bet == "200":
                if int(bet) > player.saldo:
                    print("You only have", player.saldo, "$")
                    continue
                validBet = True
            
        os.system("clear")
        print("You bet", bet, "$\n")

        print("The cards have been dealt")
        print("The dealer has", dealerHand)
        print("You have", player.playerHand, "\n")
        
        try:
            bet = int(bet)
        except ValueError:
            print("hmm")

        while getHandValue(player.playerHand) < 21:
            validAnswer = False
            while not validAnswer:
                answer = input("Hit or Stand? \n").lower()
                if answer == "quit":
                    sys.exit()
                if answer == "hit" or answer == "stand":
                    validAnswer = True

            if answer == "hit":
                player.playerHand.append(random.choice(cards))
                print("\nYou have", player.playerHand)
                time.sleep(1)
            if answer == "stand":
                time.sleep(1)
                break
        
        if checkForBlackJack(player.playerHand):
            print("You got a BlackJack")

        if getHandValue(player.playerHand) > 21:
            print("Bust. House takes all \n")
            player.saldo -= bet
            newGame(player)
            continue

        #Insurance
        if "Ace" in dealerHand:
            insuranceBet = askForInsurance(bet)
            

        #Dealers turn
        print("\nDealers turn")

        dealerHand.remove("X")
        dealerHand.insert(0, random.choice(cards))
        print(dealerHand,"\n")

        while True:
            if getHandValue(dealerHand) > 21:
                print("House is busted, Player Wins!\n")
                player.saldo += bet*2
                break
            if checkForBlackJack(dealerHand) and not checkForBlackJack(player.playerHand):
                print("House has BlackJack, House Wins!\n")
                player.saldo -= bet
                break
            if getHandValue(dealerHand) == getHandValue(player.playerHand):
                print("Standoff")
                print("As result you get your", bet, "$ back!\n")
                break
            if getHandValue(dealerHand) > getHandValue(player.playerHand):
                print("The dealer has", dealerHand)
                print("You have", player.playerHand)
                print("House wins!\n")
                player.saldo -= bet
                break
            if getHandValue(dealerHand) < 21:
                dealerHand.append(random.choice(cards))
                print("Dealer hits")
                print(dealerHand, "\n")
            time.sleep(1)

        if insuranceBet > 0 and checkForBlackJack(dealerHand):
            player.saldo += insuranceBet * 2
        elif insuranceBet > 0 and not checkForBlackJack(dealerHand):
            player.saldo -= insuranceBet
            

        newGame(player)


def askForInsurance(bet):
    #Does the player want insurance?
    while True:
        answer = input("\nThe dealer has an Ace, do you want insurance? (y/n) \n").lower()
        if answer == "y":
            while True:
                answer = input("How much du you want to insurance? \n")
                if answer.lower() == "quit":
                    sys.exit()
                try:
                    val = int(answer)
                    if val > 0 and val <= bet/2:
                        print("You chose to insurance", answer, "$")
                        return val
                    else:
                        print("You can only insurance up to half of your bet\n")
                except ValueError:
                    print("Please input a number\n")
        if answer == "n":
            print("You chose not to take insurance")
            return 0
        if answer == "quit":
            sys.exit()

def newGame(player):
    #Does the player still have chips? 
    while player.saldo < 50:
        print("You don't have enough chips to play...")
        answer = input("Would you like to buy more chips? (y/n) \n").lower()
        if answer == "y":
            while True:
                answer = input("How much?\n")
                if answer.lower() == "quit":
                    sys.exit()                        
                try:
                    val = int(answer)
                    if val >= 50:
                        player.saldo += val
                        return
                    else:
                        print("The smallest chip costs 50 $")
                except ValueError:
                    print("Please input a number")
        if answer == "n":
            print("Thanks for the games, please leave the table")
            sys.exit()
        if answer == "quit":
            sys.exit()

def checkForBlackJack(list):
    if len(list) == 2 and "Ace" in list:
        if 10 in list or "Jack" in list or "Queen" in list or "King" in list:
            return True
    return False

def getHandValue(list):
    sum = 0
    aces = 0
    for card in list:
        if card == "Jack" or card == "Queen" or card == "King":
            sum += 10
        elif card == "Ace":
            sum += 11
            aces += 1
        else:
            sum += card
    
    if sum > 21 and aces > 0:
        sum -= 10 * aces
    
    return sum 

    

def main():
    try:
        player = sys.argv[1]
        
        if player.lower() == "player":
            print("You are now a player \n")
            youAsPlayer()
        else:
            print("Please write 'Player' as the 3rd argument")
    except IndexError:
        print("You need to specify the an argument (What 'role' you want to play as)")
        print("ie. ($ python BlackJack.py Dealer or $ python BlackJack.py Player)")


if __name__ == "__main__":
    main()
