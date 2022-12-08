class BankAccount:

    no_of_cust = 0
    acc_num = 42010
    
    def __init__(self, name, mobile_no, initial_depo, pin):
        
        self.name = name
        self.cust_acc_num = BankAccount.acc_num
        self.mobile_no = mobile_no
        self.acc_balance = initial_depo
        self.pin = pin
        
        BankAccount.acc_num = BankAccount.acc_num + 1 
        BankAccount.no_of_cust = BankAccount.no_of_cust + 1
        
    def basic_details(self):
        print(f"\nUser: {self.name}\t\t\t Account No: {self.cust_acc_num}\t\t Balance: {self.acc_balance} Pesos\n"
              
    def deposit(self):
        print("\n***********************************************************")
        print("|\t\t\t\t\t\tDEPOSIT    \t\t\t\t\t\t  |")
        print("*******************************************************")
        amount= int(input("Enter the Amount to Deposit => "))
        try:
            amount > 0
            self.acc_balance = self.acc_balance + amount
            print(f"\n>>>> TRANSACTION COMPLETED. Current Balance =>  {self.acc_balance} Pesos <<<<")
       except:
            print("\n\t>>>> INVALID AMOUNT!! TRANSACTION ABORTED <<<<")
    
    def payment(self, other):
        print("\n***********************************************************")
        print("|\t\t\t\t\t\tPAYMENT\t\t\t\t\t\t\t  |")
        print("***********************************************************")
        amount = int(input("Enter the Amount to Pay => "))
        try:
            amount <= self.acc_balance and amount > 0
            self.acc_balance = self.acc_balance - amount
            other.acc_balance= other.acc_balance + amount
            print(f"\n>> TRANSACTION COMPLETED. Current Balance: {self.acc_balance} Pesos <<")
        except:
            print("\n\t>>>> INVALID AMOUNT!! TRANSACTION ABORTED <<<<")
              
    def withdraw(self):
        print("\n***********************************************************")
        print("|\t\t\t\t\t\tWITHDRAW\t\t\t\t\t\t  |")
        print("***********************************************************")
        amount = int(input("Enter the Amount to Withdraw => "))
        try:
            amount <= self.acc_balance and amount > 0
            self.acc_balance = self.acc_balance - amount
            print(f"\n>> TRANSACTION COMPLETED. Current Balance: {self.acc_balance} Pesos <<")
        except:
            print("\n\t>>>> INVALID AMOUNT!! TRANSACTION ABORTED <<<<")
              
if __name__ == '__main__':

    cust1 = BankAccount(name="KEN ",    mobile_no=987654321, initial_depo=1000, pin=1232)
    cust2 = BankAccount(name="JAN JAN", mobile_no=98765432, initial_depo=2000, pin=4561)
   
   
