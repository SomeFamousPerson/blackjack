import random
cardValue = 0
bust = False
aceCount = 0
computerCardValue = 0
computerAceCount = 0
intDraw = 0
choice = ""
draw = 0
def turn():
    global aceCount
    global cardValue
    global bust
    global deck
    global choice 
    if bust == False:
        choice = input("Draw or hold? ")
        if choice == ("hold"):
            print("Value: ",cardValue)
        elif choice == ("draw"):
            drawCard()
            #card value
            cardValue = cardValue+intDraw
            if cardValue > 21:
                #change aces to ones
                if aceCount > 0:
                  aceCount -= 1
                  cardValue -= 10
                  print("Value: ",cardValue)
                else:
                #go bust
                  print("Value: ",cardValue)
                  print("Bust")
                  bust = True
            else:
                print("Value:",cardValue)
        else:
          print("Invalid input")
deck = ["A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥","A♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦","A♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣","A♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠"]
def drawCard():
    #grab randon card and remove it from deck
    global draw
    global aceCount
    global intDraw
    draw = (random.choice(deck))
    deck.remove(draw)
    print(draw)
    #count Aces
    if draw == "A♥" or draw == "A♦" or draw == "A♣" or draw == "A♠":
      aceCount += 1
    #convert to INT value
    draw=(draw.replace("♥", ""))
    draw=(draw.replace("♦", ""))
    draw=(draw.replace("♣", ""))
    draw=(draw.replace("♠", ""))
    draw=(draw.replace("J", "10"))
    draw=(draw.replace("Q", "10"))
    draw=(draw.replace("K", "10"))
    draw=(draw.replace("A", "11"))
    intDraw = int(draw)
drawCard()
cardValue = (intDraw)
drawCard()
cardValue = (cardValue+intDraw)
print("Value: ",cardValue)
#player move
while choice != ("hold") and bust == False:
    turn()
#computer turn
if bust == False:
  print("Computer turn")
  def computerTurn():
    global draw
    global computerAceCount
    global intDraw
    global computerCardValue
    draw = (random.choice(deck))
    deck.remove(draw)
    print(draw)
    #count Aces
    if draw == "A♥" or draw == "A♦" or draw == "A♣" or draw == "A♠":
       computerAceCount = computerAceCount+1
    #convert to INT value
    draw=(draw.replace("♥", ""))
    draw=(draw.replace("♦", ""))
    draw=(draw.replace("♣", ""))
    draw=(draw.replace("♠", ""))
    draw=(draw.replace("J", "10"))
    draw=(draw.replace("Q", "10"))
    draw=(draw.replace("K", "10"))
    draw=(draw.replace("A", "11"))
    intDraw = int(draw)
    computerCardValue = computerCardValue+intDraw
    if computerCardValue > 21 and computerAceCount > 0:
      computerAceCount = computerAceCount-1
      computerCardValue = computerCardValue-10
  computerTurn()
  computerTurn()
  print("Value:",computerCardValue)
  while computerCardValue <= (16):
    computerTurn()
    print("Value: ",computerCardValue)
  if computerCardValue > 21:
    print("Bust")
    print("You win")
  elif cardValue > computerCardValue:
    print("Player wins")
  elif cardValue == computerCardValue:
    print("Draw")
  elif cardValue < computerCardValue:
    print("Computer wins")
  else:
    print("Something went wrong")
else:
  print("Computer wins")
