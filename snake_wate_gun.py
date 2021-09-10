"""
MY FIRST MINI PROJECT

"""

import random
print("Welcome to SNAKE-WATER-GUN Game zone")
print("Enter s for ---> SNAKE")
print("Enter w for ---> WATER")
print("Enter g for ---> GUN")
try:
    n = int(input("Enter the number of rounds you want to play:"))
    i = 1
    won = 0
    losse = 0
    t = ['s', 'g', 'w']
    while(i <= n):
        print("ROUND", i)
        p = random.choice(t)
        c = input("Enter your choice: ")
        if(c!='g' and c!='s' and c != 'w'):
          print("Invalide input try again")
          continue
        if (c == 'g' and p == 'w'):
          print("You Losse Round", i)
          print("Your choice", c)
          print("Opponent choice", p)
          losse+=1
      
        elif (c == 'w' and p == 'g'):
          print("Congratulation You Won Round", i)
          print("Your choice", c)
          print("Opponent choice", p)
          won+=1
      
        elif (c == 'g' and p == 's'):
          print("congratulation You Won Round", i)
          print("Your choice", c)
          print("Opponent choice", p)
          won += 1
      
        elif( c == 's' and p == 'g'):
          print("You Losse Round", i)
          print("Your choice", c)
          print("Opponent choice", p)
          losse +=1
      
        elif (c == 's' and p == 'w'):
          print("congratulation You Won Round", i)
          print("Your choice", c)
          print("Opponent choice", p)
          won += 1
      
        elif(c == 'w' and p == 's'):
          print("You Losse Round", i)
          print("Your choice", c)
          print("Opponent choice", p)
          losse += 1
      
        elif (c == p):
          print("Match Draw")
      
        i+=1
    
    if (won > losse):
      print("******You win the match******")
      print("YOUR SCORE IS", won)
  
    elif(won == losse):
      print("******MATCH DRAW******")

    else:
      print("******YOU LOSS THE MATCH******")
      print("YOUR SCORE IS", won)

    
except :
    print("Sorry please Enter Integer value of rounds you want to play")
    
