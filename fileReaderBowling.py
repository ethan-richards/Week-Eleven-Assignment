#Ethan Richards
#IWU CIS 125
#Bowling game kata 
#fileReaderBowling.py
#reads a file of scores and then prints the calculated scores and scores in the file to see if it is correct.
from BowlingGame import Game
import string

fileName = open("testscores.txt", "r") 
gameList = []

for line in fileName:
    line = line.strip() 
    scoreList = line.split(",") 
    scoreList = [int(i) for i in scoreList] 
    finalScore = scoreList.pop() 
    game = Game() 
    for roll in scoreList: 
        game.roll(roll)
    score = game.score() 
    print("Calculated score is {}, and the given score is {}".format(score,  finalScore))
    if score == finalScore:
        print("The score was correct!")
    else:
        print("The score should be", score)
            
     