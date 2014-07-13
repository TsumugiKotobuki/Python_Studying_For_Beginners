from highscoreclass import Highscore
import random,time,glob


class game:
    def __init__(self):
        #generating random numbers
        random.seed()
        #important variables
        self.right = 0
        self.amount = 3
        #asking for the name
        s = input("Enter name (max. 10 letters): ")
        #limit it to 10 letters
        self.player = s[0:10]
        
        
    def play(self):
        
        #the actual game
        a = random.randint(1,10)
        for i in range(self.amount):
            a = random.randint(1,10)
            print(a)
            ac=int(input("enter the number now! "))
            
            if ac == a:

                self.right += 1
                

    def timing(self,start):
            
        #if start is true the game beginns, and we start counting
        if start:
            self.start_t = time.time()

        else:
            end_t = time.time()
            self.time = end_t - self.start_t

    def __str__(self):
            
            
            #output stuff
        output = "Correct:{0:d} of {1:d} in {2:.2f}" \
        " seconds".format(self.right,self.amount,self.time)

        if self.right == self.amount:
            output += ", highscore!"
            hs = Highscore()
            hs.save(self.player,self.time)
            print(hs)
            
        else:
            output += ", no highscore..."

        return output
