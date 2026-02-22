import time

detailList=[]
prices=[]
items=[]

def record():
    time.sleep(3)
    print("Initializing system...")
    time.sleep(4)
    print("ACTIVITIES")
    activity=input("A:Input product details :\n B:Exit ")
    if activity.lower().strip()=="A":
        fill=True
        print("Type 'done' on finishing the product details")
        time.sleep(2)
        while fill:
            product=input("Input product name : ")
            if product.lower().strip()=="done":
                fill=False
                break
            else:
                quantity=int(input("Input product quantity : "))
                price=input("Input product unit price : ")
                register={
                    "name":product,
                    "quantity":quantity,
                    "price":price,
                }
                detailList.append(register)
                prices.append(price*quantity)
                items.append(product)
                time.sleep(3)
                print(f"Added {quantity} {product} to purchased list.")
                time.sleep(3)

def total():
    time.sleep(3)
    value=sum(prices)
    if value>50000:
        print("Initiating discount...")
        time.sleep(3)
        final=0.9*value
        print(f"The total fixed ammount is {final}")
    elif value>0:
        print(f"The total fixed amount is {value}")
    else:
        print("No transaction detected")

def receipt():



print("Welcome to the supermarket shopping system!")
time.sleep(3)
permission=input("Want to proceed? (yes/no)")
if permission.lower().strip()=="yes":
    record()
    
elif permission.lower().strip()=="no":
    time.sleep(3)
    print("Welcome Again")
else: 
    time.sleep(3)
    print("Invalid input , your options are (yes/no)")
    record()