from gameclass import game
from highscoreclass import Highscore

while True:

    try:
        menu = int(input("0: Exit, 1:Highscores, 2:Play: "))
    except:
        print("Wrong input")
        continue

    if menu == 0:
        break

    elif menu == 1:
        hs = Highscore()
        print(hs)
    elif menu == 2:
        g = game()
        g.timing(True)
        g.play()
        g.timing(False)
        print(g)
    else:
        print("wrong input")
