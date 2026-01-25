totalIncome=[]
incomeAmount=[]
totalExpenses=[]
expenseAmount=[]

numberOfIncomeEntry=int(input("Input number of income entry:  "))
count=numberOfIncomeEntry
try:
    while count>0:
        income=int(input( "Income added:  "))
        incomeAmount.append(income)
        count-=1
        totalIncome=sum(incomeAmount)
    
    
    numberOfExpenditure=int(input("Input number of expense transactions:  "))
    nom=numberOfExpenditure    
    while nom>0:
            expense=int(input( "Expense ammount:  "))
            expenseAmount.append(expense)
            nom-=1
            totalExpenses=sum(expenseAmount)

    # print(totalIncome)
    # print(expenseAmount)

    am3=max(expenseAmount)
    am5=min(expenseAmount)

    # print(totalExpenses)

    balance=totalIncome-totalExpenses
    transactionList=expenseAmount.append(incomeAmount)
    totalTransaction=len(incomeAmount)+len(expenseAmount)
    am1=len(incomeAmount)
    am2=len(expenseAmount)-1
    am4=max(incomeAmount)
    am6=min(incomeAmount)
    print(f"Total number of transactions is { am1+am2}")
    print(f"The highest transaction is {max(am3,am4)}")
    print(f"The lowest transaction is {min( am5,am6)}")
    if balance<0:
            print("Warning!!!!!! Total expenses are greater than balance, beaware of your expenditure")
    elif balance>0:
            print(f"Account balance is {totalIncome-totalExpenses} ")
    elif balance==0:
            print("Your account balance is zero(0)")
     
except ValueError:
    print("Input Error during Entry")




# sorted()

# list()

# map()

# filter()

# people=[]

# sorter_people=sorted(people, key=lambda x:x["age"])

# filter_people=list(filter(lambda x:x%0,people))



# recursion

# insertion algorithm

# deletion algorithm

# search algorithm

