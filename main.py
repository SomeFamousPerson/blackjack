import random
cardValue = 0
bust = False
aceCount = 0
def turn():
    global aceCount
    global cardValue
    global bust
    if bust == False:
        choice = input("Draw or hold? ")
        if choice == ("draw"):
            drawCard()
            #card valuehold
            cardValue = cardValue+intDraw
            if cardValue > 21:
                #change aces to ones
                if aceCount > 0:
                  aceCount = aceCount-1
                  cardValue = cardValue-10
                #go bust
                else:
                  print("Value: ",cardValue)
                  print("Bust")
                  bust = True
            else:
                print(draw)
                print("Value:",cardValue)
        elif choice == ("hold"):
            print("Value: ",cardValue)
deck = ["A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥","A♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦","A♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣","A♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠"]
def drawCard():
    #grab randon card and remove it from deck
    global draw
    global aceCount
    draw = (random.choice(deck))
    deck.remove(draw)
    print(draw)
    #count Aces
    if draw == "A♥" or "A♦" or "A♣" or "A♠":
      aceCount = aceCount+1
    #convert to INT value
    draw=(draw.replace("♥", ""))
    draw=(draw.replace("♦", ""))
    draw=(draw.replace("♣", ""))
    draw=(draw.replace("♠", ""))
    draw=(draw.replace("J", "10"))
    draw=(draw.replace("Q", "10"))
    draw=(draw.replace("K", "10"))
    draw=(draw.replace("A", "11"))
    global intDraw
    intDraw = int(draw)
drawCard()
cardValue = (intDraw)
drawCard()
cardValue = (cardValue+intDraw)
print("Value: ",cardValue)
#player move
global choice 
choice = ""
while choice != ("hold") and bust == False:
    turn()
#computer turn