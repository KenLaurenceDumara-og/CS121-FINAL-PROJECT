class BankAccount:

    no_of_cust = 0
    acc_num = 42010
    
    def __init__(self, name, mobile_no, initial_depo, pin):
        
        self.name = name
        self.cust_acc_num = BankAccount.acc_num
        self.mobile_no  = mobile_no
        self.acc_balance = initial_depo
        self.pin = pin