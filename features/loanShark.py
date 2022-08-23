class Loanshark:
    def __init__(self, loan, favor):
        self.loan = loan
        self.favor = favor
        self.interestRate = 12 - self.favor

    def takeLoan(self, balance):
        self.loanAmmount = int(input("How much?"))
        self.loan += self.loanAmmount
        self.interestRate = self.loan/100 * self.favor
        balance += self.loanAmmount
        return balance, self.loan, self.interestrate

    def returnLoan(self):
        return self.loan

    def returnInterestRate(self):
        return self.loan/100 * self.favor
    
    def menu(self, balance):
        # TODO: add loan system        
        print("Take out a loan, pay due interest or repay debt?:")
        print("Take out(1)?        Pay due itnerest(2)?          Repay(3)?")
        choice = input("Your Choice?: ")
    
        if choice == "1":
            takeLoan()
    
