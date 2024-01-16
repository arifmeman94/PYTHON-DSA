print("Welcome to tip calculator")
bill = int(input("Please type your bill amount:\n"))
tippercent = int(input("How much percent tip you want to pay on your bill amount?\n"))
tipamount = (bill*tippercent)/100
total = tipamount+bill
person = int(input("In how many person you want to divide the bill?\n"))
print("Total bill with tip amount is:", total)
print("Each person has to pay:",total/person)