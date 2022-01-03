import random
import datetime
class Account:
    def __init__(self, id, balance =0, annualInterestRate = 3.4):
        self.id = id
        self.balance = balance 
        self.annualInterestRate = annualInterestRate
    def getid(self):
        return self.id
    def getbalance(self):
        return self.balance
    def getannualInterestRate(self):
        return self.annualInterestRate
    def getMonthlyInterestRate(self):
        return self.annualInterestRate/ 12
    def withdraw(self, amount):
        self.balance -= amount
    def deposit(self, amount):
        self. balance += amount
    def getMonthlyInterest(self):
        return self.balance * self.getMonthlyInterestRate()
def main():
        accounts =[]
        for i in range(1000,9999):
            account = Account(i, 0)
            accounts.append(account)
        while True:
            id = int(input("Enter account pin:"))
            while id < 1000 or id > 9999:
                id = int(input("Invalid id.....check your pin:"))
            while True:
                print("""1- view Balance,2-Withdraw,3-Deposit,4-Exit""")
                selection = int(input("Enter your selection:"))
                for acc in accounts:
                    if acc.getid()  == id:
                        accountObj = acc
                        break
                if selection == 1:
                    print(accountObj.getbalance())
                elif selection == 2:
                    amt = float(input("Enter amount to Withdraw:"))
                    ver_withdraw = input("Is this the correct amount, Yes or No ?" +str(amt) + "")
                    if ver_withdraw == "Yes":
                        print("Verify Withdraw")
                    else:
                        break
                    if amt < accountObj.getbalance():
                        accountObj.withdraw(amt)
                        print("Updated Balance: " + str(accountObj.getbalance())  + "n")
                    else:
                        print("Your balance is less than withdrawal amount :" + str(accountObj.getbalance()) + "n")
                        print("Please make a deposit.");
                elif selection == 3:
                    amt = float(input("Enter amount to deposit: "))
                    ver_deposit = input("Is this the correct amount, Yes, or No ?" + str(amt) + "")
                    if ver_deposit == "Yes":
                        accountObj.deposit(amt);
                        print("Updated Balance:" + str(accountObj.getbalance()) + "n")
                    else:
                        break
                elif selection ==  4:
                    print("Transaction is now complete.")
                    print("Transaction number :", random.randint(10000,1000000))
                    print("Current Interest Rate :", accountObj.annualInterestRate)
                    print("Monthly Interest Rate:", accountObj.annualInterestRate /12)
                    print("Thanks for choosing us as your bank")
                    exit()
                else:
                    print("That's an invalid choice.")
x = datetime.datetime.now()
print(x)
main()
