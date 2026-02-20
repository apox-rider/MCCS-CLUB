import time

def attendance():
    percentage=(noPresent/total)*100
    if percentage<75:
        print(f"Warning!! Warning!! Warning!!")
        time.sleep(4)
        print(f"Only {round(percentage,2)}% have attended the lesson")
    elif percentage>=75:
        print(f"{round(percentage,2)}% of the class attended")
    elif percentage==0:
        print("WARNING! WARNING!")
        time.sleep(4)
        print("No student attended the session")


present=[]
absent=[]
try:
    total=int(input("How many students are supposed to be in class? \n Number: "))
    noPresent=int(input("How many are present?\n Number: "))
    noAbsent=total-noPresent
    time.sleep(4)
    print("Registation for analysis preparing for prompt...")
    time.sleep(5)

    print("Register present student names")
    while noPresent>0:
        time.sleep(3)
        name=input("Input student name: ")
        present.append(name)
        noPresent-=1
        time.sleep(3)
        print(f"{name} registered")

    time.sleep(5)
    print("Present students registered!")
    time.sleep(5)

    print("Register absent student names")
    while noAbsent>0:
        time.sleep(3)
        absname=input("Input Absentee: ")
        absent.append(absname)
        noAbsent-=1
        time.sleep(3)
        print(f"{absname} recorded")

    time.sleep(5)
    print("Absentees registered!")
    time.sleep(5)

    print("Analysing...")
    time.sleep(4)

    attendance()
except ValueError:
    print("Invalid input")

