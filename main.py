# A Stock Exchange game with a twist (twist coming soon-ish)
# Roadmap:
## ⏳[ ] Spread out functions to classes and function collections
## [X] Improve text currency formating
## [ ] Currency choice
## [ ] Language selection (English & German at first)
## [ ] Add Loan system with debt and dayly interest
## [ ] Add more realistic stock movement
## [ ] Add history of stock
## [ ] Add more stocks to choose from
## [ ] Add player and stock changes and interactions having effect on global market
## [ ] Add news and world events
## [ ] Add over the top detail like taxes, expenses, etc.

import random
import ascii_art
from features import shareTrade
from features import loanShark
from os import system, name

shark = loanShark.Loanshark(random.randint(5, 50) * 1000, random.randint(0, 4))

def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

def moneyToString(ammount):
  addedSymbol = f"${ammount:_}"
  addedSymbol = addedSymbol.replace("_", "'")
  return addedSymbol

logo = ascii_art.return_logo()

# Function to skip to the next day
def skip(days):
    days = days - 1
    return days


# Function that runs at the end of the game showing statistics
def endgame(balance, shares, days, loan):
    print("\n\n\nYou finished with:")
    print("Balance:", moneyToString(balance))
    print("Shares:", shares)
    print("Loan debt left:", moneyToString(loan))
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
            print("Days left:", days, "          Balance:",
                  moneyToString(balance), "          Shares:", shares)
            print("Todays Stock price:", f"${price}")
            print("Your loan:", moneyToString(shark.loan))
            print("\nWhat do you want to do?: \nBuy(1)?          Sell(2)?        Loanshark(3)?          Next day(3)?\n"
            )
            choice = input("Your Choice?: ")

            if choice == "1":
                balance, shares = shareTrade.buy(balance, price, shares)
            elif choice == "2":
                balance, shares = shareTrade.sell(balance, price, shares)
            elif choice == "3":
                balance, loan, interestRate = shark.menu(balance)
            elif choice == "4":
                nextDay = True
            else:
                input("Wrong Choice Error")

        days = skip(days)
    endgame(balance, shares, totalDays, loan)


# Function to initiate the game
def main():
    days = int(input("Choose how many days: "))
    balance = random.randint(1, 10) * 1000
    shares = 0
    rounds(days, balance, shares)


main()
