import random
from graphics import *
def main():
    START = True
    GAME1 = False
    GAME2 = False
    GAME3 = False
    while START:
        Menu = GraphWin("Menu",850,600)
        Menu.setBackground('light blue')
        MenuPanel = Rectangle(Point(50,50), Point(800,550))
        MenuPanel.setFill('light green')
        MenuPanel.draw(Menu)
        MenuMessage = Text(Point(425,150), "MAIN MENU")
        MenuMessage.setTextColor("purple")
        MenuMessage.setStyle("bold")
        MenuMessage.setSize(30)
        MenuMessage.draw(Menu)
        MenuText = Text(Point(425,300),"Please select which game you would like to play")
        MenuText.setTextColor("blue")
        MenuText.setSize(15)
        MenuText.setStyle('bold')
        MenuText.draw(Menu)
        MenuBox1 = Rectangle(Point(150, 500),Point(300,400))
        MenuBox1.setFill('white')
        MenuBox1.draw(Menu)
        MenuBoxText1 = Text(Point(225,450),"Game 1")
        MenuBoxText1.setSize(20)
        MenuBoxText1.setTextColor('orange')
        MenuBoxText1.setStyle('bold')
        MenuBoxText1.draw(Menu)
        MenuBoxText1Game = Text(Point(225,375),"Heads or Tails")
        MenuBoxText1Game.setSize(18)
        MenuBoxText1Game.setStyle('bold')
        MenuBoxText1Game.draw(Menu)
        MenuBox2 = Rectangle(Point(350, 500),Point(500,400))
        MenuBox2.setFill('white')
        MenuBox2.draw(Menu)
        MenuBoxText2 = Text(Point(425,450),"Game 2")
        MenuBoxText2.setSize(20)
        MenuBoxText2.setTextColor('pink')
        MenuBoxText2.setStyle('bold')
        MenuBoxText2.draw(Menu)
        MenuBoxText2Game = Text(Point(425,375),"Tic Tac Toe")
        MenuBoxText2Game.setSize(18)
        MenuBoxText2Game.setStyle('bold')
        MenuBoxText2Game.draw(Menu)
        MenuBox3 = Rectangle(Point(550, 500),Point(700,400))
        MenuBox3.setFill('white')
        MenuBox3.draw(Menu)
        MenuBoxText3 = Text(Point(625,450),"Game 3")
        MenuBoxText3.setSize(20)
        MenuBoxText3.setTextColor('green')
        MenuBoxText3.setStyle('bold')
        MenuBoxText3.draw(Menu)
        MenuBoxText3Game = Text(Point(625,375),"TBA")
        MenuBoxText3Game.setSize(18)
        MenuBoxText3Game.setStyle('bold')
        MenuBoxText3Game.draw(Menu)
        QuitBox = Rectangle(Point(650,75),Point(750,175))
        QuitBox.setFill('red')
        QuitBox.draw(Menu)
        QuitBoxText = Text(Point(700,125),"Quit")
        QuitBoxText.setSize(30)
        QuitBoxText.setStyle('bold')
        QuitBoxText.setTextColor('white')
        QuitBoxText.draw(Menu)

        Signature = Text(Point(700,575),"Created by Kit Ma      August 2019")
        Signature.setSize(12)
        Signature.setStyle('bold')
        Signature.draw(Menu)
        while True:
            click = Menu.getMouse()
            x = click.getX()
            y = click.getY()
            if x>=150 and x<=300 and y>=400 and y<=500:
                Menu.close()
                GAME1 = True
                break
            elif x>=350 and x<=500 and y>=400 and y<=500:
                Menu.close()
                GAME2 = True
                break
    ##        if x>=550 and x<=700 and y>=400 and y<500:
    ##            GAME3 = True
            elif x>=650 and x<=750 and y>=75 and y<=175:
                Menu.close()
                START = False
                print("Goodbye")
                break
            else:
                START = True
            

        while GAME1:
            lives = 3
            Game1Screen = GraphWin("Heads or Tails",850,600, autoflush = False)
            Game1Screen.setBackground('light blue')
            GameLayout = Rectangle(Point(50,50), Point(800,550))
            GameLayout.setFill(color_rgb(252,155,99))
            GameLayout.draw(Game1Screen)
            Game1Text = Text(Point(425,100),"Heads or Tails")
            Game1Text.setSize(30)
            Game1Text.setStyle('bold')
            Game1Text.setTextColor("green")
            Game1Text.draw(Game1Screen)
            HeadsButton = Rectangle(Point(100, 500),Point(375,400))
            HeadsButton.setFill('white')
            HeadsButton.draw(Game1Screen)
            HeadsText = Text(Point(230,450),"HEADS")
            HeadsText.setSize(20)
            HeadsText.setStyle('bold')
            HeadsText.setTextColor('blue')
            HeadsText.draw(Game1Screen)
            TailsButton = Rectangle(Point(475, 500),Point(750,400))
            TailsButton.setFill('white')
            TailsButton.draw(Game1Screen)
            TailsText = Text(Point(615,450),"TAILS")
            TailsText.setSize(20)
            TailsText.setStyle('bold')
            TailsText.setTextColor('red')
            TailsText.draw(Game1Screen)
            LivesText = Text(Point(150, 575),"LIVES:")
            LivesText.setSize(20)
            LivesText.setTextColor('purple')
            LivesText.setStyle('bold')
            LivesText.draw(Game1Screen)
            LivesNumberText = Text(Point(220,575),lives)
            LivesNumberText.setStyle('bold')
            LivesNumberText.setTextColor('purple')
            LivesNumberText.setSize(20)
            LivesNumberText.draw(Game1Screen)
            QuitBox = Rectangle(Point(650,75),Point(750,175))
            QuitBox.setFill('red')
            QuitBox.draw(Game1Screen)
            QuitBoxText = Text(Point(700,125),"Quit")
            QuitBoxText.setSize(30)
            QuitBoxText.setStyle('bold')
            QuitBoxText.setTextColor('white')
            QuitBoxText.draw(Game1Screen)
            coin_turn = Image(Point(425,250), "Coin2.gif")
            coin_turn.draw(Game1Screen)
            Round = 1
            RoundText = Text(Point(350,575),"Round:")
            RoundText.setSize(20)
            RoundText.setStyle('bold')
            Roundnum = Text(Point(425,575),Round)
            Roundnum.setSize(20)
            Roundnum.setStyle('bold')
            RoundText.draw(Game1Screen)
            Roundnum.draw(Game1Screen)
            CoinStart = True
            dead = True
            coinflip = 3
            while CoinStart:
                select = random.randint(0,1)
                if lives == 0:
                        gameovertext = Text(Point(450,350),"Game Over, Thank you for playing")
                        gameovertext.setSize(20)
                        gameovertext.setStyle('bold')
                        gameovertext.draw(Game1Screen)
                        click = Game1Screen.getMouse()
                        x = click.getX()
                        y = click.getY()    
                        if x>=650 and x<=750 and y>=75 and y<=175:
                            Game1Screen.close()
                            GAME1 = False
                            break
                        else:
                            select = 3
                click = Game1Screen.getMouse()
                x = click.getX()
                y = click.getY()
                if x>=650 and x<=750 and y>=75 and y<=175:
                    Game1Screen.close()
                    GAME1 = False
                    break
                elif x>=100 and x<=375 and y>=400 and y<=500:
                    coinflip = 0
                    if select == 1:
                        coin_turn.undraw()
                        for i in range(175):
                             coin_turn = Image(Point(425+i,250), "Coin2.gif")
                             coin_turn.draw(Game1Screen)
                             update(50)
                             coin_turn.undraw()
                        coin_turn = Image(Point(425,250), "Coin2.gif")
                        coin_turn.draw(Game1Screen)
                        if coinflip != select:
                            Round = Round + 1
                            Roundnum.undraw()
                            Roundnum = Text(Point(425,575),Round)
                            Roundnum.setSize(20)
                            Roundnum.setStyle('bold')
                            Roundnum.draw(Game1Screen)
                    if select == 0:
                        coin_turn.undraw()
                        for i in range(175):
                             coin_turn = Image(Point(425-i,250), "Coin2.gif")
                             coin_turn.draw(Game1Screen)
                             update(50)
                             coin_turn.undraw()
                        coin_turn = Image(Point(425,250), "Coin2.gif")
                        coin_turn.draw(Game1Screen)
                        if coinflip == select:
                            lives = lives - 1
                            Round = Round + 1
                            LivesNumberText.undraw()
                            LivesNumberText = Text(Point(220,575),lives)
                            LivesNumberText.setSize(20)
                            LivesNumberText.setStyle('bold')
                            LivesNumberText.setTextColor('purple')
                            LivesNumberText.draw(Game1Screen)
                            RoundText.setStyle('bold')
                            Roundnum.undraw()
                            Roundnum = Text(Point(425,575),Round)
                            Roundnum.setSize(20)
                            Roundnum.setStyle('bold')
                            Roundnum.draw(Game1Screen)
                        

    
                elif x>=475 and x<=750 and y>=400 and y<=500:
                    coinflip = 1
                    if select == 0:
                        coin_turn.undraw()
                        for i in range(175):
                             coin_turn = Image(Point(425-i,250), "Coin2.gif")
                             coin_turn.draw(Game1Screen)
                             update(50)
                             coin_turn.undraw()
                        coin_turn = Image(Point(425,250), "Coin2.gif")
                        coin_turn.draw(Game1Screen)
                        if coinflip != select:
                            Round = Round + 1
                            Roundnum.undraw()
                            Roundnum = Text(Point(425,575),Round)
                            Roundnum.setSize(20)
                            Roundnum.setStyle('bold')
                            Roundnum.draw(Game1Screen)
                    if select == 1:
                        coin_turn.undraw()
                        for i in range(175):
                             coin_turn = Image(Point(425+i,250), "Coin2.gif")
                             coin_turn.draw(Game1Screen)
                             update(50)
                             coin_turn.undraw()
                        coin_turn = Image(Point(425,250), "Coin2.gif")
                        coin_turn.draw(Game1Screen)
                        if coinflip == select:
                            lives = lives - 1
                            Round = Round + 1
                            LivesNumberText.undraw()
                            LivesNumberText = Text(Point(220,575),lives)
                            LivesNumberText.setSize(20)
                            LivesNumberText.setStyle('bold')
                            LivesNumberText.setTextColor('purple')
                            LivesNumberText.draw(Game1Screen)
                            Roundnum.undraw()
                            Roundnum = Text(Point(425,575),Round)
                            Roundnum.setSize(20)
                            Roundnum.setStyle('bold')
                            Roundnum.draw(Game1Screen)

                
                else:
                    CoinStart = True

                    

            
            
##        while GAME1:
##            x = ['heads','tails']
##            woah = True
##            cheese = True
##            lives = 3
##            rounds = 1
##            while cheese:
##                print("Do you want to play a game 1?: ")
##                Input = input()
##                if Input.lower() == 'no' or Input.lower() == 'n':
##                    woah = False
##                    cheese = False
##                elif Input.lower() == 'yes' or Input.lower() == 'y':
##                    print("Ok let's play :D")
##                    print("\nThe game we will be playing today is heads or tails")
##                    print("\nYou will have three lives and if you choose the same side as the computer you will lose a life")
##                    print("\nOnce all your lives are gone, it will be GAME OVER")
##                    print("\n.\n.\n.\nLOADED GAME\n")
##                    cheese = False
##                else:
##                    print("Please select the correct input")
##            while woah:
##                if lives == 0:
##                    print("Game over!@!@@#!@#@$!@$!@")
##                    print("Would you like to play again?:")
##                    Input3 = input()
##                    if Input3.lower() == 'y' or Input3.lower() == 'yes':
##                        lives = 3
##                        rounds = 1
##                    elif Input3.lower() == 'n' or Input3.lower() == 'no':
##                        woah = False
##                    else:
##                        print("Input yes or no")
##                else:
##                    print("Round",rounds)
##                    print("Please choose heads or tails:")
##                    Input2 = input()
##                    select = random.randint(0,1)
##                    chosen = x[select]
##                    print(chosen)
##                    if chosen == Input2.lower():
##                        lives = lives - 1
##                        rounds = rounds + 1
##                        print("You have lost a life, you have", lives,"lives left.")
##                    elif chosen != Input2.lower() and Input2.lower() == 'heads' or Input2.lower() == 'tails':
##                        rounds = rounds + 1
##                    else:
##                        print("Please try again with the correct input")
##                        
##            print("\nGoing back to the main menu\n")
##            GAME1 = False

        GameStarting = True

        while GAME2:
            win = GraphWin("Game2",850,600)
            win.setBackground('light blue')
            rbox = Rectangle(Point(300,50), Point(800,550))
            rbox.setFill("white")
            rbox.draw(win)
            lbox = Rectangle(Point(50,50), Point(250,550))
            lbox.setFill('white')
            lbox.draw(win)

            GameTitle = Text(Point(150,75),"TIC TAC TOE")
            GameTitle.setSize(18)
            GameTitle.setStyle('bold')
            GameTitle.setTextColor("Orange")
            GameTitle.draw(win)

            GameRules = Text(Point(150,175), "RULES:")
            GameRules.setSize(15)
            GameRules.setStyle('bold')
            GameRules.setTextColor('Green')
            GameRules.draw(win)

            GameRules2 = Text(Point(150,250),"Click on one of the\nsquares on the right and\nmake sure it's 3 in a row")
            GameRules2.setSize(13)
            GameRules2.setTextColor('Green')
            GameRules2.draw(win)


            RandomSelect = random.randint(0,1)
            #print(RandomSelect,"goes first")
            InitialStart = 5
            if RandomSelect == 0:
                InitialStart = 0
                PlayerOFirst = Text(Point(150,400),"Player O goes first")
                PlayerOFirst.setSize(15)
                PlayerOFirst.setStyle('bold')
                PlayerOFirst.setTextColor('blue')
                PlayerOFirst.draw(win)
            if RandomSelect == 1:
                InitialStart = 1
                PlayerXFirst = Text(Point(150,400),"Player X goes first")
                PlayerXFirst.setSize(15)
                PlayerXFirst.setStyle('bold')
                PlayerXFirst.setTextColor('red')
                PlayerXFirst.draw(win)

            GameBoard = [3]*9

            PlayerXNext = Text(Point(150,400),"It is now\nPlayer X's turn")
            PlayerXNext.setSize(15)
            PlayerXNext.setStyle('bold')
            PlayerXNext.setTextColor('red')

            PlayerONext = Text(Point(150,400),"It is now\nPlayer O's turn")
            PlayerONext.setSize(15)
            PlayerONext.setStyle('bold')
            PlayerONext.setTextColor('blue')

            Yeet = True
            
            while Yeet:
                ExitBox = Rectangle(Point(75,450), Point(225,525))
                ExitBox.setFill("white")
                ExitBox.draw(win)
                CenterExitBox = ExitBox.getCenter()
                ExitBoxText = Text(CenterExitBox, "EXIT")
                ExitBoxText.setSize(20)
                ExitBoxText.setStyle('bold')
                ExitBoxText.setTextColor('black')
                ExitBoxText.draw(win)


##                for i in range(3):
##                    SetupLineHorizontal = Line(Point(350,225 + i*150), Point(750,225+ i*150))
##                    SetupLineHorizontal.draw(win)
##
##                    SetupLineVertical = Line(Point(475 + i*150,100), Point(475 + i*150,500))
##                    SetupLineVertical.draw(win)

                SetupBoxHorizontal1 = Rectangle(Point(370,100), Point(495,225))
                SetupBoxHorizontal2 = Rectangle(Point(495,100), Point(620,225))
                SetupBoxHorizontal3 = Rectangle(Point(620,100),Point(745,225))
                SetupBoxHorizontal4 = Rectangle(Point(370,225), Point(495,350))
                SetupBoxHorizontal5 = Rectangle(Point(495,225),Point(620,350))
                SetupBoxHorizontal6 = Rectangle(Point(620,225),Point(745,350))
                SetupBoxHorizontal7 = Rectangle(Point(370,350), Point(495,475))
                SetupBoxHorizontal8 = Rectangle(Point(495,350),Point(620,475))
                SetupBoxHorizontal9 = Rectangle(Point(620,350),Point(745,475))
                SetupBoxHorizontal1.draw(win)
                SetupBoxHorizontal2.draw(win)
                SetupBoxHorizontal3.draw(win)
                SetupBoxHorizontal4.draw(win)
                SetupBoxHorizontal5.draw(win)
                SetupBoxHorizontal6.draw(win)
                SetupBoxHorizontal7.draw(win)
                SetupBoxHorizontal8.draw(win)
                SetupBoxHorizontal9.draw(win)
                NextStart = 3

                Oops = 0
                if GameStarting == False:
                    click = win.getMouse()
                    x = click.getX()
                    y = click.getY()
                    if x >= 75 and x<=225 and y>=450 and y<=525:
                            win.close()
                            GAME2 = False
                            Yeet = False
                            break

                while GameStarting:

                    #If Player O goes first

                    if RandomSelect == 0 and InitialStart == 0:
                        click = win.getMouse()
                        x = click.getX()
                        y = click.getY()
                        #print(x,y)
                        InitialStart = 3
                        PlayerOFirst.undraw()
                        if Oops == 1:
                            RetryMessageO.undraw()
                            Oops = 0
                        if x >= 75 and x<=225 and y>=450 and y<=525:
                            win.close()
                            GAME2 = False
                            Yeet = False
                            break
                        elif x>=370 and x<=495 and y>=100 and y<=225 and GameBoard[0] == 3:
                            SetupBoxHorizontal1.setFill('blue')
                            GameBoard[0] = 0
                            NextStart = 0
                            PlayerXNext.draw(win)
                        elif x>=495 and x<=620 and y>=100 and y<=225 and GameBoard[1] == 3:
                            SetupBoxHorizontal2.setFill('blue')
                            GameBoard[1] = 0
                            NextStart = 0
                            PlayerXNext.draw(win)
                        elif x>=620 and x<=745 and y>=100 and y<=225 and GameBoard[2] == 3:
                            SetupBoxHorizontal3.setFill('blue')
                            GameBoard[2] = 0
                            NextStart = 0
                            PlayerXNext.draw(win)
                        elif x>=370 and x<=495 and y>=225 and y<=350 and GameBoard[3] == 3:
                            SetupBoxHorizontal4.setFill('blue')
                            GameBoard[3] = 0
                            NextStart = 0
                            PlayerXNext.draw(win)
                        elif x>=495 and x<=620 and y>=225 and y<=350 and GameBoard[4] == 3:
                            SetupBoxHorizontal5.setFill('blue')
                            GameBoard[4] = 0
                            NextStart = 0
                            PlayerXNext.draw(win)
                        elif x>=620 and y<=745 and y>=225 and y<=350 and GameBoard[5] == 3:
                            SetupBoxHorizontal6.setFill('blue')
                            GameBoard[5] = 0
                            NextStart = 0
                            PlayerXNext.draw(win)
                        elif x>=370 and x<=495 and y>=350 and y<=475 and GameBoard[6] == 3:
                            SetupBoxHorizontal7.setFill('blue')
                            GameBoard[6] = 0
                            NextStart = 0
                            PlayerXNext.draw(win)
                        elif x>=495 and x<=620 and y>=350 and y<=475 and GameBoard[7] == 3:
                            SetupBoxHorizontal8.setFill('blue')
                            GameBoard[7] = 0
                            NextStart = 0
                            PlayerXNext.draw(win)
                        elif x>=620 and x<=745 and y>=350 and y<=475 and GameBoard[8] == 3:
                            SetupBoxHorizontal9.setFill('blue')
                            GameBoard[8] = 0
                            PlayerXNext.draw(win)
                            NextStart = 0
                        else:
                            Oops = 1
                            InitialStart = 0
                            RetryMessageO = Text(Point(150,400),"Player O, please\n select a different\nsquare click to\nclear this messsage")
                            RetryMessageO.setTextColor('blue')
                            RetryMessageO.setSize(15)
                            RetryMessageO.setStyle('bold')
                            RetryMessageO.draw(win)
                        
                        
                    if RandomSelect == 0 and NextStart == 1:
                        click = win.getMouse()
                        x = click.getX()
                        y = click.getY()
                        PlayerONext.undraw()
                        if Oops == 1:
                            RetryMessageO.undraw()
                            Oops = 0
                        elif x>=370 and x<=495 and y>=100 and y<=225 and GameBoard[0] == 3:
                            SetupBoxHorizontal1.setFill('blue')
                            GameBoard[0] = 0
                            NextStart = 0
                            PlayerXNext.draw(win)
                        elif x>=495 and x<=620 and y>=100 and y<=225 and GameBoard[1] == 3:
                            SetupBoxHorizontal2.setFill('blue')
                            GameBoard[1] = 0
                            NextStart = 0
                            PlayerXNext.draw(win)
                        elif x>=620 and x<=745 and y>=100 and y<=225 and GameBoard[2] == 3:
                            SetupBoxHorizontal3.setFill('blue')
                            GameBoard[2] = 0
                            NextStart = 0
                            PlayerXNext.draw(win)
                        elif x>=370 and x<=495 and y>=225 and y<=350 and GameBoard[3] == 3:
                            SetupBoxHorizontal4.setFill('blue')
                            GameBoard[3] = 0
                            NextStart = 0
                            PlayerXNext.draw(win)
                        elif x>=495 and x<=620 and y>=225 and y<=350 and GameBoard[4] == 3:
                            SetupBoxHorizontal5.setFill('blue')
                            GameBoard[4] = 0
                            NextStart = 0
                            PlayerXNext.draw(win)
                        elif x>=620 and y<=745 and y>=225 and y<=350 and GameBoard[5] == 3:
                            SetupBoxHorizontal6.setFill('blue')
                            GameBoard[5] = 0
                            NextStart = 0
                            PlayerXNext.draw(win)
                        elif x>=370 and x<=495 and y>=350 and y<=475 and GameBoard[6] == 3:
                            SetupBoxHorizontal7.setFill('blue')
                            GameBoard[6] = 0
                            NextStart = 0
                            PlayerXNext.draw(win)
                        elif x>=495 and x<=620 and y>=350 and y<=475 and GameBoard[7] == 3:
                            SetupBoxHorizontal8.setFill('blue')
                            GameBoard[7] = 0
                            NextStart = 0
                            PlayerXNext.draw(win)
                        elif x>=620 and x<=745 and y>=350 and y<=475 and GameBoard[8] == 3:
                            SetupBoxHorizontal9.setFill('blue')
                            GameBoard[8] = 0
                            NextStart = 0
                            PlayerXNext.draw(win)
                        elif x >= 75 and x<=225 and y>=450 and y<=525:
                            win.close()
                            GAME2 = False
                            Yeet = False
                            break
                        else:
                            Oops = 1
                            NextStart = 1
                            RetryMessageO = Text(Point(150,400),"Player O, please\n select a different\nsquare click to\nclear this messsage")
                            RetryMessageO.setTextColor('blue')
                            RetryMessageO.setSize(15)
                            RetryMessageO.setStyle('bold')
                            RetryMessageO.draw(win)
                            #Horizontal
                        if GameBoard[0] == 0 and GameBoard[1] == 0 and GameBoard[2] == 0:
                            PlayerXNext.undraw()
                            PlayerONext.undraw()
                            WinnerO = Text(Point(150,400),"O is the winner")
                            WinnerO.setSize(15)
                            WinnerO.setStyle('bold')
                            WinnerO.setTextColor('blue')
                            WinnerO.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[3] == 0 and GameBoard[4] == 0 and GameBoard[5] == 0:
                            PlayerXNext.undraw()
                            PlayerONext.undraw()
                            WinnerO = Text(Point(150,400),"O is the winner")
                            WinnerO.setSize(15)
                            WinnerO.setStyle('bold')
                            WinnerO.setTextColor('blue')
                            WinnerO.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[6] == 0 and GameBoard[7] == 0 and GameBoard[8] == 0:
                            PlayerXNext.undraw()
                            PlayerONext.undraw()
                            WinnerO = Text(Point(150,400),"O is the winner")
                            WinnerO.setSize(15)
                            WinnerO.setStyle('bold')
                            WinnerO.setTextColor('blue')
                            WinnerO.draw(win)
                            GameStarting = False
                            break
                        #Diagonal
                        if GameBoard[0] == 0 and GameBoard[4] == 0 and GameBoard[8] == 0:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerO = Text(Point(150,400),"O is the winner")
                            WinnerO.setSize(15)
                            WinnerO.setStyle('bold')
                            WinnerO.setTextColor('blue')
                            WinnerO.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[2] == 0 and GameBoard[4] == 0 and GameBoard[6] == 0:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerO = Text(Point(150,400),"O is the winner")
                            WinnerO.setSize(15)
                            WinnerO.setStyle('bold')
                            WinnerO.setTextColor('blue')
                            WinnerO.draw(win)
                            GameStarting = False
                            break
                        #Vertical
                        if GameBoard[0] == 0 and GameBoard[3] == 0 and GameBoard[6] == 0:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerO = Text(Point(150,400),"O is the winner")
                            WinnerO.setSize(15)
                            WinnerO.setStyle('bold')
                            WinnerO.setTextColor('blue')
                            WinnerO.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[1] == 0 and GameBoard[4] == 0 and GameBoard[7] == 0:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerO = Text(Point(150,400),"O is the winner")
                            WinnerO.setSize(15)
                            WinnerO.setStyle('bold')
                            WinnerO.setTextColor('blue')
                            WinnerO.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[2] == 0 and GameBoard[5] == 0 and GameBoard[8] == 0:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerO = Text(Point(150,400),"O is the winner")
                            WinnerO.setSize(15)
                            WinnerO.setStyle('bold')
                            WinnerO.setTextColor('blue')
                            WinnerO.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[0] != 3 and GameBoard[1] != 3 and GameBoard[2] != 3 and GameBoard[3] != 3 and GameBoard[4] != 3 and GameBoard[5] != 3 and GameBoard[6] != 3 and GameBoard[7] != 3 and GameBoard[8] != 3:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            Tie = Text(Point(150,400),"It is a tie")
                            Tie.setSize(15)
                            Tie.setStyle('bold')
                            Tie.setTextColor('gold')
                            Tie.draw(win)
                            GameStarting = False
                            break


                    if RandomSelect == 0 and NextStart == 0:
                        click = win.getMouse()
                        x = click.getX()
                        y = click.getY()
                        PlayerXNext.undraw()
                        if Oops == 1:
                            RetryMessageX.undraw()
                            Oops = 0
                        elif x>=370 and x<=495 and y>=100 and y<=225 and GameBoard[0] == 3:
                            SetupBoxHorizontal1.setFill('red')
                            GameBoard[0] = 1
                            PlayerONext.draw(win)
                            NextStart = 1

                        elif x>=495 and x<=620 and y>=100 and y<=225 and GameBoard[1] == 3:
                            SetupBoxHorizontal2.setFill('red')
                            GameBoard[1] = 1
                            PlayerONext.draw(win)
                            NextStart = 1

                        elif x>=620 and x<=745 and y>=100 and y<=225 and GameBoard[2] == 3:
                            SetupBoxHorizontal3.setFill('red')
                            GameBoard[2] = 1
                            PlayerONext.draw(win)
                            NextStart = 1

                        elif x>=370 and x<=495 and y>=225 and y<=350 and GameBoard[3] == 3:
                            SetupBoxHorizontal4.setFill('red')
                            GameBoard[3] = 1
                            PlayerONext.draw(win)
                            NextStart = 1

                        elif x>=495 and x<=620 and y>=225 and y<=350 and GameBoard[4] == 3:
                            SetupBoxHorizontal5.setFill('red')
                            GameBoard[4] = 1
                            PlayerONext.draw(win)
                            NextStart = 1

                        elif x>=620 and y<=745 and y>=225 and y<=350 and GameBoard[5] == 3:
                            SetupBoxHorizontal6.setFill('red')
                            GameBoard[5] = 1
                            PlayerONext.draw(win)
                            NextStart = 1

                        elif x>=370 and x<=495 and y>=350 and y<=475 and GameBoard[6] == 3:
                            SetupBoxHorizontal7.setFill('red')
                            GameBoard[6] = 1
                            PlayerONext.draw(win)
                            NextStart = 1

                        elif x>=495 and x<=620 and y>=350 and y<=475 and GameBoard[7] == 3:
                            SetupBoxHorizontal8.setFill('red')
                            GameBoard[7] = 1
                            PlayerONext.draw(win)
                            NextStart = 1

                        elif x>=620 and x<=745 and y>=350 and y<=475 and GameBoard[8] == 3:
                            SetupBoxHorizontal9.setFill('red')
                            GameBoard[8] = 1
                            PlayerONext.draw(win)
                            NextStart = 1

                        elif x >= 75 and x<=225 and y>=450 and y<=525:
                            win.close()
                            GAME2 = False
                            Yeet = False
                            break
                        else:
                            Oops = 1
                            NextStart = 0
                            RetryMessageX = Text(Point(150,400),"Player X, please\n select a different\nsquare. Click to\ndismiss this messsage")
                            RetryMessageX.setTextColor('red')
                            RetryMessageX.setSize(15)
                            RetryMessageX.setStyle('bold')
                            RetryMessageX.draw(win)
                        #Horizontal
                        if GameBoard[0] == 1 and GameBoard[1] == 1 and GameBoard[2] == 1:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerX = Text(Point(150,400),"X is the winner")
                            WinnerX.setSize(15)
                            WinnerX.setStyle('bold')
                            WinnerX.setTextColor('red')
                            WinnerX.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[3] == 1 and GameBoard[4] == 1 and GameBoard[5] == 1:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerX = Text(Point(150,400),"X is the winner")
                            WinnerX.setSize(15)
                            WinnerX.setStyle('bold')
                            WinnerX.setTextColor('red')
                            WinnerX.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[6] == 1 and GameBoard[7] == 1 and GameBoard[8] == 1:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerX = Text(Point(150,400),"X is the winner")
                            WinnerX.setSize(15)
                            WinnerX.setStyle('bold')
                            WinnerX.setTextColor('red')
                            WinnerX.draw(win)
                            GameStarting = False
                            break
                        #Diagonal
                        if GameBoard[0] == 1 and GameBoard[4] == 1 and GameBoard[8] == 1:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerX = Text(Point(150,400),"X is the winner")
                            WinnerX.setSize(15)
                            WinnerX.setStyle('bold')
                            WinnerX.setTextColor('red')
                            WinnerX.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[2] == 1 and GameBoard[4] == 1 and GameBoard[6] == 1:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerX = Text(Point(150,400),"X is the winner")
                            WinnerX.setSize(15)
                            WinnerX.setStyle('bold')
                            WinnerX.setTextColor('red')
                            WinnerX.draw(win)
                            GameStarting = False
                            break
                        #Vertical
                        if GameBoard[0] == 1 and GameBoard[3] == 1 and GameBoard[6] == 1:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerX = Text(Point(150,400),"X is the winner")
                            WinnerX.setSize(15)
                            WinnerX.setStyle('bold')
                            WinnerX.setTextColor('red')
                            WinnerX.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[1] == 1 and GameBoard[4] == 1 and GameBoard[7] == 1:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerX = Text(Point(150,400),"X is the winner")
                            WinnerX.setSize(15)
                            WinnerX.setStyle('bold')
                            WinnerX.setTextColor('red')
                            WinnerX.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[2] == 1 and GameBoard[5] == 1 and GameBoard[8] == 1:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerX = Text(Point(150,400),"X is the winner")
                            WinnerX.setSize(15)
                            WinnerX.setStyle('bold')
                            WinnerX.setTextColor('red')
                            WinnerX.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[0] != 3 and GameBoard[1] != 3 and GameBoard[2] != 3 and GameBoard[3] != 3 and GameBoard[4] != 3 and GameBoard[5] != 3 and GameBoard[6] != 3 and GameBoard[7] != 3 and GameBoard[8] != 3:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            Tie = Text(Point(150,400),"It is a tie")
                            Tie.setSize(15)
                            Tie.setStyle('bold')
                            Tie.setTextColor('gold')
                            Tie.draw(win)
                            GameStarting = False
                            break


                    #If Player X goes first
                    if RandomSelect == 1 and InitialStart == 1:
                        print(RandomSelect,InitialStart)
                        click = win.getMouse()
                        x = click.getX()
                        y = click.getY()
                        InitialStart = 3
                        PlayerXFirst.undraw()
                        if Oops == 1:
                            RetryMessageX.undraw()
                            Oops = 0
                        elif x >= 75 and x<=225 and y>=450 and y<=525:
                            win.close()
                            GAME2 = False
                            Yeet = False
                            break
                        elif x>=370 and x<=495 and y>=100 and y<=225 and GameBoard[0] == 3:
                            SetupBoxHorizontal1.setFill('red')
                            GameBoard[0] = 1
                            NextStart = 0
                            IntitialStart = 3
                            print(InitialStart)
                            PlayerONext.draw(win)
                        elif x>=495 and x<=620 and y>=100 and y<=225 and GameBoard[1] == 3:
                            SetupBoxHorizontal2.setFill('red')
                            GameBoard[1] = 1
                            NextStart = 0
                            IntitialStart = 3
                            PlayerONext.draw(win)
                        elif x>=620 and x<=745 and y>=100 and y<=225 and GameBoard[2] == 3:
                            SetupBoxHorizontal3.setFill('red')
                            GameBoard[2] = 1
                            NextStart = 0
                            IntitialStart = 3
                            PlayerONext.draw(win)
                        elif x>=370 and x<=495 and y>=225 and y<=350 and GameBoard[3] == 3:
                            SetupBoxHorizontal4.setFill('red')
                            GameBoard[3] = 1
                            NextStart = 0
                            IntitialStart = 3
                            PlayerONext.draw(win)
                        elif x>=495 and x<=620 and y>=225 and y<=350 and GameBoard[4] == 3:
                            SetupBoxHorizontal5.setFill('red')
                            GameBoard[4] = 1
                            NextStart = 0
                            IntitialStart = 3
                            PlayerONext.draw(win)
                        elif x>=620 and y<=745 and y>=225 and y<=350 and GameBoard[5] == 3:
                            SetupBoxHorizontal6.setFill('red')
                            GameBoard[5] = 1
                            NextStart = 0
                            IntitialStart = 3
                            PlayerONext.draw(win)
                        elif x>=370 and x<=495 and y>=350 and y<=475 and GameBoard[6] == 3:
                            SetupBoxHorizontal7.setFill('red')
                            GameBoard[6] = 1
                            NextStart = 0
                            IntitialStart = 3
                            PlayerONext.draw(win)
                        elif x>=495 and x<=620 and y>=350 and y<=475 and GameBoard[7] == 3:
                            SetupBoxHorizontal8.setFill('red')
                            GameBoard[7] = 1
                            NextStart = 0
                            IntitialStart = 3
                            PlayerONext.draw(win)
                        elif x>=620 and x<=745 and y>=350 and y<=475 and GameBoard[8] == 3:
                            SetupBoxHorizontal9.setFill('red')
                            GameBoard[8] = 1
                            NextStart = 0
                            IntitialStart = 3
                            PlayerONext.draw(win)
##                        else:
##                            Oops = 1
##                            InitialStart = 1
##                            RetryMessageX = Text(Point(150,400),"Player X, please\n select a different\nsquare. Click to\ndismiss this messsage")
##                            RetryMessageX.setTextColor('red')
##                            RetryMessageX.setSize(15)
##                            RetryMessageX.setStyle('bold')
##                            RetryMessageX.draw(win)
                        print(InitialStart)


                    if RandomSelect == 1 and NextStart == 0:
                        click = win.getMouse()
                        x = click.getX()
                        y = click.getY()
                        PlayerONext.undraw()
                        if Oops == 1:
                            RetryMessageO.undraw()
                            Oops = 0
                        elif x>=370 and x<=495 and y>=100 and y<=225 and GameBoard[0] == 3:
                            SetupBoxHorizontal1.setFill('blue')
                            GameBoard[0] = 0
                            NextStart = 1
                            PlayerXNext.draw(win)
                        elif x>=495 and x<=620 and y>=100 and y<=225 and GameBoard[1] == 3:
                            SetupBoxHorizontal2.setFill('blue')
                            GameBoard[1] = 0
                            NextStart = 1
                            PlayerXNext.draw(win)
                        elif x>=620 and x<=745 and y>=100 and y<=225 and GameBoard[2] == 3:
                            SetupBoxHorizontal3.setFill('blue')
                            GameBoard[2] = 0
                            NextStart = 1
                            PlayerXNext.draw(win)
                        elif x>=370 and x<=495 and y>=225 and y<=350 and GameBoard[3] == 3:
                            SetupBoxHorizontal4.setFill('blue')
                            GameBoard[3] = 0
                            NextStart = 1
                            PlayerXNext.draw(win)
                        elif x>=495 and x<=620 and y>=225 and y<=350 and GameBoard[4] == 3:
                            SetupBoxHorizontal5.setFill('blue')
                            GameBoard[4] = 0
                            NextStart = 1
                            PlayerXNext.draw(win)
                        elif x>=620 and y<=745 and y>=225 and y<=350 and GameBoard[5] == 3:
                            SetupBoxHorizontal6.setFill('blue')
                            GameBoard[5] = 0
                            NextStart = 1
                            PlayerXNext.draw(win)
                        elif x>=370 and x<=495 and y>=350 and y<=475 and GameBoard[6] == 3:
                            SetupBoxHorizontal7.setFill('blue')
                            GameBoard[6] = 0
                            NextStart = 1
                            PlayerXNext.draw(win)
                        elif x>=495 and x<=620 and y>=350 and y<=475 and GameBoard[7] == 3:
                            SetupBoxHorizontal8.setFill('blue')
                            GameBoard[7] = 0
                            NextStart = 1
                            PlayerXNext.draw(win)
                        elif x>=620 and x<=745 and y>=350 and y<=475 and GameBoard[8] == 3:
                            SetupBoxHorizontal9.setFill('blue')
                            GameBoard[8] = 0
                            NextStart = 1
                            PlayerXNext.draw(win)
                        elif x >= 75 and x<=225 and y>=450 and y<=525:
                            win.close()
                            GAME2 = False
                            Yeet = False
                            break
                        else:
                            Oops = 1
                            NextStart = 0
                            RetryMessageO = Text(Point(150,400),"Player O, please\n select a different\nsquare. Click to\nclear this messsage")
                            RetryMessageO.setTextColor('blue')
                            RetryMessageO.setSize(15)
                            RetryMessageO.setStyle('bold')
                            RetryMessageO.draw(win)
                        #Horizontal
                        if GameBoard[0] == 0 and GameBoard[1] == 0 and GameBoard[2] == 0:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerO = Text(Point(150,400),"O is the winner")
                            WinnerO.setSize(15)
                            WinnerO.setStyle('bold')
                            WinnerO.setTextColor('blue')
                            WinnerO.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[3] == 0 and GameBoard[4] == 0 and GameBoard[5] == 0:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerO = Text(Point(150,400),"O is the winner")
                            WinnerO.setSize(15)
                            WinnerO.setStyle('bold')
                            WinnerO.setTextColor('blue')
                            WinnerO.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[6] == 0 and GameBoard[7] == 0 and GameBoard[8] == 0:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerO = Text(Point(150,400),"O is the winner")
                            WinnerO.setSize(15)
                            WinnerO.setStyle('bold')
                            WinnerO.setTextColor('blue')
                            WinnerO.draw(win)
                            GameStarting = False
                            break
                        #Diagonal
                        if GameBoard[0] == 0 and GameBoard[4] == 0 and GameBoard[8] == 0:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerO = Text(Point(150,400),"O is the winner")
                            WinnerO.setSize(15)
                            WinnerO.setStyle('bold')
                            WinnerO.setTextColor('blue')
                            WinnerO.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[2] == 0 and GameBoard[4] == 0 and GameBoard[6] == 0:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerO = Text(Point(150,400),"O is the winner")
                            WinnerO.setSize(15)
                            WinnerO.setStyle('bold')
                            WinnerO.setTextColor('blue')
                            WinnerO.draw(win)
                            GameStarting = False
                            break
                        #Vertical
                        if GameBoard[0] == 0 and GameBoard[3] == 0 and GameBoard[6] == 0:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerO = Text(Point(150,400),"O is the winner")
                            WinnerO.setSize(15)
                            WinnerO.setStyle('bold')
                            WinnerO.setTextColor('blue')
                            WinnerO.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[1] == 0 and GameBoard[4] == 0 and GameBoard[7] == 0:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerO = Text(Point(150,400),"O is the winner")
                            WinnerO.setSize(15)
                            WinnerO.setStyle('bold')
                            WinnerO.setTextColor('blue')
                            WinnerO.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[2] == 0 and GameBoard[5] == 0 and GameBoard[8] == 0:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerO = Text(Point(150,400),"O is the winner")
                            WinnerO.setSize(15)
                            WinnerO.setStyle('bold')
                            WinnerO.setTextColor('blue')
                            WinnerO.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[0] != 3 and GameBoard[1] != 3 and GameBoard[2] != 3 and GameBoard[3] != 3 and GameBoard[4] != 3 and GameBoard[5] != 3 and GameBoard[6] != 3 and GameBoard[7] != 3 and GameBoard[8] != 3:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            Tie = Text(Point(150,400),"It is a tie")
                            Tie.setSize(15)
                            Tie.setStyle('bold')
                            Tie.setTextColor('gold')
                            Tie.draw(win)
                            GameStarting = False
                            break


                    if RandomSelect == 1 and NextStart == 1:
                        click = win.getMouse()
                        x = click.getX()
                        y = click.getY()
                        PlayerXNext.undraw()
                        if Oops == 1:
                            RetryMessageX.undraw()
                            Oops = 0
                        elif x>=370 and x<=495 and y>=100 and y<=225 and GameBoard[0] == 3:
                            SetupBoxHorizontal1.setFill('red')
                            GameBoard[0] = 1
                            NextStart = 0
                            PlayerONext.draw(win)
                        elif x>=495 and x<=620 and y>=100 and y<=225 and GameBoard[1] == 3:
                            SetupBoxHorizontal2.setFill('red')
                            GameBoard[1] = 1
                            NextStart = 0
                            PlayerONext.draw(win)
                        elif x>=620 and x<=745 and y>=100 and y<=225 and GameBoard[2] == 3:
                            SetupBoxHorizontal3.setFill('red')
                            GameBoard[2] = 1
                            NextStart = 0
                            PlayerONext.draw(win)
                        elif x>=370 and x<=495 and y>=225 and y<=350 and GameBoard[3] == 3:
                            SetupBoxHorizontal4.setFill('red')
                            GameBoard[3] = 1
                            NextStart = 0
                            PlayerONext.draw(win)
                        elif x>=495 and x<=620 and y>=225 and y<=350 and GameBoard[4] == 3:
                            SetupBoxHorizontal5.setFill('red')
                            GameBoard[4] = 1
                            NextStart = 0
                            PlayerONext.draw(win)
                        elif x>=620 and y<=745 and y>=225 and y<=350 and GameBoard[5] == 3:
                            SetupBoxHorizontal6.setFill('red')
                            GameBoard[5] = 1
                            NextStart = 0
                            PlayerONext.draw(win)
                        elif x>=370 and x<=495 and y>=350 and y<=475 and GameBoard[6] == 3:
                            SetupBoxHorizontal7.setFill('red')
                            GameBoard[6] = 1
                            NextStart = 0
                            PlayerONext.draw(win)
                        elif x>=495 and x<=620 and y>=350 and y<=475 and GameBoard[7] == 3:
                            SetupBoxHorizontal8.setFill('red')
                            GameBoard[7] = 1
                            NextStart = 0
                            PlayerONext.draw(win)
                        elif x>=620 and x<=745 and y>=350 and y<=475 and GameBoard[8] == 3:
                            SetupBoxHorizontal9.setFill('red')
                            GameBoard[8] = 1
                            NextStart = 0
                            PlayerONext.draw(win)
                        elif x >= 75 and x<=225 and y>=450 and y<=525:
                            win.close()
                            GAME2 = False
                            Yeet = False
                            break
                        else:
                            Oops = 1
                            NextStart = 1
                            RetryMessageX = Text(Point(150,400),"Player X, please\n select a different\nsquare. Click to\ndismiss this messsage")
                            RetryMessageX.setTextColor('red')
                            RetryMessageX.setSize(15)
                            RetryMessageX.setStyle('bold')
                            RetryMessageX.draw(win)

                        #Horizontal
                        if GameBoard[0] == 1 and GameBoard[1] == 1 and GameBoard[2] == 1:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerX = Text(Point(150,400),"X is the winner")
                            WinnerX.setSize(15)
                            WinnerX.setStyle('bold')
                            WinnerX.setTextColor('red')
                            WinnerX.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[3] == 1 and GameBoard[4] == 1 and GameBoard[5] == 1:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerX = Text(Point(150,400),"X is the winner")
                            WinnerX.setSize(15)
                            WinnerX.setStyle('bold')
                            WinnerX.setTextColor('red')
                            WinnerX.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[6] == 1 and GameBoard[7] == 1 and GameBoard[8] == 1:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerX = Text(Point(150,400),"X is the winner")
                            WinnerX.setSize(15)
                            WinnerX.setStyle('bold')
                            WinnerX.setTextColor('red')
                            WinnerX.draw(win)
                            GameStarting = False
                            break
                        #Diagonal
                        if GameBoard[0] == 1 and GameBoard[4] == 1 and GameBoard[8] == 1:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerX = Text(Point(150,400),"X is the winner")
                            WinnerX.setSize(15)
                            WinnerX.setStyle('bold')
                            WinnerX.setTextColor('red')
                            WinnerX.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[2] == 1 and GameBoard[4] == 1 and GameBoard[6] == 1:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerX = Text(Point(150,400),"X is the winner")
                            WinnerX.setSize(15)
                            WinnerX.setStyle('bold')
                            WinnerX.setTextColor('red')
                            WinnerX.draw(win)
                            GameStarting = False
                            break
                        #Vertical
                        if GameBoard[0] == 1 and GameBoard[3] == 1 and GameBoard[6] == 1:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerX = Text(Point(150,400),"X is the winner")
                            WinnerX.setSize(15)
                            WinnerX.setStyle('bold')
                            WinnerX.setTextColor('red')
                            WinnerX.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[1] == 1 and GameBoard[4] == 1 and GameBoard[7] == 1:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerX = Text(Point(150,400),"X is the winner")
                            WinnerX.setSize(15)
                            WinnerX.setStyle('bold')
                            WinnerX.setTextColor('red')
                            WinnerX.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[2] == 1 and GameBoard[5] == 1 and GameBoard[8] == 1:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            WinnerX = Text(Point(150,400),"X is the winner")
                            WinnerX.setSize(15)
                            WinnerX.setStyle('bold')
                            WinnerX.setTextColor('red')
                            WinnerX.draw(win)
                            GameStarting = False
                            break
                        if GameBoard[0] != 3 and GameBoard[1] != 3 and GameBoard[2] != 3 and GameBoard[3] != 3 and GameBoard[4] != 3 and GameBoard[5] != 3 and GameBoard[6] != 3 and GameBoard[7] != 3 and GameBoard[8] != 3:
                            PlayerONext.undraw()
                            PlayerXNext.undraw()
                            Tie = Text(Point(150,400),"It is a tie")
                            Tie.setSize(15)
                            Tie.setStyle('bold')
                            Tie.setTextColor('gold')
                            Tie.draw(win)
                            GameStarting = False
                            break

                
main()
