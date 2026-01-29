print ("Welcome to the number pattern generator ")
choice=input("Want to preceed?(yes/no) ")
if choice.strip()=="yes":
    while choice:
        try:
            n = int(input("Enter a number:  "))  
            for row in range(1, n+1):            
                for number in range(1, row+1):   
                    print(number, end=" ")        
                print()                        
        except ValueError:
            print("Input not number ")
else:
    print("Pattern generator closed . " )