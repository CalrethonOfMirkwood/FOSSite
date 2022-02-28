# War Game
#
# Cards are represented in base 13
#
# Clovers : 0(0-c)
# Diamonds: 1(0-c)
# Hearts  : 2(0-c)
# Spades  : 3(0-c)
#
# 0-8 -> 2-10
# 9 -> Jack
# 10 -> Queen
# 11 -> King
# 12 -> Ace
#
# Each card is represented as base 13 number.
# 5 represents the Seven of Clovers (0*13+5)
# 23 represents the Queen of Diamonds (13+10)
# 46 represents the Nine of Spades (3*13+7)
# 26 represents the Ace of Hearts (2*13+0)
#
import random
import pygame

suits = ["Clover", "Diamond", "Heart", "Spade"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
state = 0
cardstosubmit = 0
war = False
ANIFRAMES = 50
playerdeck_animation = 0
computerdeck_animation = 0

def NumToCard(id):
    id = id%52
    return suits[int(id/13)]+" "+ranks[id%13]

maindeck = []
playerdeck_main = []
playerdeck_acquired = []
playerdeck_played = []
computerdeck_main = []
computerdeck_acquired = []
computerdeck_played = []

pygame.init()
w = 1000
h = 800
screen = pygame.display.set_mode((w,h))
cards = pygame.image.load("cards.png")
background = pygame.image.load("table.jpg")
background = pygame.transform.scale(background, (w, h))
backgroundwar = pygame.image.load("wartable.jpg")
backgroundwar = pygame.transform.scale(backgroundwar, (w, h))
cardback = pygame.image.load("cardback.png")
cardback = pygame.transform.scale(cardback, (74, 115))

def DrawCards(id, x, y):
    if id > 51:
        screen.blit(cardback, (x,y))
    else:
        if (id+1)%13 == 0:
            id-=12
        else:
            id+=1
                
        cropx = (id%13)*73.85
        cropy = int(id/13)*115
        screen.blit(cards, (x,y,74,115), (cropx, cropy, 74, 115))

def DrawTable():
    global playerdeck_animation
    global computerdeck_animation
    
    if war:
        screen.blit(backgroundwar, (0,0))
    else:
        screen.blit(background, (0,0))
    for i in range(len(maindeck)):
        DrawCards(maindeck[i], w*(0.5-len(maindeck)*0.006)+i*w*0.012, h*0.4)

    for i in range(len(playerdeck_main)):
        DrawCards(52, w*0.7+i*w*0.005, h*0.75)

    for i in range(len(playerdeck_acquired)):
        DrawCards(playerdeck_acquired[i], w*0.1+i*w*0.012, h*0.75)

    for i in range(len(playerdeck_played)):
        x = w*(0.5-len(playerdeck_played)*0.006)+i*w*0.012
        y = h*0.55
        if i == len(playerdeck_played)-1 and playerdeck_animation > 0:
            x = x * (ANIFRAMES - playerdeck_animation) / ANIFRAMES + (w*0.7+(len(playerdeck_main)+1)*w*0.005) * playerdeck_animation / ANIFRAMES
            y = y * (ANIFRAMES - playerdeck_animation) / ANIFRAMES + (h*0.75) * playerdeck_animation / ANIFRAMES
            playerdeck_animation -= 1
        DrawCards(playerdeck_played[i], x, y)

    for i in range(len(computerdeck_main)):
        DrawCards(52, w*0.2+i*w*0.005, h*0.2)

    for i in range(len(computerdeck_acquired)):
        DrawCards(computerdeck_acquired[i], w*0.5+i*w*0.012, h*0.2)

    for i in range(len(computerdeck_played)):
        x = w*(0.5-len(computerdeck_played)*0.006)+i*w*0.012
        y = h*0.38
        if i == len(computerdeck_played)-1 and computerdeck_animation > 0:
            x = x * (ANIFRAMES - computerdeck_animation) / ANIFRAMES + (w*0.2+(len(computerdeck_main)+1)*w*0.005) * computerdeck_animation / ANIFRAMES
            y = y * (ANIFRAMES - computerdeck_animation) / ANIFRAMES + (h*0.2) * computerdeck_animation / ANIFRAMES
            computerdeck_animation -= 1
        DrawCards(computerdeck_played[i], x, y)

###### Main

for i in range(0,52):
    maindeck.append(i)

prev_state = -1
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            state+=1
            print("New state = %d    prev state = %d"%(state, prev_state))
        if event.type == pygame.QUIT:
            run = False

    if prev_state != state:
        if state == 0:
            print("initial deck:", maindeck, "\n")
            print("Press any key to shuffle...")
        
        if state == 1:
            random.shuffle(maindeck)
            print("shuffled deck:", maindeck, "\n")
            print("Press any key to distribute cards...")

        if state == 2:
            for i in range(0,26):
                playerdeck_main.append(maindeck.pop())
                computerdeck_main.append(maindeck.pop())

            print("my deck:", playerdeck_main)
            print("computer deck:", computerdeck_main)

            print("my deck in human language")
            for x in playerdeck_main:
                print("[%d][%s] "%(x, NumToCard(x)))

            print("Press any key to start game...")

        if state == 3:

            if len(playerdeck_main)>0 and len(computerdeck_main)>0:
                playerdeck_played.append(playerdeck_main.pop()+cardstosubmit*52)
                computerdeck_played.append(computerdeck_main.pop()+cardstosubmit*52)
                playerdeck_animation = ANIFRAMES
                computerdeck_animation = ANIFRAMES
                print("played cards. Me:[%s]  Computer:[%s]"%(NumToCard(playerdeck_played[-1]), NumToCard(computerdeck_played[-1])))

            if cardstosubmit > 0:
                cardstosubmit -= 1
                state = 2

        if state == 4:
            if playerdeck_played[-1]%13 > computerdeck_played[-1]%13:
                print("YOU WON!")
                while len(playerdeck_played)>0 or len(computerdeck_played)>0:
                    playerdeck_acquired.append(playerdeck_played.pop(0))
                    playerdeck_acquired.append(computerdeck_played.pop(0))
                war = False
            elif playerdeck_played[-1]%13 < computerdeck_played[-1]%13:
                print("COMPUTER WON!")
                while len(playerdeck_played) or len(computerdeck_played):
                    computerdeck_acquired.append(playerdeck_played.pop(0))
                    computerdeck_acquired.append(computerdeck_played.pop(0))
                war = False
            else:
                print("WAR!")
                cardstosubmit = 1
                war = True
            state = 2

# move aquired cards to player and computer's main deck if main deck is empty
        if len(playerdeck_main) == 0 and len(playerdeck_acquired) > 0:
            size=len(playerdeck_acquired)
            for i in range(size):
                playerdeck_main.insert(0,playerdeck_acquired[i]%52)
            playerdeck_acquired.clear()

        if len(computerdeck_main) == 0 and len(computerdeck_acquired) > 0:
            size=len(computerdeck_acquired)
            for i in range(size):
                computerdeck_main.insert(0,computerdeck_acquired[i]%52)
            computerdeck_acquired.clear()

# current status
        print("my       deck     :", playerdeck_main)
        print("my       acquired :", playerdeck_acquired)
        print("my       played:", playerdeck_played)
        print("computer deck     :", computerdeck_main)
        print("computer acquired :", computerdeck_acquired)
        print("computer played:", computerdeck_played)

        prev_state = state

    DrawTable()
    pygame.display.update()

    if state == 3:
        if len(playerdeck_main) > 0 and len(computerdeck_main) == 0:
            print("YOU WON!! Game over!")
            run = False
        elif len(playerdeck_main) == 0 and len(computerdeck_main) > 0:
            print("COMPUTER WON!! Game over!")
            run = False
        elif len(playerdeck_main) == 0 and len(computerdeck_main) == 0:
            # it probably won't happen in 10 years of playtime but its possible that the player and the computers's decks both have the exact same order of card values
            print("Tie! Game over!")
            run = False

pygame.quit()
