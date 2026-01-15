import time
# register
studentDetails=[ ]
print("Welcome to Student Analyzer!")
no = int(input("How many students are there in class?"))
if no < 0:
    print("Number of students can't be negative")
elif no == 0:
    print("The class is empty")
elif no>0:
    print(f"The class has {no} students")
    message=print(f"Please register,one after another") 
    time.sleep(0.08)
    while no > 0:
        name=str(input("Enter Student name : "))
        score=int(input("Fill corresponding score: "))  
        details={
            'name' : name,
            'score': score
        }       
        studentDetails.append(details)
        time.sleep(2)
        print("Student details added")
        time.sleep(2)
        no -= 1
        print(...,end='\r',flush=True)
    print("Registered")
    print("loading list...")
    time.sleep(3)


# Average calc
count=len(studentDetails)
total=sum(student['score'] for student in studentDetails)
average=total/count

# Display for Highest score
print(max(student['score'] for student in studentDetails))
# Display for lowest score
print(min(student['score'] for student in studentDetails))
# Display for Highest score
print(average)



