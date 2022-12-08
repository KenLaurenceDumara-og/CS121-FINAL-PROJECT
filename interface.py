from playsound import playsound
playsound('BANKSOUND.mp3')
from Bank import BankAccount

customer_dict = {}              # use account no. as key and class object(customer account) as value
mobile_acc_link = {}            # use mobile no. as key and store account no. as value, for linking purpose

def sign_up():
    name = input("Enter your Name => ")
    mobile_no = int(input("Enter Your Mobile Number => "))
    initial_depo = int(input("Enter the Initial Deposit Amount => "))
    if initial_depo <= 0:
        print("Invalid Amount")
        return
    
    pin = int(input('Create PIN: '))
    customer = BankAccount(name=name, mobile_no=mobile_no, initial_depo=initial_depo, pin=pin)
    customer_dict[customer.cust_acc_num] = customer                 # acct. no. stored as key and oject as value
    mobile_acc_link[customer.mobile_no] = customer.cust_acc_num     # mobile no. linked
    print("\n\t\t\t>>>> Signing Up!!! <<<<\n")
    print(f">> {customer.name} Welcome to Our Bank. {customer.cust_acc_num} is your Account Number. <<")

def login():
    print("\n***********************************************************")
    print("|\t\t\t\t\t\tLogin \t\t\t\t\t\t\t  |")
    print("***********************************************************")
    account_no = int(input("Enter your Account Number => "))
    account_pin = int(input("Enter your Pin => "))
    if account_no in customer_dict.keys() and account_pin == customer_dict[account_no].pin :
        print(f"\n\t>>>>> {customer_dict[account_no].name} CONGRATS! Successfully Logged In! <<<<")
        customer_dict[account_no].basic_details()
    
        
