import time
from datetime import datetime

detailList=[]
prices=[]
items=[]

def record():
    time.sleep(3)
    print("Initializing system...")
    time.sleep(4) 
    print("ACTIVITIES")
    activity=input("A:Input product details \nB:Exit \nOption : ")
    if activity.strip().capitalize()=="A":
        fill=True
        print("Type 'done' on finishing the product details")
        time.sleep(2)
        while fill:
            product=input("Input product name : ")
            if product.lower().strip()=="done":
                fill=False
                break
            else:
                try:
                    quantity=int(input("Input product quantity : ")) 
                    units=input("Input product unit : ")
                    price=input("Input product unit price : ")
                    register={
                        "name":product,
                        "quantity":f"{quantity} {units}", 
                        "price":price,
                    }
                    detailList.append(register) 
                    all=int(price*quantity)
                    prices.append(all)
                    items.append(product)
                    time.sleep(3)
                    print(f"Added {quantity}{units} of {product} to purchased list.")
                    time.sleep(3)  
                except ValueError:
                    print("Invalid Input")
                    
    elif activity.upper().strip()=="B": 
        close=True
        time.sleep(3)
        while close:
            break
    else:
        time.sleep(2)
        print("invalid option. ")
        print("System break!!")
        

def total():
    time.sleep(3)
    value=sum(prices)
    if value>50000:
        print("Initiating discount...")
        time.sleep(3)
        final=0.9*value
        print(f"The total fixed ammount is {round(final,2)}")
    elif value>0:
        print(f"The total fixed amount is {round(value,2)}")
    else:
        print("No transaction detected")

def receipt():
    time.sleep(3)
    print("Receipt")
    print(f"You've bought {detailList} at {datetime.now()}")



print("Welcome to the supermarket shopping system!")
time.sleep(3)
permission=input("Want to proceed? (yes/no) : ")
if permission.lower().strip()=="yes":
    record()
    receipt()
    total()
    
elif permission.lower().strip()=="no":
    time.sleep(3)
    print("Welcome Again")
else: 
    time.sleep(3)
    print("Invalid input , your options are (yes/no)")
    print(permission)