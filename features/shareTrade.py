def buysellchoice():
  # TODO: add check if number
  choice = input("")
  return int(choice)
  # chosen = False
  # while chosen == False:
    # choice = 0

# Function to buy shares
def buy(balance, price, shares):
    print("The max amount of shares you can buy is:", balance // price)
    print("If you want to buy max shares type: '12345'")
    print("How many shares would you like to buy?: ", end=" ")
    choice = buysellchoice()

    # short input to buy max amount of shares
    if choice == 12345:
        shares = shares + (balance // price)
        balance = balance - ((balance // price) * price)

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

