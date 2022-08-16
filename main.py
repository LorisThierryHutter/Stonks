# A Stock Exchange game with a twist (twist coming soon-ish)
# Roadmap:
## ⏳[ ] Spread out functions to classes and function collections
## [ ] Add Loan system with debt and dayly interest
## [ ] Add more realistic stock movement
## [ ] Add history of stock
## [ ] Add more stocks to choose from
## [ ] Add player and stock changes and interactions having effect on global market
## [ ] Add news and world events
## [ ] Add over the top detail like taxes, expenses, etc.

import random
import ascii_art
from os import system, name

def clear():
  if name == 'nt':
    _= system('cls')

  else:
    _= system('clear')

logo = ascii_art.return_logo()

def buysellchoice():
  # TODO: add check if number
  choice = input("")
  return int(choice)
  # chosen = False
  # while chosen == False:
    # choice = 0


def loan():
  # TODO: add loan system
  print("Take out a loan or repay?: Take out(1)?          Repay(2)?")
  print("pog")

# Function to buy shares
def buy(balance, price, shares):
  print("The max amount of shares you can buy is:", balance//price)
  print("If you want to buy max shares type: '12345'")
  print("How many shares would you like to buy?: ", end=" ")
  choice = buysellchoice()

  # short input to buy max amount of shares
  if choice == 12345:
    shares = shares + (balance//price)
    balance = balance - ((balance//price) * price)

  else:
    if balance - (price * choice) < 0:
      print("You don't have enough money for that transaction!")

    else:
      balance = balance - (price * choice)
      shares = shares + choice

  return balance, shares

# Function to sell shares
def sell(balance, price, shares):
  print("The max amount of shares you can sell is:", shares)
  print("If you want to sell max shares type: '12345'")
  print("How many shares would you like to sell?: ", end=" ")
  choice = buysellchoice()

  # short input to sell max amount of shares
  if choice == 12345:
    balance = balance + (shares * price)
    shares = 0

  else:
    if choice > shares:
      print("You don't have enough shares for that transaction!")
    
    else:
      balance = balance + (price * choice)
      shares = shares - choice
  
  return balance, shares

# Function to skip to the next day
def skip(days):
  days = days - 1
  return days

# Function that runs at the end of the game showing statistics
def endgame(balance, shares, days):
  print("\n\n\nYou finished with:")
  print("Balance:", balance.replace("_", "'"))
  print("Shares:", shares)
  print("Which you earned withing:", days, "days!")
  print("\nGAME OVER")

# Function to show every day with all options. Basically the main game function
def rounds(days, balance, shares):
  totalDays = days
  for i in range(days):
    nextDay = False
    price = random.randint(1, 1000)
    while nextDay == False:
      clear()
      print(logo)
      balanceString = f"${balance:_}"
      print("Days left:", days, "          Balance:", balanceString.replace("_", "'"), "          Shares:", shares)
      print("Todays Stock price:", f"${price}")
      print("What do you want to do?: Buy(1)?          Sell(2)?          Next day(3)?")
      choice = input("Your Choice?: ")

      if choice == "1":
        balance, shares = buy(balance, price, shares)
      elif choice == "2":
        balance, shares = sell(balance, price, shares)
      elif choice == "3":
        nextDay = True
      else:
        input("Wrong Choice Error")
    
    days = skip(days)
  balanceString = f"${balance:_}"
  endgame(balanceString, shares, totalDays)


# Function to initiate the game
def main():
  days = int(input("Choose how many days: "))
  balance = random.randint(1, 10)*1000
  shares = 0
  rounds(days, balance, shares)



main()

