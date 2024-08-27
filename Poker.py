import random
deckCardsList = ["Ace of Spades, ", "Two of Spades, ", "Three of Spades, ", "Four of Spades, ", "Five of Spades, ", "Six of Spades, ", "Seven of Spades, ", "Eight of Spades, ", "Nine of Spades, ", "Ten of Spades, ", "Jack of Spades, ", "Queen of Spades, ", "King of Spades, ", "Ace of Clubs, ", "Two of Clubs, ", "Three of Clubs, ", "Four of Clubs, ", "Five of Clubs, ", "Six of Clubs, ", "Seven of Clubs, ", "Eight of Clubs, ", "Nine of Clubs, ", "Ten of Clubs, ", "Jack of Clubs, ", "Queen of Clubs, ", "King of Clubs, ", "Ace of Diamonds, ", "Two of Diamonds, ", "Three of Diamonds, ", "Four of Diamonds, ", "Five of Diamonds, ", "Six of Diamonds, ", "Seven of Diamonds, ", "Eight of Diamonds, ", "Nine of Diamonds, ", "Ten of Diamonds, ", "Jack of Diamonds, ", "Queen of Diamonds, ", "King of Diamonds, ", "Ace of Hearts, ", "Two of Hearts, ", "Three of Hearts, ", "Four of Hearts, ", "Five of Hearts, ", "Six of Hearts, ", "Seven of Hearts, ", "Eight of Hearts, ", "Nine of Hearts, ", "Ten of Hearts, ", "Jack of Hearts, ", "Queen of Hearts, ", "King of Hearts, "]
shuffledDeck = []
shuffledDeck2 = []
shuffledDeck3 = []
shuffledDeck4 = []
shuffledDeck5 = []
shuffledDeck6 = []
shuffledDeck7 = []
shuffledDeck8 = []
shuffledDeck9 = []
shuffledDeck10 = []
LowestPossibleScore = False
lencards = len(deckCardsList)
p1DeckPossibilities = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
p2DeckPossibilities = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
p1DeckScores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
p2DeckScores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
p1allin = False
p2allin = False
p1fold = False
p2fold = False
TableCards = []
def ShuffleDeck1():
    #This sorts the deck. It is much longer than it needs to be.
    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = deckCardsList[cardnum]    
        shuffledDeck.append(card)
        deckCardsList.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck[cardnum]    
        shuffledDeck2.append(card)
        shuffledDeck.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck2[cardnum]    
        shuffledDeck3.append(card)
        shuffledDeck2.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck3[cardnum]    
        shuffledDeck4.append(card)
        shuffledDeck3.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck4[cardnum]    
        shuffledDeck5.append(card)
        shuffledDeck4.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck5[cardnum]    
        shuffledDeck6.append(card)
        shuffledDeck5.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck6[cardnum]    
        shuffledDeck7.append(card)
        shuffledDeck6.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck7[cardnum]    
        shuffledDeck8.append(card)
        shuffledDeck7.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck8[cardnum]    
        shuffledDeck9.append(card)
        shuffledDeck8.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck9[cardnum]    
        shuffledDeck10.append(card)
        shuffledDeck9.remove(card)

p1 = []
p2 = []
def SortDeck(pdeck):
    p1sorted = []
    sortlist = ["Ace", "Two", "Thr", "Fou", "Fiv", "Six", "Sev", "Eig", "Nin", "Ten", "Jac", "Que", "Kin"]
    for i in range(len(sortlist)):
        for index in range(5):
            player1card = pdeck[index]
            if player1card[0:3] == sortlist[i]:
                card = player1card
                p1sorted.append(card)
    return p1sorted

def RoyalFlush(p1sorted, score):
    global LowestPossibleScore
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    suitlist = ["e", "t", "d", "b"]
    for index in range(len(suitlist)):
        score+=1
        if p1c1[-4] == p1c2[-4] == p1c3[-4] == p1c4[-4] == p1c5[-4] == suitlist[index]:
            if p1c1[0:3] == "Ace" and p1c2[0:3] == "Ten" and p1c3[0:3] == "Jac" and p1c4[0:3] == "Que" and p1c5[0:3] == "Kin":
                LowestPossibleScore = True
                return score
    return score

def StraightFlush(p1sorted, score):
    global LowestPossibleScore
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    numlist = ["Ace", "Two", "Thr", "Fou", "Fiv", "Six", "Sev", "Eig", "Nin", "Ten", "Jac", "Que", "Kin"]
    for index in range(10):
        score +=1
        if p1c1[-4] == p1c2[-4] == p1c3[-4] == p1c4[-4] == p1c5[-4] == "e" or p1c1[-4] == p1c2[-4] == p1c3[-4] == p1c4[-4] == p1c5[-4] == "t" or p1c1[-4] == p1c2[-4] == p1c3[-4] == p1c4[-4] == p1c5[-4] == "d" or p1c1[-4] == p1c2[-4] == p1c3[-4] == p1c4[-4] == p1c5[-4] == "b":
            if p1c1[0:3] == numlist[-index] and p1c2[0:3] == numlist[-1 - index] and p1c3[0:3] == numlist[-2 - index] and p1c4[0:3] == numlist[-3 - index] and p1c5[0:3] == numlist[-4 - index]:
                LowestPossibleScore = True
                return score
    return score

def FourOfAKind(p1sorted, score):
    global LowestPossibleScore
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p1c1 = p1c1[0:3]
    p1c2 = p1c2[0:3]
    p1c3 = p1c3[0:3]
    p1c4 = p1c4[0:3]
    p1c5 = p1c5[0:3]
    numlist = ["Ace", "Kin", "Que", "Jac", "Ten", "Nin", "Eig", "Sev", "Six", "Fiv", "Fou", "Thr", "Two"]
    for index in range(len(numlist)):
        score+=1
        if p1c1 == numlist[index] and p1c2 == numlist[index] and p1c3 == numlist[index] and p1c4 == numlist[index] or p1c2 == numlist[index] and p1c3 == numlist[index] and p1c4 == numlist[index] and p1c5 == numlist[index]:
            LowestPossibleScore = True
            return score
    return score

def FullHouse(p1sorted, score):
    global LowestPossibleScore
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p1c1 = p1c1[0:3]
    p1c2 = p1c2[0:3]
    p1c3 = p1c3[0:3]
    p1c4 = p1c4[0:3]
    p1c5 = p1c5[0:3]
    numlist = ["Ace", "Kin", "Que", "Jac", "Ten", "Nin", "Eig", "Sev", "Six", "Fiv", "Fou", "Thr", "Two"]
    for index in range(len(numlist)):
        score+=1
        if (p1c1 == numlist[index] and p1c2 == numlist[index] and p1c3 == numlist[index] and p1c4 == p1c5) or (p1c1 == p1c2 and p1c3 == numlist[index] and p1c4 == numlist[index] and p1c5 == numlist[index]):
            LowestPossibleScore = True
            return score
    return score

def Flush(p1sorted, score):
    global LowestPossibleScore
    samesuitp1 = False
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    numlist = ["Ace", "Kin", "Que", "Jac", "Ten", "Nin", "Eig", "Sev", "Six", "Fiv", "Fou", "Thr", "Two"]
    if (p1c1[-4] == p1c2[-4] == p1c3[-4] == p1c4[-4] == p1c5[-4] == "e") or (p1c1[-4] == p1c2[-4] == p1c3[-4] == p1c4[-4] == p1c5[-4] == "t") or (p1c1[-4] == p1c2[-4] == p1c3[-4] == p1c4[-4] == p1c5[-4] == "d") or (p1c1[-4] == p1c2[-4] == p1c3[-4] == p1c4[-4] == p1c5[-4] == "b"):
        samesuitp1 = True
    for index in range(len(numlist)):
        score+=1
        if samesuitp1 == True:
            if p1c1[0:3] == numlist[index] or p1c2[0:3] == numlist[index] or p1c3[0:3] == numlist[index] or p1c4[0:3] == numlist[index] or p1c5[0:3] == numlist[index]:
                LowestPossibleScore = True
                return score
    return score

def Straight(p1sorted, score):
    global LowestPossibleScore
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p1c1 = p1c1[0:3]
    p1c2 = p1c2[0:3]
    p1c3 = p1c3[0:3]
    p1c4 = p1c4[0:3]
    p1c5 = p1c5[0:3]
    numlist = ["Ace", "Two", "Thr", "Fou", "Fiv", "Six", "Sev", "Eig", "Nin", "Ten", "Jac", "Que", "Kin"]
    for index in range(10):
        score+=1
        if p1c1 == numlist[-index] and p1c2 == numlist[-1 -index] and p1c3 == numlist[-2 -index] and p1c4 == numlist[-3 -index] and p1c5 == numlist[-4 -index]:
            LowestPossibleScore = True
            return score
    return score

def ThreeOfAKind(p1sorted, score):
    global LowestPossibleScore
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p1c1 = p1c1[0:3]
    p1c2 = p1c2[0:3]
    p1c3 = p1c3[0:3]
    p1c4 = p1c4[0:3]
    p1c5 = p1c5[0:3]
    numlist = ["Ace", "Kin", "Que", "Jac", "Ten", "Nin", "Eig", "Sev", "Six", "Fiv", "Fou", "Thr", "Two"]
    for index in range(len(numlist)):
        score+=1
        if (p1c1 == numlist[index] and p1c2 == numlist[index] and p1c3 == numlist[index]) or (p1c2 == numlist[index] and p1c3 == numlist[index] and p1c4 == numlist[index]) or (p1c3 == numlist[index] and p1c4 == numlist[index] and p1c5 == numlist[index]):
            LowestPossibleScore = True
            return score
    return score

def TwoPair(p1sorted, score):
    global LowestPossibleScore
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p1c1 = p1c1[0:3]
    p1c2 = p1c2[0:3]
    p1c3 = p1c3[0:3]
    p1c4 = p1c4[0:3]
    p1c5 = p1c5[0:3]
    numlist = ["Ace", "Kin", "Que", "Jac", "Ten", "Nin", "Eig", "Sev", "Six", "Fiv", "Fou", "Thr", "Two"]
    for index in range(len(numlist)):
        score+=1
        if (p1c1 == numlist[index] and p1c2 == numlist[index] and (p1c3 == p1c4 or p1c4 == p1c5)) or (p1c2 == numlist[index] and p1c3 == numlist[index] and p1c4 == p1c5) or (p1c3 == numlist[index] and p1c4 == numlist[index] and p1c1 == p1c2) or (p1c4 == numlist[index] and p1c5 == numlist[index] and (p1c1 == p1c2 or p1c2 == p1c3)):
            LowestPossibleScore = True
            return score
    return score

def PairHigh(p1sorted, score):
    global LowestPossibleScore
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p1c1 = p1c1[0:3]
    p1c2 = p1c2[0:3]
    p1c3 = p1c3[0:3]
    p1c4 = p1c4[0:3]
    p1c5 = p1c5[0:3]
    numlist = ["Ace", "Kin", "Que", "Jac", "Ten", "Nin", "Eig", "Sev", "Six", "Fiv", "Fou", "Thr", "Two"]
    for index in range(len(numlist)):
        score+=1
        if p1c1 == p1c2 == numlist[index] or p1c2 == p1c3 == numlist[index] or p1c3 == p1c4 == numlist[index] or p1c4 == p1c5 == numlist[index]:
            LowestPossibleScore = True
            return score
    return score

def HighHighCard(p1sorted, score):
    global LowestPossibleScore
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p1c1 = p1c1[0:3]
    p1c2 = p1c2[0:3]
    p1c3 = p1c3[0:3]
    p1c4 = p1c4[0:3]
    p1c5 = p1c5[0:3]
    numlist = ["Ace", "Kin", "Que", "Jac", "Ten", "Nin", "Eig", "Sev", "Six", "Fiv", "Fou", "Thr", "Two"]
    for index in range(len(numlist)):
        score+=1
        if p1c1 == numlist[index]:
            LowestPossibleScore = True
            return score
    return score

def DecideWinner():
    #This picks the winner(s) and does stuff with the pot
    global p1money, p2money, pot
    p1LowestScore = 999999999999999999999
    p2LowestScore = 999999999999999999999
    for index in range(len(p1DeckPossibilities)):
        if p1DeckScores[index] < p1LowestScore:
            p1LowestScore = p1DeckScores[index]
        if p2DeckScores[index] < p2LowestScore:
            p2LowestScore = p2DeckScores[index]
    if  p1LowestScore == p2LowestScore:
        print("You split the pot")
        pot = pot/2
        p1money = p1money + pot
        p2money = p2money + pot
        pot = 0
    elif  p1LowestScore < p2LowestScore:
        print("Player 1 gets the pot")
        p1money = p1money + pot
        pot = 0
    else:
        print("Player 2 gets the pot")
        p2money = p2money + pot
        pot = 0

def Picking_Winner(psorted, score):
    global LowestPossibleScore
    #This funciton goes through the hands you can have in poker until someone is a winner
    LowestPossibleScore = False
    score = RoyalFlush(psorted, score)
    if  LowestPossibleScore == False:
        score = StraightFlush(psorted, score)
    if  LowestPossibleScore == False:
        score = FourOfAKind(psorted, score)
    if  LowestPossibleScore == False:
        score = FullHouse(psorted, score)
    if  LowestPossibleScore == False:
        score = Flush(psorted, score)
    if  LowestPossibleScore == False:
        score = Straight(psorted, score)
    if  LowestPossibleScore == False:
        score = ThreeOfAKind(psorted, score)
    if  LowestPossibleScore == False:
        score = TwoPair(psorted, score)
    if  LowestPossibleScore == False:
        score = PairHigh(psorted, score)
    if  LowestPossibleScore == False:
        score = HighHighCard(psorted, score)
    return score

def Start_Game():
    #This adds cards to the player's hands and the pot
    cards = 0
    while cards < 2:
        card = shuffledDeck10[0]
        p1.append(card)
        shuffledDeck10.remove(card)
        card = shuffledDeck10[0]
        p2.append(card)
        shuffledDeck10.remove(card)
        cards = cards + 1
    for index in range(3):
        card = shuffledDeck10[0]
        TableCards.append(card)
        shuffledDeck10.remove(card)

def ValidateBet(p1bet, p2bet):
    #validates a bet that can be used in poker. Numbers must be positive, and less than or equal to your chip amount
    global p1fold, p2fold, p1money, p2money, pot
    p1fold = False
    p2fold = False
    p1allin = False
    p2allin = False
    p1bet1 = 0
    p2bet1 = 0
    while True:
        p1bet = str(p1bet)
        p2bet = str(p2bet)
        p1bettoomuch = False
        p2bettoomuch = False
        if p1bet.strip('-').isnumeric() and p2bet.strip('-').isnumeric():
            p1bet = int(p1bet)
            p2bet = int(p2bet)
            if p1bet > p1bet1:
                p1bet1 = p1bet
            if p2bet > p2bet1:
                p2bet1 = p2bet
            if p1bet >= 0 and p2bet >= 0:
                if p1bet > p1money and p1allin == False:
                    print("You can't bet more chips than you have")
                    p1bet = input("How much does player 1 bet?")
                    p1bettoomuch = True
                if p2bet > p2money and p2allin == False:
                    print("You can't bet more chips than you have")
                    p2bet = input("How much does player 2 bet?")
                    p2bettoomuch = True
                if p1bet == p1money and p1bet == p2bet:
                    p1allin = True
                    pot = pot + p1bet + p2bet
                    p1money = 0
                    p2money = p2money - p2bet
                    return[p1allin, p2allin, p1fold, p2fold]
                if p2bet == p2money and p1bet == p2bet:
                    p2allin = True
                    pot = pot + p1bet + p2bet
                    p1money = p1money - p1bet
                    p2money = 0
                    return[p1allin, p2allin, p1fold, p2fold]
                if p1bet == p2bet and p1bettoomuch == False and p2bettoomuch == False:
                    pot = pot + p1bet + p2bet
                    p1money = p1money - p1bet
                    p2money = p2money - p2bet
                    return[p1allin, p2allin, p1fold, p2fold]
                elif p1bettoomuch == False and p2bettoomuch == False:
                    if p1bet > p2bet:
                        print("player 1 bet", p1bet)
                        p2bet = input("player 2 must match player 1 or fold:")
                        p1bet = str(p1bet)
                    elif p1bet < p2bet:
                        print("player 2 bet", p2bet)
                        p1bet = input("player 1 must match player 2 or fold:")
                        p2bet = str(p2bet)
            elif p1bet < 0:
                print("You can't bet in the negative")
                p1bet = input("How much do you bet?")
            elif p2bet < 0:
                print("You can't bet in the negative")
                p2bet = input("How much do you bet?")
        elif (p1bet == "all in" and p2bet == "all in") or (p1bet == "all-in" and p2bet == "all-in") or (p1allin == True and p2bet == "all in") or (p1bet == "all in" and p2allin == True) or (p1allin == True and p2bet == "all-in") or (p1bet == "all-in" and p2allin == True):
            pot = pot + p1money + p2money
            p1money = 0
            p2money = 0
            p1allin = True
            p2allin = True
            return[p1allin, p2allin, p1fold, p2fold]
        elif p1bet == "all in":
            p1bet = p1money
            p1money = 0
            p1allin = True
            if int(p2bet) == p2money:
                p2bet = int(p2bet)
                pot = pot + p2bet + p1bet
                p2money = 0
                p2allin = True
                return[p1allin, p2allin, p1fold, p2fold]
            while True:
                if p2bet.isnumeric():
                    if p1bet > int(p2bet):
                        print("Player 1 went all in and had", p1bet, "money")
                        p2bet = input("player 2 must match player 1's bet or go all in")
                    elif int(p2bet) <= p2money:
                        p2bet = int(p2bet)
                        pot = pot + p2bet + p1bet
                        p1money = 0
                        p2money = p2money - p2bet
                        return[p1allin, p2allin, p1fold, p2fold]
                elif p2bet.lower() == "all in" or p2bet.lower() == "all-in":
                    pot = pot + p1bet + p2money
                    p1money = 0
                    p2money = 0
                    p2allin = True
                    return[p1allin, p2allin, p1fold, p2fold]
        elif p2bet == "all in":
            p2bet = p2money
            p2money = 0
            p2allin = True
            if int(p1bet) == p1money:
                p1bet = int(p1bet)
                pot = pot + p2bet + p1bet
                p1money = 0
                p1allin = True
                return[p1allin, p2allin, p1fold, p2fold]
            while True:
                if p1bet.isnumeric():
                    if p2bet > int(p1bet):
                        print("Player 2 went all in and had", p2bet, "money")
                        p1bet = input("player 1 must match player 2's bet or go all in")
                    elif int(p1bet) <= p1money:
                        p1bet = int(p1bet)
                        pot = pot + p1bet + p2bet
                        p1money = p1money - p1bet
                        p2money = 0
                        return[p1allin, p2allin, p1fold, p2fold]
                elif p1bet.lower() == "all in" or p1bet.lower() == "all-in":
                    pot = pot + p2bet + p1money
                    p1money = 0
                    p2money = 0
                    p1allin = True
                    return[p1allin, p2allin, p1fold, p2fold]
        elif p1bet == "fold":
            print("Player 1 chooses to fold. Player 2 wins!")
            pot = pot + p1bet1 + p2bet1
            p2money = p2money + pot - p2bet1
            p1money = p1money - p1bet1
            p1fold = True
            return[p1allin, p2allin, p1fold, p2fold]
        elif p2bet == "fold":
            print("Player 2 chooses to fold. Player 1 wins!")
            pot = pot + p1bet1 + p2bet1
            p1money = p1money + pot - p1bet1
            p2money = p2money - p2bet1
            p2fold = True
            return[p1allin, p2allin, p1fold, p2fold]
        elif p1bet == "match" and p2bet.isnumeric():
            p2bet = int(p2bet)
            pot = pot + p2bet + p2bet
            p1money = p1money - p2bet
            p2money = p2money - p2bet
            return[p1allin, p2allin, p1fold, p2fold]
        elif p2bet == "match" and p1bet.isnumeric():
            p1bet = int(p1bet)
            pot = pot + p1bet + p1bet
            p2money = p2money - p1bet
            p1money = p1money - p1bet
            return[p1allin, p2allin, p1fold, p2fold]
        if p1bet == "":
            p1bet = input("Player 1 must bet something or fold: ")
        if p2bet == "":
            p2bet = input("Player 2 must bet something or fold: ")
        elif not(p1bet.strip('-').isnumeric):
            p1bet = input("Player 1, you must bet a numerical number or go all in: ")
        elif not(p2bet.strip('-').isnumeric):
            p2bet = input("Player 2, you must bet a numerical number or go all in: ")

p1money = 1000
p2money = 1000
pot = 0
def TheBetting():
    #Allows you to bet 3 times and then pick 3 cards from the table
    global p1money, p2money, pot, p1allin, p2allin, p1fold, p2fold, p1, p2, TableCards, shuffledDeck10
    print("Your cards are:", "".join(p1))
    print("The Table Cards are:", "".join(TableCards))
    print("player 1 has", p1money, "chips")
    while True:
        print("You cannot bet more chips than you have")
        p1bet = input("How much does player 1 bet?")
        if p1bet.isnumeric():
            p1bet = int(p1bet)
            if p1bet <= p1money:
                break
        else:
            break
    print("\n" * 20)
    if p1bet != "fold":
        print("Your cards are:", "".join(p2))
        print("The Table Cards are:", "".join(TableCards))
        print("player 2 has", p2money, "chips")
        print("player 1 has bet", p1bet)
        while True:
            print("You cannot bet more chips than you have")
            p2bet = input("How much does player 2 bet?")
            if p2bet.isnumeric():
                p2bet = int(p2bet)
                if p2bet <= p2money:
                    break
            else:
                break
        print("\n" * 20)
        p1allin, p2allin, p1fold, p2fold, = ValidateBet(p1bet, p2bet)

    if p1bet == "fold":
        p1fold = True

    if p1fold == False and p2fold == False and p1allin == False and p2allin == False:
        TableCards.append(shuffledDeck10[0])
        shuffledDeck10.remove(shuffledDeck10[0])
        print("The pot is", pot)
        print("These are the new TableCards:", "".join(TableCards))
        print("player 1 has", p1money, "chips")
        while True:
            print("You cannot bet more chips than you have")
            p1bet2 = input("How much does player 1 bet?")
            if p1bet2.isnumeric():
                p1bet2 = int(p1bet2)
                if p1bet2 <= p1money:
                    break
            else:
                break
        if p1bet2 != "fold":
            print("player 1 bet", p1bet2)
            print("player 2 has", p2money, "chips")
            while True:
                print("You cannot bet more chips than you have")
                p2bet2 = input("How much does player 2 bet?")
                if p2bet2.isnumeric():
                    p2bet2 = int(p2bet2)
                    if p2bet2 <= p2money:
                        break
                else:
                    break
            p1allin, p2allin, p1fold, p2fold, = ValidateBet(p1bet2, p2bet2)

        if p1bet2 == "fold":
            p1fold = True
            p2money = p2money + pot
            pot = 0

    if p1fold == False and p2fold == False and p1allin == False and p2allin == False:
        print("The pot is", pot)
        TableCards.append(shuffledDeck10[0])
        shuffledDeck10.remove(shuffledDeck10[0])
        print("The pot is", pot)
        print("These are the final Table Cards:", "".join(TableCards))
        print("player 1 has", p1money, "chips")
        while True:
            print("You cannot bet more chips than you have")
            p1bet3 = input("How much does player 1 bet?")
            if p1bet3.isnumeric():
                p1bet3 = int(p1bet3)
                if p1bet3 <= p1money:
                    break
            else:
                break
        if p1bet3 != "fold":
            print("player 1 bet", p1bet3)
            print("player 2 has", p2money, "chips")
            while True:
                print("You cannot bet more chips than you have")
                p2bet3 = input("How much does player 2 bet?")
                if p2bet3.isnumeric():
                    p2bet3 = int(p2bet3)
                    if p2bet3 <= p2money:
                        break
                else:
                    break
            p1allin, p2allin, p1fold, p2fold, = ValidateBet(p1bet3, p2bet3)

        if p1bet3 == "fold":
            p1fold = True
            p2money = p2money + pot
            pot = 0

while True:
    #Runs the actual game. Decides if it runs again
    ShuffleDeck1()
    Start_Game()
    TheBetting()
    if p1fold == False and p2fold == False:
        p1Deck = [p1[0], p1[1], TableCards[0], TableCards[1], TableCards[2], TableCards[3], TableCards[4]]
        index = 0
        for a in range(3):
            if index == 21:
                break
            for b in range(3):
                if index == 21:
                    break
                if b+1 <= a:
                    break
                for c in range(3):
                    if index == 21:
                        break
                    if c+2 <= b:
                        break
                    for d in range(3):
                        if index == 21:
                            break
                        if d+3 <= c:
                            break
                        for e in range(3):
                            if index == 21:
                                break
                            if e+4 <= d:
                                break
                            p1DeckPossibilities[index] = SortDeck([p1Deck[a], p1Deck[b+1], p1Deck[c+2], p1Deck[d+3], p1Deck[e+4]])
                            print(p1DeckPossibilities[index])
                            index+=1

        p2Deck = [p2[0], p2[1], TableCards[0], TableCards[1], TableCards[2], TableCards[3], TableCards[4]]
        index = 0
        for a in range(3):
            if index == 21:
                break
            for b in range(3):
                if index == 21:
                    break
                if b+1 <= a:
                    break
                for c in range(3):
                    if index == 21:
                        break
                    if c+2 <= b:
                        break
                    for d in range(3):
                        if index == 21:
                            break
                        if d+3 <= c:
                            break
                        for e in range(3):
                            if index == 21:
                                break
                            if e+4 <= d:
                                break
                            p2DeckPossibilities[index] = SortDeck([p2Deck[a], p2Deck[b+1], p2Deck[c+2], p2Deck[d+3], p2Deck[e+4]])
                            print(p2DeckPossibilities[index])
                            index+=1
        for x in range(21):
            p1DeckScores[x] = Picking_Winner(p1DeckPossibilities[x], p1DeckScores[x])
        for x in range(21):
            p2DeckScores[x] = Picking_Winner(p2DeckPossibilities[x], p2DeckScores[x])
        DecideWinner()
    if p1money == 0:
        print("Player 1 has lost")
        print("Player 2 has 2,000 chips")
        break
    if p2money == 0:
        print("player 2 has lost")
        print("Player 1 has 2,000 chips")
        break
    print("Player 1 has", p1money, "chips")
    print("Player 2 has", p2money, "chips")
    p1_again = input("Would player 1 like to play again?")
    p2_again = input("Would player 2 like to play again?")

    if p1_again == "yes" and p2_again == "yes" and p1money != 0 and p2money != 0:
        print("\n" * 20)
        pot = 0
        p1 = []
        p2 = []
        deckCardsList = ["Ace of Spades, ", "Two of Spades, ", "Three of Spades, ", "Four of Spades, ", "Five of Spades, ", "Six of Spades, ", "Seven of Spades, ", "Eight of Spades, ", "Nine of Spades, ", "Ten of Spades, ", "Jack of Spades, ", "Queen of Spades, ", "King of Spades, ", "Ace of Clubs, ", "Two of Clubs, ", "Three of Clubs, ", "Four of Clubs, ", "Five of Clubs, ", "Six of Clubs, ", "Seven of Clubs, ", "Eight of Clubs, ", "Nine of Clubs, ", "Ten of Clubs, ", "Jack of Clubs, ", "Queen of Clubs, ", "King of Clubs, ", "Ace of Diamonds, ", "Two of Diamonds, ", "Three of Diamonds, ", "Four of Diamonds, ", "Five of Diamonds, ", "Six of Diamonds, ", "Seven of Diamonds, ", "Eight of Diamonds, ", "Nine of Diamonds, ", "Ten of Diamonds, ", "Jack of Diamonds, ", "Queen of Diamonds, ", "King of Diamonds, ", "Ace of Hearts, ", "Two of Hearts, ", "Three of Hearts, ", "Four of Hearts, ", "Five of Hearts, ", "Six of Hearts, ", "Seven of Hearts, ", "Eight of Hearts, ", "Nine of Hearts, ", "Ten of Hearts, ", "Jack of Hearts, ", "Queen of Hearts, ", "King of Hearts, "]
        shuffledDeck = []
        shuffledDeck2 = []
        shuffledDeck3 = []
        shuffledDeck4 = []
        shuffledDeck5 = []
        shuffledDeck6 = []
        shuffledDeck7 = []
        shuffledDeck8 = []
        shuffledDeck9 = []
        shuffledDeck10 = []
        p1DeckPossibilities = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        p2DeckPossibilities = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        p1DeckScores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        p2DeckScores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        lencards = len(deckCardsList)
        TableCards = []

    elif p1_again == "no" or p2_again == "no":
        break
    else:
        p1_again = input("Would player 1 like to play again?")
        p2_again = input("Would player 2 like to play again?")
