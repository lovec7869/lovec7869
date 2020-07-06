# Write a program that keeps a running total of the number of bugs collected during the five days.
# the loop should ask for the number of bugs collected for each day
# when the loop is finished, the program should display the total number of bugs collected.
# july 2 2020
# CTI-110 P4T2 - Bug Collector
# Carlando Love

# Define the variables.
days = 5
bugs_total = 0

# Create the loop that asks the user for the amount of bugs collected each day.

for count in range (days):
  bugs=int(input('How many bugs did you collect?'))
  print('You collected,' , bugs ,'bugs')
  bugs_total=bugs_total+bugs
print('Your bug total is,' , bugs_total) 

