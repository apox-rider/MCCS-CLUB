import time

studentDetails=[]
scores=[]
passedStudents=[]
failedStudents=[]
print("Welcome to Student Management System")
totalStudents=int(input("Enter the number of students in your class : "))

def average():
    total=sum(student['score'] for student in studentDetails)
    count=len(studentDetails)
    av=total/count
    print(f"Average Score: {av}")

def haspassed():
    if score>=50:
        passed=details["name"]
        passedStudents.append(passed)

def hasfailed():
    if score<50:
        failed=details["name"]
        failedStudents.append(failed)
def highestScorer():
     highestscore =details["score"]
     for num in details["score"]:
         if num>highestscore:
             print (f"The highest scorer is {details['name']}.")

try:
    if totalStudents<0:
        print("Number of students can only be positive, please re-fill")
    elif totalStudents==0:
        print("The class is empty, no details to collect")
    elif totalStudents>0:
        print(f"Your class has {totalStudents} students")
        time.sleep(2)
        print("Count Saved Successfully")
        time.sleep(2)
        print("Preparing registration manual...")
        time.sleep(2)
        while totalStudents:
            name=input("Input Student's name:  ")
            time.sleep(2)
            score=int(input("Input corresponding scores:  "))
            details={
                "name": name,
                "score":score
            }
            totalStudents-=1
            scores.append(score)
            studentDetails.append(details)
            haspassed()
            hasfailed()
            print("Credentials added")
            time.sleep(3)
    print("Loading Calculations...")
    time.sleep(2)
    print("Evaluating average score and highestscorer.... ")
    time.sleep(3)
    average()
    highestScorer()

except ValueError:
    print("Invalid input")
 
 


