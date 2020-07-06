# Create a expense calculator
# CTI-110
# P4HW1 - Expenses
# july 4 2020
# Carlando Love

userBudget = float( input( "enter how much you've budget" + \
                          " for the month $"))

moreExpenses = "y"
userTotalExpenses = 0

while moreExpenses == "y":
    userExpenses = float(input( "enter an expense:$"))
    userTotalExpenses += userExpenses
    moreExpenses = input( "do you have another expense?: type y"+\
                          " for yes, type n for no: " )

print()    
if userTotalExpenses > userBudget:
    print( "you were over budget of $",format(userBudget,",.2f"), \
           "by $", format( userTotalExpenses - userBudget,",.2f"))
elif userBudget > userTotalExpenses:
    print( "you were under budget of $",format(userBudget,",.2f"), \
           "by $", format( userBudget - userTotalExpenses,",.2f"))
else:
    print( "You were right on budget. Great Job!") 
           

input("press enter to exit.")
           
