#DiceRoll.py
#Name: Trevor Woosley
#Date: 03/02/2025
#Assignment: Dice Roll
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for r in range(100):
    dice1 = random.randint(1,6)
    rolls[dice1 - 1] = rolls[dice1 - 1] + 1

    dice2 = random.randint(1,6)
    rolls[dice2 - 1] = rolls[dice2 - 1] + 1

  #find the sum total of the two dice

  sumDice = dice1 + dice2
  
  #print statictics for dice rolls
  dice = 1
  for count in rolls:
    print(dice, ":", count)
    dice = dice + 1

  print (sumDice)

if __name__ == '__main__':
  main()
