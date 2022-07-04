#bank
#3-method account_creation,withdraw,deposit
class Bank:
    bankname='SBI'
    def account_creatiion(self,name,acc_no):
        self.name=name
        self.acc_no=acc_no
        self.min=3000
        self.balance=self.min
        print("Your",Bank.bankname,"account has been created  with",self.name," account no:",self.acc_no,"with minimum balance",self.min)

    def deposit(self,amt):
        self.amt=amt
        self.balance=self.balance+self.amt
        print("Your",Bank.bankname,"account has been credited with",self.amt)
        print("Your Account balance is",self.balance)

    def withdraw(self,amount):
        self.amount=amount
        if amount>self.balance:
            print("Insufficient Balance")
        else:
            self.balance=self.balance-amount
            print("Your account has been debited",self.amount)
            print("Your account balance is",self.balance)

ob=Bank()
ob.account_creatiion("Ajith",180021094113)
ob.deposit(10000)
ob.withdraw(5000)

