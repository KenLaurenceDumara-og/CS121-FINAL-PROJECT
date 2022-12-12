from playsound import playsound
playsound('banksound.mp3')
from Bank import BankAccount

customer_dict = {}              # use account no. as key and class object(customer account) as value
mobile_acc_link = {}            # use mobile no. as key and store account no. as value, for linking purpose

def sign_up():
    name = input("Enter Your Name => ")
    mobile_no = int(input("Enter Your Mobile Number => "))
    initial_depo = int(input("Enter the Amount to Deposit => "))
    if initial_depo <= 0:
        print("Invalid Amount")
        return
    
    pin = int(input("Create PIN => "))
    customer = BankAccount(name=name, mobile_no=mobile_no, initial_depo=initial_depo, pin=pin)
    customer_dict[customer.cust_acc_num] = customer                 # acct. no. stored as key and oject as value
    mobile_acc_link[customer.mobile_no] = customer.cust_acc_num     # mobile no. linked
    print("\n\t\t\t>>>> Signing Up!!! <<<<\n")
    print(f">> {customer.name} Welcome to Our Bank. {customer.cust_acc_num} is your Account Number. <<")

def login():
    print("\n***********************************************************")
    print("|\t\t\t\t\t\tLOGIN \t\t\t\t\t\t\t  |")
    print("***********************************************************")
    account_no = int(input("Enter your Account Number => "))
    account_pin = int(input("Enter your Pin => "))
    try:
        account_no in customer_dict.keys() and account_pin == customer_dict[account_no].pin 
        print(f"\n\t>>>>> {customer_dict[account_no].name} CONGRATS! Successfully Logged In! <<<<")
        customer_dict[account_no].basic_details()
    except:
        print("\n\t>>>>>> Incorrect Account Number or Pin!! <<<<<<")
        return
    while True:
        print("***********************************************************")
        print("|\t\t\t\t\tWELCOME TO OUR BANK\t\t\t\t\t  |")
        print("***********************************************************")
        print("\n\t========= Choose what you want to do in Our Bank =========")
        
       print("\t\t\t\t1. Deposit")
       print("\t\t\t\t2. Withdraw")
       print("\t\t\t\t3. Money Transfer")
       print("\t\t\t\t4. Logout")
       user_input = input("Please Enter Your Choice => ")

        if user_input1 == '1':
            customer_dict[account_no].deposit()
        elif user_input1 == '2':
            customer_dict[account_no].withdraw()
        elif user_input1 == '3':
            print("\n***********************************************************")
            print("|\t\t\t\t\t\tMONEY TRANSFER\t\t\t\t\t  |")
            print("***********************************************************")
        mobile = int(input("Enter the Mobile Number of the Recepient => "))
            if mobile in mobile_acc_link.keys():
                secondary = mobile_acc_link[mobile]             # use mobile no. to get acct. no.
                customer_dict[account_no].payment(customer_dict[secondary])
            else:
                print("\n>> The Mobile Number You Entered does not have an Account <<")
        elif user_input1 == '4':
            print("\n\n\t\t>>>> Successfully Logged Out <<<<")
            return
        else:
            print("\n\t\t>>>> INVALID INPUT PLEASE TRY AGAIN!! <<<<")
        print("_________________________________________________________")
        customer_dict[account_no].basic_details()
        
    while True:
        print("\n***********************************************************")
        print("|\t\t\t\t\tWELCOME TO OUR BANK\t\t\t\t\t  |")
        print("*********************************************************")
        print("\n\t===== Choose what you want to do in Our Bank =====")
        print("\t\t1. Sign Up (New Account Owner)")
        print("\t\t2. Login (Existing Account) ")
        print("\t\t3. Display Number of Customer ")
        print("\t\t4. Exit")
        user_input1 = input("Please Enter your Choice =>  ")

    if user_input1 == '1':
        print("\n***********************************************************")
        print("|\t\t\t\t\t\tSIGN UP\t\t\t\t\t\t\t  |")
        print("*********************************************************") 
        sign_up()
    elif user_input1 == '2':
        login()
    elif user_input1 == '3':
        print("\n>> There are Currently", BankAccount.no_of_cust,"customer/s in Our Bank. <<")
    elif user_input1 == '4':
        print("\n\t---------- THANK YOU FOR USING OUR BANK ----------")
        break
    else:
        print("\nINVALID INPUT PLEASE TRY AGAIN")
        print("___________________________________________________")
    
  
