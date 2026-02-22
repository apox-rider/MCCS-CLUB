import time

detailList=[]

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
            product=input("Input product name")
            if product.lower().strip()=="done":
                fill=False
                break
            else:
                price=input("Input product price")
                register={
                    "name":product,
                    "price":price
                }
                detailList.append(register)


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