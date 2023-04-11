import random

class Loanshark:
    def __init__(self, loan, favor):
        self.favorTicker = 0
        self.loan = loan
        self.favor = favor
        self.interestFavor = 12 - self.favor
        self.interestRate = int(self.loan/100 * self.interestFavor)
        self.paidInterest = False

    def takeLoan(self, balance):
        self.loanAmmount = int(input("How much?"))
        self.loan += self.loanAmmount
        self.interestRate = int(self.loan/100 * self.interestFavor)
        balance += self.loanAmmount
        return balance, self.loan, self.interestRate

    def returnLoan(self):
        return self.loan

    def returnPaidInterest(self):
        return self.paidInterest

    def setPaidInterestState(self, didPay):
        self.paidInterest = didPay
    
    def returnInterestRate(self):
        return int(self.loan/100 * self.interestFavor)

    def changeFavor(self, favorChange):
        self.favor = (self.favor + favorChange if self.favor+favorChange < 11 else 10)

    def sharkBreakLeg(self):
        if random.randint(1, 20) + self.favor < 10:
            print("Your legs are broken")
        else:
            print("Legs aren't broken")
        
        input("Press enter to continue...")
    
    def skipInterestPayment(self):
        self.favorTicker = 0
        self.changeFavor(-1)
        self.sharkBreakLeg()
        self.setPaidInterestState(True)
    
    def payInterest(self, balance):
        if balance - self.interestRate >= 0:
            balance -= self.interestRate
            print("Paid shark")
            input("Press enter to continue...")
            self.setPaidInterestState(True)
            self.favorTicker += 1
            if self.favorTicker >= 10:
                self.favorTicker = 0
                self.changeFavor(1)
            return balance
        else:
            print("Not enough money...")
            input("Press enter to continue...")
            return balance
        
    
    def menu(self, balance):
        # TODO: add loan system        
        print("Take out a loan, pay due interest or repay debt?:")
        print("Take out(1)?        Pay due itnerest(2)?          Repay(3)?")
        choice = input("Your Choice?: ")
    
        if choice == "1":
            return self.takeLoan(balance)
        elif choice == "2":
            return self.payInterest(balance), self.loan, self.interestRate
            
