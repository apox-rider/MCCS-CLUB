import time
totalBalance=10000
 
def menu():
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Exit")

def check_balance():
     print("Calculating....")
     time.sleep(2)
     print(f"Your balance is {totalBalance}")

def make_deposit():  
    global totalBalance 
    try:
        depAmmount=int(input("How much do you want to deposit?"))
        if depAmmount<=0:
            print("No deposit done,can only add positive amount. ")
        else:
            totalBalance += depAmmount
            print(f"{depAmmount} added in account")
            print(f"Your new balance is {totalBalance}")
    except ValueError:
        print("Invalid input")

def make_withdrawal():
    global totalBalance
    try:
        amount=int(input("How much doyou want to withdraw?"))
        if amount<=0:
            print("No withdrawal done, minimum withdrawal amount not reached")
        elif amount>totalBalance:
            print("Amount insufficient")
        elif amount<=totalBalance and amount>0:
            totalBalance -= amount
            print(f"{amount} withdrawn successfully.")
            print(f"Remaining balance is {totalBalance}")
    except ValueError:
        print("Invalid Input. Fill correct data")

def exit():
    print("Thank you for using our ATM. Welcome again!")

print("Welcome to the ATM Simulation")
time.sleep(2)

response = input("Want to open menu?  (yes/no): ").strip().lower()
if response == "yes":
    print("Menu loading...")
    time.sleep(10)
    
    while True:
        menu()
        try:
            choice = int(input("Make a choice (1-4):  "))
            
            if choice == 1:
                check_balance()
            elif choice == 2:
                make_deposit()
            elif choice == 3:
                make_withdrawal()
            elif choice == 4:
                exit()
                break    
            else:
                print("Invalid choice. Please select 1–4.")
        except ValueError:
            print("Please enter number 1-4 ")
else:
    print("ATM Closed. Welcome again! ")


 