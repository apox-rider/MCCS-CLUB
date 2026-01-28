**Problems solved** 
1. Students Result Analyzer.
2. Simple ATM Simulation.
3. Number Pattern Generator.
4. Password Validator.

**Language used**;
    PYTHON

**How to run the program** 
PROGRAM RUNNING IN TERMINAL
1. Students Result Analyzer
When in the directory folder ,run: python3 analyser.py

2. Simple ATM Simulation
When in the directory folder ,run: python3 simulator.py

3. Number Pattern Generator
When in the directory folder ,run: python3 generator.py

4. Password Validator
When in the directory folder ,run: python3 validator.py

**Explanation of my Logic** 
1. Students Result Analyzer<br>
    Logic: <br>
      ⭐️It has the varriables that store arrays of the student details; the name and scores 

      ⭐️It has input section for the class number of students

      ⭐️It has got a loop that is limited to the number of students in the class to register names and the scores

      ⭐️The project has got two functions which are called  ; 
    <div>
-the average()<br>
            a.It calculates the total from the input scores 
            b.It counts the number of students
            c.It carries the formula to calculate the average which it solves using the variables of total obtained and the counts of number of students
            d.It prints the average score  

-scoreDisplay()<br>
            a.It conditionally identifies scores depending on the user input.
            b.It considers the first input as the reference for obtaioning the lowest score and the highest score 
            c.It prints the finall data of the lowest score and the highest score
</div>

2. Simple ATM Simulation<br>
    Logic: <br>
     
      ⭐️It has the variable that store balance data starting with the initial value of 10000
     
      ⭐️The project has got five functions which are called  ; 
    <div>
-the menu()<br>
            It prints the features included in the menu depending on user demands

-check_balance()<br>
            It prints the value of the present total balance

-make_deposit()<br>
            a. It updates the value of the total balance by adding positive amount eliminating errors of the user input like the if ammount is 0 or -ve , it handles the errors 
            b. It updates the value of the totalBalalnce 
            
-make_withdrawal()<br>
            a. It demands input of ammount the user wants to withdraw.
            b. The conditionals handle the invalid amount other than the ammount greater than 0.
            c. It updates totalAmount buy deducting from the total balance .

-exit()<br>
            prints to notify user for the program break if the user wants to end it.
    </div>

      ⭐️Its logically arranged using if-else statements which are enclosed with the while loop to keep the menu function that provide wide options for the user input and operation as well as choice


3. Number Pattern Generator<br>
    Logic:<br>

      ⭐️It is assembled with nested for loops to organise rows in outer loop and fills per row in inner for loop . The try-except handles the vallue errors , within the while loop 


4. Password Validator<br>
    Logic:<br>

      ⭐️The password validator program has a single function which is the password_Checker() thatdemands user input and checks the length of input which should have 8 or more characters using conditionals and then on verification , checks for presence of a number within the charactors to conclude print as valid if both conditions are met or invalid if either or all conditions arent met which in the end is printed out whether valid or invalid

4. QrCode Generator<br>
    Logic:<br>

      ⭐️The qrcode generator generates the qrcode on input of the a link 

 
             
