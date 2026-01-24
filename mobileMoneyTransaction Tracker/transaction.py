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
    try:
        while nom>0:
            expense=int(input( "Expense ammount:  "))
            expenseAmount.append(expense)
            nom-=1
            totalExpenses=sum(expenseAmount)
        balance=totalIncome-totalExpenses
        transactionList=expenseAmount.append(incomeAmount)
        totalTransaction=len(incomeAmount)+len(expenseAmount)
        print(f"Total number of transactions is {len(transactionList)}")
        print(f"The highest transaction is {max(max(incomeAmount) and max(expenseAmount))}")
        print(f"The lowest transaction is {min(min(incomeAmount) and min(expenseAmount))}")
        if balance<0:
            print("Warning!!!!!! Total expenses are greater than balance, beaware of your expenditure")
        elif balance>0:
            print(f"Account balance is {totalIncome-totalExpenses} ")
        elif balance==0:
            print("Your account balance is zero(0)")
    except ValueError:
        print("Input Error  ")
except ValueError:
    print("Input Error during Entry")

