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
shuffledDeck11 = []
shuffledDeck12 = []
shuffledDeck13 = []
shuffledDeck14 = []
shuffledDeck15 = []
shuffledDeck16 = []
shuffledDeck17 = []
shuffledDeck18 = []
shuffledDeck19 = []
shuffledDeck20 = []
lencards = len(deckCardsList)
player1win = False
player2win = False
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

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck10[cardnum]    
        shuffledDeck11.append(card)
        shuffledDeck10.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck11[cardnum]    
        shuffledDeck12.append(card)
        shuffledDeck11.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck12[cardnum]    
        shuffledDeck13.append(card)
        shuffledDeck12.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck13[cardnum]    
        shuffledDeck14.append(card)
        shuffledDeck13.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck14[cardnum]    
        shuffledDeck15.append(card)
        shuffledDeck14.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck15[cardnum]    
        shuffledDeck16.append(card)
        shuffledDeck15.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck16[cardnum]    
        shuffledDeck17.append(card)
        shuffledDeck16.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck17[cardnum]    
        shuffledDeck18.append(card)
        shuffledDeck17.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck18[cardnum]    
        shuffledDeck19.append(card)
        shuffledDeck18.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck19[cardnum]    
        shuffledDeck20.append(card)
        shuffledDeck19.remove(card)

p1 = []
p2 = []
p1sorted = []
p2sorted = []
def SortDeck():
    sortlist = ["Ace", "Two", "Thr", "Fou", "Fiv", "Six", "Sev", "Eig", "Nin", "Ten", "Jac", "Que", "Kin"]
    for i in range(len(sortlist)):
        for index in range(5):
            player1card = p1[index]
            if player1card[0:3] == sortlist[i]:
                card = player1card
                p1sorted.append(card)

    #sorting second player
    for i in range(len(sortlist)):
        for index in range(5):
            player2card = p2[index]
            if player2card[0:3] == sortlist[i]:
                card = player2card
                p2sorted.append(card)

def RoyalFlush():
    global player1win, player2win
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    suitlist = ["e", "t", "d", "b"]
    for index in range(len(suitlist)):
        if p1c1[-4] == p1c2[-4] == p1c3[-4] == p1c4[-4] == p1c5[-4] == suitlist[index]:
            if p1c1[0:3] == "Ace" and p1c2[0:3] == "Ten" and p1c3[0:3] == "Jac" and p1c4[0:3] == "Que" and p1c5[0:3] == "Kin":
                player1win = True
    p2c1 = p2sorted[0]
    p2c2 = p2sorted[1]
    p2c3 = p2sorted[2]
    p2c4 = p2sorted[3]
    p2c5 = p2sorted[4]
    for index in range(len(suitlist)):
        if p2c1[-4] == p2c2[-4] == p2c3[-4] == p2c4[-4] == p2c5[-4] == suitlist[index]:
            if p2c1[0:3] == "Ace" and p2c2[0:3] == "Ten" and p2c3[0:3] == "Jac" and p2c4[0:3] == "Que" and p2c5[0:3] == "Kin":
                player2win = True

def StraightFlush():
    global player1win, player2win
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p2c1 = p2sorted[0]
    p2c2 = p2sorted[1]
    p2c3 = p2sorted[2]
    p2c4 = p2sorted[3]
    p2c5 = p2sorted[4]
    numlist = ["Ace", "Two", "Thr", "Fou", "Fiv", "Six", "Sev", "Eig", "Nin", "Ten", "Jac", "Que", "Kin"]
    for index in range(10):
        if p1c1[-4] == p1c2[-4] == p1c3[-4] == p1c4[-4] == p1c5[-4] == "e" or p1c1[-4] == p1c2[-4] == p1c3[-4] == p1c4[-4] == p1c5[-4] == "t" or p1c1[-4] == p1c2[-4] == p1c3[-4] == p1c4[-4] == p1c5[-4] == "d" or p1c1[-4] == p1c2[-4] == p1c3[-4] == p1c4[-4] == p1c5[-4] == "b":
            if p1c1[0:3] == numlist[-index] and p1c2[0:3] == numlist[-1 - index] and p1c3[0:3] == numlist[-2 - index] and p1c4[0:3] == numlist[-3 - index] and p1c5[0:3] == numlist[-4 - index]:
                player1win = True
        if p2c1[-4] == p2c2[-4] == p2c3[-4] == p2c4[-4] == p2c5[-4] == "e" or p2c1[-4] == p2c2[-4] == p2c3[-4] == p2c4[-4] == p2c5[-4] == "t" or p2c1[-4] == p2c2[-4] == p2c3[-4] == p2c4[-4] == p2c5[-4] == "d" or p2c1[-4] == p2c2[-4] == p2c3[-4] == p2c4[-4] == p2c5[-4] == "b":
            if p2c1[0:3] == numlist[-index] and p2c2[0:3] == numlist[-1 - index] and p2c3[0:3] == numlist[-2 - index] and p2c4[0:3] == numlist[-3 - index] and p2c5[0:3] == numlist[-4 - index]:
                player2win = True
        if player1win == True or player2win == True:
            break
    if player1win == True and player2win == True:
        HighHighCard()

def FourOfAKind():
    global player1win, player2win
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p2c1 = p2sorted[0]
    p2c2 = p2sorted[1]
    p2c3 = p2sorted[2]
    p2c4 = p2sorted[3]
    p2c5 = p2sorted[4]
    p1c1 = p1c1[0:3]
    p1c2 = p1c2[0:3]
    p1c3 = p1c3[0:3]
    p1c4 = p1c4[0:3]
    p1c5 = p1c5[0:3]
    p2c1 = p2c1[0:3]
    p2c2 = p2c2[0:3]
    p2c3 = p2c3[0:3]
    p2c4 = p2c4[0:3]
    p2c5 = p2c5[0:3]
    numlist = ["Ace", "Kin", "Que", "Jac", "Ten", "Nin", "Eig", "Sev", "Six", "Fiv", "Fou", "Thr", "Two"]
    for index in range(len(numlist)):
        if p1c1 == numlist[index] and p1c2 == numlist[index] and p1c3 == numlist[index] and p1c4 == numlist[index] or p1c2 == numlist[index] and p1c3 == numlist[index] and p1c4 == numlist[index] and p1c5 == numlist[index]:
            player1win = True
        if p2c1 == numlist[index] and p2c2 == numlist[index] and p2c3 == numlist[index] and p2c4 == numlist[index] or p2c2 == numlist[index] and p2c3 == numlist[index] and p2c4 == numlist[index] and p2c5 == numlist[index]:
            player2win = True
        if player1win == True or player2win == True:
            break

    if player1win == True and player2win == True:
        HighHighCard()

def FullHouse():
    global player1win, player2win
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p2c1 = p2sorted[0]
    p2c2 = p2sorted[1]
    p2c3 = p2sorted[2]
    p2c4 = p2sorted[3]
    p2c5 = p2sorted[4]
    p1c1 = p1c1[0:3]
    p1c2 = p1c2[0:3]
    p1c3 = p1c3[0:3]
    p1c4 = p1c4[0:3]
    p1c5 = p1c5[0:3]
    p2c1 = p2c1[0:3]
    p2c2 = p2c2[0:3]
    p2c3 = p2c3[0:3]
    p2c4 = p2c4[0:3]
    p2c5 = p2c5[0:3]
    numlist = ["Ace", "Kin", "Que", "Jac", "Ten", "Nin", "Eig", "Sev", "Six", "Fiv", "Fou", "Thr", "Two"]
    for index in range(len(numlist)):
        if (p1c1 == numlist[index] and p1c2 == numlist[index] and p1c3 == numlist[index] and p1c4 == p1c5) or (p1c1 == p1c2 and p1c3 == numlist[index] and p1c4 == numlist[index] and p1c5 == numlist[index]):
            player1win = True
        if (p2c1 == numlist[index] and p2c2 == numlist[index] and p2c3 == numlist[index] and p2c4 == p2c5) or (p2c1 == p2c2 and p1c3 == numlist[index] and p1c4 == numlist[index] and p1c5 == numlist[index]):
            player2win = True
        if player1win == True or player2win == True:
            break

    if player1win == True and player2win == True:
        HighHighCard()

def Flush():
    global player1win, player2win
    samesuitp1 = False
    samesuitp2 = False
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p2c1 = p2sorted[0]
    p2c2 = p2sorted[1]
    p2c3 = p2sorted[2]
    p2c4 = p2sorted[3]
    p2c5 = p2sorted[4]
    numlist = ["Ace", "Kin", "Que", "Jac", "Ten", "Nin", "Eig", "Sev", "Six", "Fiv", "Fou", "Thr", "Two"]
    if (p1c1[-4] == p1c2[-4] == p1c3[-4] == p1c4[-4] == p1c5[-4] == "e") or (p1c1[-4] == p1c2[-4] == p1c3[-4] == p1c4[-4] == p1c5[-4] == "t") or (p1c1[-4] == p1c2[-4] == p1c3[-4] == p1c4[-4] == p1c5[-4] == "d") or (p1c1[-4] == p1c2[-4] == p1c3[-4] == p1c4[-4] == p1c5[-4] == "b"):
        samesuitp1 = True
    if (p2c1[-4] == p2c2[-4] == p2c3[-4] == p2c4[-4] == p2c5[-4] == "e") or (p2c1[-4] == p2c2[-4] == p2c3[-4] == p2c4[-4] == p2c5[-4] == "t") or (p2c1[-4] == p2c2[-4] == p2c3[-4] == p2c4[-4] == p2c5[-4] == "d") or (p2c1[-4] == p2c2[-4] == p2c3[-4] == p2c4[-4] == p2c5[-4] == "b"):
        samesuitp2 = True
    for index in range(len(numlist)):
        if samesuitp1 == True:
            if p1c1[0:3] == numlist[index] or p1c2[0:3] == numlist[index] or p1c3[0:3] == numlist[index] or p1c4[0:3] == numlist[index] or p1c5[0:3] == numlist[index]:
                player1win = True
        if samesuitp2 == True:        
            if p2c1[0:3] == numlist[index] or p2c2[0:3] == numlist[index] or p2c3[0:3] == numlist[index] or p2c4[0:3] == numlist[index] or p2c5[0:3] == numlist[index]:
                player2win = True
        if player1win == True or player2win == True:
            break

    if player1win == True and player2win == True:
        HighHighCard()

def Straight():
    global player1win, player2win
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p2c1 = p2sorted[0]
    p2c2 = p2sorted[1]
    p2c3 = p2sorted[2]
    p2c4 = p2sorted[3]
    p2c5 = p2sorted[4]
    p1c1 = p1c1[0:3]
    p1c2 = p1c2[0:3]
    p1c3 = p1c3[0:3]
    p1c4 = p1c4[0:3]
    p1c5 = p1c5[0:3]
    p2c1 = p2c1[0:3]
    p2c2 = p2c2[0:3]
    p2c3 = p2c3[0:3]
    p2c4 = p2c4[0:3]
    p2c5 = p2c5[0:3]
    numlist = ["Ace", "Two", "Thr", "Fou", "Fiv", "Six", "Sev", "Eig", "Nin", "Ten", "Jac", "Que", "Kin"]
    for index in range(10):
        if p1c1 == numlist[-index] and p1c2 == numlist[-1 -index] and p1c3 == numlist[-2 -index] and p1c4 == numlist[-3 -index] and p1c5 == numlist[-4 -index]:
            player1win = True
        if p2c1 == numlist[-index] and p2c2 == numlist[-1 -index] and p2c3 == numlist[-2 -index] and p2c4 == numlist[-3 -index] and p2c5 == numlist[-4 -index]:
            player2win = True
        if player1win == True or player2win == True:
            break
    if player1win == True and player2win == True:
        HighHighCard()

def ThreeOfAKind():
    global player1win, player2win
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p2c1 = p2sorted[0]
    p2c2 = p2sorted[1]
    p2c3 = p2sorted[2]
    p2c4 = p2sorted[3]
    p2c5 = p2sorted[4]
    p1c1 = p1c1[0:3]
    p1c2 = p1c2[0:3]
    p1c3 = p1c3[0:3]
    p1c4 = p1c4[0:3]
    p1c5 = p1c5[0:3]
    p2c1 = p2c1[0:3]
    p2c2 = p2c2[0:3]
    p2c3 = p2c3[0:3]
    p2c4 = p2c4[0:3]
    p2c5 = p2c5[0:3]
    numlist = ["Ace", "Kin", "Que", "Jac", "Ten", "Nin", "Eig", "Sev", "Six", "Fiv", "Fou", "Thr", "Two"]
    for index in range(len(numlist)):
        if (p1c1 == numlist[index] and p1c2 == numlist[index] and p1c3 == numlist[index]) or (p1c2 == numlist[index] and p1c3 == numlist[index] and p1c4 == numlist[index]) or (p1c3 == numlist[index] and p1c4 == numlist[index] and p1c5 == numlist[index]):
            player1win = True
        if (p2c1 == numlist[index] and p2c2 == numlist[index] and p2c3 == numlist[index]) or (p2c2 == numlist[index] and p2c3 == numlist[index] and p2c4 == numlist[index]) or (p2c3 == numlist[index] and p2c4 == numlist[index] and p2c5 == numlist[index]):
            player2win = True
        if player1win == True or player2win == True:
            break
    if player1win == True and player2win == True:
        HighHighCard()

def TwoPair():
    global player1win, player2win
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p2c1 = p2sorted[0]
    p2c2 = p2sorted[1]
    p2c3 = p2sorted[2]
    p2c4 = p2sorted[3]
    p2c5 = p2sorted[4]
    p1c1 = p1c1[0:3]
    p1c2 = p1c2[0:3]
    p1c3 = p1c3[0:3]
    p1c4 = p1c4[0:3]
    p1c5 = p1c5[0:3]
    p2c1 = p2c1[0:3]
    p2c2 = p2c2[0:3]
    p2c3 = p2c3[0:3]
    p2c4 = p2c4[0:3]
    p2c5 = p2c5[0:3]
    numlist = ["Ace", "Kin", "Que", "Jac", "Ten", "Nin", "Eig", "Sev", "Six", "Fiv", "Fou", "Thr", "Two"]
    for index in range(len(numlist)):
        if (p1c1 == numlist[index] and p1c2 == numlist[index] and (p1c3 == p1c4 or p1c4 == p1c5)) or (p1c2 == numlist[index] and p1c3 == numlist[index] and p1c4 == p1c5) or (p1c3 == numlist[index] and p1c4 == numlist[index] and p1c1 == p1c2) or (p1c4 == numlist[index] and p1c5 == numlist[index] and (p1c1 == p1c2 or p1c2 == p1c3)):
            player1win = True
        if (p2c1 == numlist[index] and p2c2 == numlist[index] and (p2c3 == p2c4 or p2c4 == p2c5)) or (p2c2 == numlist[index] and p2c3 == numlist[index] and p2c4 == p2c5) or (p2c3 == numlist[index] and p2c4 == numlist[index] and p2c1 == p2c2) or (p2c4 == numlist[index] and p2c5 == numlist[index] and (p2c1 == p2c2 or p2c2 == p2c3)):
            player2win = True
        if player1win == True or player2win == True:
            break
    if player1win == True and player2win == True:
        PairHigh()

def PairHigh():
    global player1win, player2win
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p2c1 = p2sorted[0]
    p2c2 = p2sorted[1]
    p2c3 = p2sorted[2]
    p2c4 = p2sorted[3]
    p2c5 = p2sorted[4]
    p1c1 = p1c1[0:3]
    p1c2 = p1c2[0:3]
    p1c3 = p1c3[0:3]
    p1c4 = p1c4[0:3]
    p1c5 = p1c5[0:3]
    p2c1 = p2c1[0:3]
    p2c2 = p2c2[0:3]
    p2c3 = p2c3[0:3]
    p2c4 = p2c4[0:3]
    p2c5 = p2c5[0:3]
    First = False
    numlist = ["Ace", "Kin", "Que", "Jac", "Ten", "Nin", "Eig", "Sev", "Six", "Fiv", "Fou", "Thr", "Two"]
    for index in range(len(numlist)):
        player1win = False
        player2win = False
        if p1c1 == p1c2 == numlist[index] or p1c2 == p1c3 == numlist[index] or p1c3 == p1c4 == numlist[index] or p1c4 == p1c5 == numlist[index]:
            player1win = True
        if p2c1 == p2c2 == numlist[index] or p2c2 == p2c3 == numlist[index] or p2c3 == p2c4 == numlist[index] or p2c4 == p2c5 == numlist[index]:
            player2win = True
        if player1win == True and player2win == False:
            break
        if player1win == False and player2win == True:
            break
        if player1win == True and player2win == True and First == True:
            HighHighCard()
        if player1win == True and player2win == True:
            First = True 

def HighHighCard():
    global player1win, player2win
    player1win = False
    player2win = False
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p2c1 = p2sorted[0]
    p2c2 = p2sorted[1]
    p2c3 = p2sorted[2]
    p2c4 = p2sorted[3]
    p2c5 = p2sorted[4]
    p1c1 = p1c1[0:3]
    p1c2 = p1c2[0:3]
    p1c3 = p1c3[0:3]
    p1c4 = p1c4[0:3]
    p1c5 = p1c5[0:3]
    p2c1 = p2c1[0:3]
    p2c2 = p2c2[0:3]
    p2c3 = p2c3[0:3]
    p2c4 = p2c4[0:3]
    p2c5 = p2c5[0:3]
    First = False
    Second = False
    Third = False
    Fourth = False
    numlist = ["Ace", "Kin", "Que", "Jac", "Ten", "Nin", "Eig", "Sev", "Six", "Fiv", "Fou", "Thr", "Two"]
    for index in range(len(numlist)):
        player1win = False
        player2win = False
        if p1c1 == numlist[index] or p1c2 == numlist[index] or p1c3 == numlist[index] or p1c4 == numlist[index] or p1c5 == numlist[index]:
            player1win = True
        if p2c1 == numlist[index] or p2c2 == numlist[index] or p2c3 == numlist[index] or p2c4 == numlist[index] or p2c5 == numlist[index]:
            player2win = True
        if player1win == True and player2win == False:
            break
        if player1win == False and player2win == True:
            break
        if player1win == True or player2win == True and First == False:
            First = True
        elif player1win == True or player2win == True and First == True and Second == False:
            Second = True
        elif player1win == True or player2win == True and First == True and Second == True and Third == False:
            Third = True
        elif player1win == True or player2win == True and First == True and Second == True and Third == True and Fourth == False:
            Fourth = True
        elif player1win == True or player2win == True and First == True and Second == True and Third == True and Fourth == True:
            break

def DecideWinner():
    #This picks the winner(s) and does stuff with the pot
    global p1money, p2money, pot
    if player1win == True and player2win == True:
        print("You split the pot")
        pot = pot/2
        p1money = p1money + pot
        p2money = p2money + pot
        pot = 0
    elif player1win == True:
        print("Player 1 gets the pot")
        p1money = p1money + pot
        pot = 0
    elif player2win == True:
        print("Player 2 gets the pot")
        p2money = p2money + pot
        pot = 0

def Picking_Winner():
    #This funciton goes through the hands you can have in poker until someone is a winner
    RoyalFlush()
    if player1win == False and player2win == False:
        StraightFlush()
    if player1win == False and player2win == False:
        FourOfAKind()
    if player1win == False and player2win == False:
        FullHouse()
    if player1win == False and player2win == False:
        Flush()
    if player1win == False and player2win == False:
        Straight()
    if player1win == False and player2win == False:
        ThreeOfAKind()
    if player1win == False and player2win == False:
        TwoPair()
    if player1win == False and player2win == False:
        PairHigh()
    if player1win == False and player2win == False:
        HighHighCard()

def Start_Game():
    #This adds cards to the player's hands and the pot
    cards = 0
    while cards < 2:
        card = shuffledDeck20[0]
        p1.append(card)
        shuffledDeck20.remove(card)
        card = shuffledDeck20[0]
        p2.append(card)
        shuffledDeck20.remove(card)
        cards = cards + 1
    for index in range(3):
        card = shuffledDeck20[0]
        TableCards.append(card)
        shuffledDeck20.remove(card)

def CardAppend(bet1, bet2, bet3):
    #Validates the cards that you picked
    global TableCards, p1, p2
    bet11 = False
    bet12 = False
    bet13 = False
    bet21 = False
    bet22 = False
    bet23 = False
    while True:
        while True:
            bet11 = False
            bet12 = False
            bet13 = False
            bet21 = False
            bet22 = False
            bet23 = False
            if bet1.strip('-').isnumeric():
                if bet2.strip('-').isnumeric():
                    if bet3.strip('-').isnumeric():
                        bet1 = int(bet1)
                        bet2 = int(bet2)
                        bet3 = int(bet3)
                        if 1 <= bet1 <= 5:
                            bet11 = True
                        else:
                            bet1 = input("Please select a number between 1 and 5 for your first card")
                            bet2 = str(bet2)
                            bet3 = str(bet3)
                        if 1 <= bet2 <= 5:
                            bet12 = True
                        else:
                            bet2 = input("Please select a number between 1 and 5 for your second card")
                            bet1 = str(bet1)
                            bet3 = str(bet3)
                        if 1 <= bet3 <= 5:
                            bet13 = True
                        else:
                            bet3 = input("Please select a number between 1 and 5 for your final card")
                            bet2 = str(bet2)
                            bet1 = str(bet1)
                    else:
                        bet3 = input("Please type a numberical number for your final card")
                else:
                    bet2 = input("Please type a numerical number for your second card")
            else:
                bet1 = input("Please type a numerical number for your first card")
            if bet11 == True and bet12 == True and bet13 == True:
                break


        if bet11 == True and bet12 == True and bet13 == True and bet21 == False:
            if bet1 != bet2 and bet1 != bet3:
                bet21 = True
            else:
                print("These are your table cards", TableCards)
                bet1 = input("Please only pick a card once")
        if bet11 == True and bet12 == True and bet13 == True and bet22 == False:
            if bet2 != bet1 and bet2 != bet3:
                bet22 = True
            else:
                print("These are your table cards", TableCards)
                bet2 = input("Please only pick a card once")
        if bet11 == True and bet12 == True and bet13 == True and bet23 == False:
            if bet3 != bet2 and bet3 != bet1:
                bet23 = True
            else:
                print("These are your table cards", TableCards)
                bet3 = input("Please only pick a card once")
        if bet21 == True and bet22 == True and bet23 == True:
            print("You picked the cards", TableCards[bet1 -1], TableCards[bet2 -1], TableCards[bet3 -1])
            likegoodCards = input("Do you like the cards you picked? ")
            if likegoodCards == "yes":
                return[bet1, bet2, bet3]
            else:
                print("Please pick 3 table cards you like")
                bet1 = input("Please pick your first card")
                bet2 = input("Please pick your second card")
                bet3 = input("Please pick your third card")
        else:
            bet1 = str(bet1)
            bet2 = str(bet2)
            bet3 = str(bet3)

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
    global p1money, p2money, pot, p1allin, p2allin, p1fold, p2fold, p1, p2, TableCards, shuffledDeck20
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
        TableCards.append(shuffledDeck20[0])
        shuffledDeck20.remove(shuffledDeck20[0])
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
        TableCards.append(shuffledDeck20[0])
        shuffledDeck20.remove(shuffledDeck20[0])
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

    if p1fold == False and p2fold == False and p1allin == False and p2allin == False:
        print("When picking your table cards to make your final hand, there can be no repeats in each player's hand, but both players can pick the same card to add to their hand")
        print("These are your table cards,", "".join(TableCards))
        p1t = input("player 1, pick one table card(number)")
        p1t2 = input("player 1, pick another table card(number)")
        p1t3 = input("player 1, pick your final card(number)")
        p1t, p1t2, p1t3, = CardAppend(p1t, p1t2, p1t3)
        p1.append(TableCards[p1t - 1])
        p1.append(TableCards[p1t2 - 1])
        p1.append(TableCards[p1t3 - 1])
        print("When picking your table cards to make your final hand, there can be no repeats in each player's hand, but both players can pick the same card to add to their hand")
        print("These are your table cards,", "".join(TableCards))
        p2t = input("player 2, pick one table card(number)")
        p2t2 = input("player 2, pick another table card(number)")
        p2t3 = input("player 2, pick your final card(number)")
        p2t, p2t2, p2t3, = CardAppend(p2t, p2t2, p2t3)
        p2.append(TableCards[p2t - 1])
        p2.append(TableCards[p2t2 - 1])
        p2.append(TableCards[p2t3 - 1])

    if p1allin == True or p2allin == True:
        tablelength = len(TableCards)
        while tablelength < 5:
            card = shuffledDeck20[0]
            TableCards.append(card)
            shuffledDeck20.remove(card)
            tablelength = len(TableCards)
        print("When picking your table cards to make your final hand, there can be no repeats in each player's hand, but both players can pick the same card to add to their hand")
        print("These are your table cards,", "".join(TableCards))
        p1t = input("player 1, pick one table card(number)")
        p1t2 = input("player 1, pick another table card(number)")
        p1t3 = input("player 1, pick your final card(number)")
        p1t, p1t2, p1t3, = CardAppend(p1t, p1t2, p1t3)
        p1.append(TableCards[p1t - 1])
        p1.append(TableCards[p1t2 - 1])
        p1.append(TableCards[p1t3 - 1])
        print("\n" * 20)
        print("When picking your table cards to make your final hand, there can be no repeats in each player's hand, but both players can pick the same card to add to their hand")
        print("These are your table cards,", "".join(TableCards))
        p2t = input("player 2, pick one table card(number)")
        p2t2 = input("player 2, pick another table card(number)")
        p2t3 = input("player 2, pick your final card(number)")
        p2t, p2t2, p2t3, = CardAppend(p2t, p2t2, p2t3)
        p2.append(TableCards[p2t - 1])
        p2.append(TableCards[p2t2 - 1])
        p2.append(TableCards[p2t3 - 1])

while True:
    #Runs the actual game. Decides if it runs again
    ShuffleDeck1()
    Start_Game()
    TheBetting()
    if p1fold == False and p2fold == False:
        SortDeck()
        Picking_Winner()
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
        p1sorted = []
        p2sorted = []
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
        shuffledDeck11 = []
        shuffledDeck12 = []
        shuffledDeck13 = []
        shuffledDeck14 = []
        shuffledDeck15 = []
        shuffledDeck16 = []
        shuffledDeck17 = []
        shuffledDeck18 = []
        shuffledDeck19 = []
        shuffledDeck20 = []
        lencards = len(deckCardsList)
        player1win = False
        player2win = False
        TableCards = []

    elif p1_again == "no" or p2_again == "no":
        break
    else:
        p1_again = input("Would player 1 like to play again?")
        p2_again = input("Would player 2 like to play again?")