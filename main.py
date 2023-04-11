# A Stock Exchange game with a twist (twist coming soon-ish)
# Roadmap:
## ⏳[ ] Spread out functions to classes and function collections
## [X] Improve text currency formating
## [X] Currency choice
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

shark = loanShark.Loanshark(random.randint(5, 50) * 1000, random.randint(-4, 3))

def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

def moneyToString(ammount, currency_symbol):
    addedSymbol = f"{currency_symbol}{ammount:_}"
    addedSymbol = addedSymbol.replace("_", "'")
    return addedSymbol

# Function to prompt user for currency choice
def chooseCurrency():
    print("Please choose your currency symbol or code (CHF, $, €, GBP, etc.) (no space included): ")
    currency_symbol = input()
    return currency_symbol

# Prompt user for currency choice
currency_symbol = chooseCurrency()


logo = ascii_art.return_logo()

# Function to skip to the next day
def skip(days, weekDayIndex):
    days = days - 1
    weekDayIndex = weekDayIndex + 1
    
    return days, weekDayIndex


# Function that runs at the end of the game showing statistics
def endgame(balance, shares, days, loan):
    print("\n\n\nYou finished with:")
    print("Balance:", moneyToString(balance, currency_symbol))
    print("Shares:", shares)
    print("Loan debt left:", moneyToString(loan, currency_symbol))
    print("Which you earned withing:", days, "days!")
    print("\nGAME OVER")

# Function to show every day with all options. Basically the main game function
def rounds(days, balance, shares, weekDay):
    totalDays = days
    for i in range(days):
        nextDay = False
        price = random.randint(1, 1000)

        while nextDay == False:
            clear()
            if weekDay[1]%7 == 0:
                shark.setPaidInterestState(False)
            # print(logo)
            print("Days left:", days, "            Today is:", weekDay[0][weekDay[1]%7])
            print("Balance:", moneyToString(balance, currency_symbol), "          Shares:", shares)
            print("Todays Stock price:", moneyToString(price, currency_symbol))
            print("Your loan:", moneyToString(shark.loan, currency_symbol), "        Interestrate:", f"{shark.interestFavor}%", "        Sharkfavor:", shark.favor)
            print("Weekly interest:", moneyToString(shark.interestRate, currency_symbol), "    This weeks interest paid?:", shark.returnPaidInterest())
            print("\nWhat do you want to do?: \nBuy(1)?          Sell(2)?        Loanshark(3)?          Next day(4)?\n")
            choice = input("Your Choice?: ")

            if choice == "1":
                balance, shares = shareTrade.buy(balance, price, shares)
            elif choice == "2":
                balance, shares = shareTrade.sell(balance, price, shares)
            elif choice == "3":
                balance, loan, interestRate = shark.menu(balance)
            elif choice == "4": 
                if weekDay[1]%7 == 6:
                    if shark.returnPaidInterest():
                        nextDay = True
                    else:
                        print("Weekly interest of", moneyToString(shark.returnInterestRate(), currency_symbol), "not yet paid")
                        choice = input("Pay interest?(1)        Skip this payment?(2): ")

                        if choice == "1":
                            balance = shark.payInterest(balance)
                            if shark.returnPaidInterest() == True:
                                nextDay = True

                        elif choice == "2":
                            shark.skipInterestPayment()
                            nextDay = True
                            
                else:
                    nextDay = True
            else:
                input("Wrong Choice Error. Press enter to continue...")

        days, weekDay[1] = skip(days, weekDay[1])
    endgame(balance, shares, totalDays, loan)


# Function to initiate the game
def main():
    days = int(input("Choose how many days: "))
    balance = random.randint(1, 10) * 1000
    shares = 0
    weekDay = [["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], 0]
    currentWeekDay = 0
    rounds(days, balance, shares, weekDay)


main()
