class BankAccount:

    no_of_cust = 0
    acc_num = 42010
    
    def __init__(self, name, mobile_no, initial_depo, pin):
        
        self.name = name
        self.cust_acc_num = BankAccount.acc_num
        self.mobile_no  = mobile_no
        self.acc_balance = initial_depo
        self.pin = pin

        BankAccount.acc_num = BankAccount.acc_num + 1 
        BankAccount.no_of_cust = BankAccount.no_of_cust + 1
        
    def basic_details(self):
        print(f"\nUser: {self.name}\t\t\t Account No: {self.cust_acc_num}\t\t Balance: {self.acc_balance} Pesos\n"
              
    def deposit(self):
        print("\n***********************************************************")
        print("|\t\t\t\t\t\tDeposit    \t\t\t\t\t\t  |")
        print("*******************************************************")
        amount= int(input("Enter amount to Deposit => "))
        try:
              amount > 0
              self.acc_balance = self.acc_balance + amount
              print(f"\n>>>> Transaction completed. Current Balance: {self.acc_balance} Pesos <<<<")
       except:
              print("\n\t>>>> Invalid Amount!! Transaction Aborted <<<<")
    
    def payment(self, other):
        print("\n***********************************************************")
        print("|\t\t\t\t\t\tPayment\t\t\t\t\t\t\t  |")
        print("***********************************************************")
        amount = int(input("Enter the amount to Pay => "))

   
    
