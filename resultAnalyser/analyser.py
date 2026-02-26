import time

studentDetails=[]
scores=[]
print("Welcome to Student Analyzer")
totalStudents=int(input("Enter the number of students in your class : "))

def average():
    total=sum(student['score'] for student in studentDetails)
    count=len(studentDetails)
    av=total/count
    print(f"Average Score: {av}") 

def scoreDisplay():
    if not scores: 
        print("No scores found ")
    else:
        lowestScore=scores[0]
        highestScore=scores[0]
        for num in scores[1:]:
            if num<lowestScore:
                lowestScore=num 
            elif num>highestScore:
                highestScore=num
        print(f"Highest Score: {highestScore}")
        print(f"Lowest Score: {lowestScore}") 
try:
    if totalStudents<0:
        print("Number of students can only be positive, please re-fill ") 
    elif totalStudents==0:
        print("The class is empty, no details to collect")
    elif totalStudents>0:
        print(f"Your class has {totalStudents} students ")
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
            print("Credentials added")
            time.sleep(3)
    print("Loading Calculations... ")
    time.sleep(2)
    print("Evaluating highest score, lowest and average score....")
    time.sleep(3)
    scoreDisplay()
    average()
except ValueError:
    print("Invalid input")
 
 


