"""
MY FIRST MINI PROJECT

"""
import random
print("Welcome to SNAKE-WATER-GUN Game zone")
print("RULES TO PLAY GAME")
print("1 - If your choice is snake and opponent choice is water than you win the round")
print("2 - If your choice is water and opponent choice is snake than you lose the round")
print("3 - If your choice is gun and opponent choice is water than you lose the round")
print("4 - If your choice is water and opponent choice is gun than you win the round")
print("5 - If your choice is gun and opponent choice is snake than you win the round")
print("6 - If your choice is snake and opponent choice is gun than you lose the round")
print("7 - If your choice and opponent choice is same that draw round")
print("Enter s for ---> SNAKE")
print("Enter w for ---> WATER")
print("Enter g for ---> GUN")
try:
    n = int(input("Enter the number of rounds you want to play:"))
    i = 1
    win = 0
    lose = 0
    t = ['s', 'g', 'w']
    while(i <= n):
        print("ROUND", i)
        p = random.choice(t)
        c = input("Enter your choice: ")
        if(c!='g' and c!='s' and c != 'w'):
          print("Invalide input try again")
          continue
        if (c == 'g' and p == 'w'):
          print("You Lose Round", i)
          print("Your choice", c)
          print("Opponent choice", p)
          lose+=1
          print("Your score", win)
          print("Opponent score", lose)
      
        elif (c == 'w' and p == 'g'):
          print("Congratulation You Won Round", i)
          print("Your choice", c)
          print("Opponent choice", p)
          win+=1
          print("Your score", win)
          print("Opponent score", lose)
      
      
        elif (c == 'g' and p == 's'):
          print("congratulation You Won Round", i)
          print("Your choice", c)
          print("Opponent choice", p)
          win += 1
          print("Your score", win)
          print("Opponent score", lose)
      
        elif( c == 's' and p == 'g'):
          print("You Lose Round", i)
          print("Your choice", c)
          print("Opponent choice", p)
          lose +=1
          print("Your score", win)
          print("Opponent score", lose)
      
        elif (c == 's' and p == 'w'):
          print("congratulation You Won Round", i)
          print("Your choice", c)
          print("Opponent choice", p)
          win += 1
          print("Your score", win)
          print("Opponent score", lose)
      
        elif(c == 'w' and p == 's'):
          print("You Lose Round", i)
          print("Your choice", c)
          print("Opponent choice", p)
          lose += 1
          print("Your score", win)
          print("Opponent score", lose)
      
        elif (c == p):
          print("Match Draw")
          print("Your choice", c)
          print("Opponent choice", p)
      
        i+=1
    
    if (win > lose):
      print("******You win the match******")
      print("YOUR SCORE IS", won)
  
    elif(win == lose):
      print("******MATCH DRAW******")
      print("Number of rounds you win", win)
      print("Number of rounds you loss", lose)

    else:
      print("******YOU LOSS THE MATCH******")
      print("YOUR SCORE IS", win)

    
except :
    print("Sorry please Enter Integer value of rounds you want to play")
    
