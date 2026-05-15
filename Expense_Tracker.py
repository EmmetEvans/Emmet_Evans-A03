'''
This is the expense tracker, the place where you can track all of my expenses from the last month.

Inputs:
- Program will ask if you want to look at category totals, biggest single expense, expenses above a limit, or expenses containing
a certain word or phrase.

Processes:
- Accumulator for each category
- Max expense identification
- Expense threshold identification
- User input word or phrase detection

Output:
- A message containing the desired tracker usage after each user input
'''

My_expenses = {
    "food":{
        "Groceries":64.96,
        "Taco Bell":300.19,
        "Library Vending Machine":2.75,
        "Smith Fieldhouse Vending Machine":1.65,
        "Joseph F Smith Building Vending Machine":3.5,
        "MOA Cafe":14.32,
        "J Dawgs":6.24
    },
    "utilities":{
        "Electricity":17.11,
        "Internet":4.80,
        "Gas":9.22
    },
    "school":{
        "Tuition":432.00,
        "Transcript Copy":20.00,
        "Printing":0.16,
        "Stupid Dumb Really Expensive Textbook":115.41
    },
    "fun stuff":{
        "Deep Rock Galactic":20.00,
        "Magic: The Gathering Precon":99.87,
        "Movie Ticket Project Hail Mary":12.21,
        "Hollow Knight: Silksong DLC":25.00,
    },
    "other":{
        "Haircut":22.13,
        "Costco Pants":12.56
    }
}

#Input
total = 0
highest = ""
print("Welcome to my expense tracker!")
choice = "Undone"
while choice != "Done":
    choice = input("\nPlease choose one of the following options (1, 2, 3, or 4):"
                           "\n1: See spending category totals"
                           "\n2: See biggest expense from the month"
                           "\n3: See all expenses above a certain threshold"
                           "\n4: Find a particular expense"
                           "\nType 'Done' when you're finished!" ).title()
    if choice == "1":
        total = 0
        category = input("What category would you like to look at? Your options are:"
                         "\nfood"
                         "\nutilities"
                         "\nschool"
                         "\nfun stuff"
                         "\nother\n").lower()
        for expense in My_expenses:
            if expense == category:
                for type in My_expenses[expense]:
                    total += My_expenses[expense][type]
        if total != 0:
            print(f"\nThe total amount of money spent on {category} this month was ${total:.2f}.\n")
        else:
            print(f"\n{category} is not an option.")
    elif choice == "2":
        total = 0
        highest = ""
        for expense in My_expenses:
            for type in My_expenses[expense]:
                if My_expenses[expense][type] > total:
                    total = My_expenses[expense][type]
                    highest = type
        print(f"\nThe biggest single expense this month: {highest}, which cost ${total}")
    elif choice == "3":
        floor = input("What is the threshold you would like to set? Enter a positive number: ")
        above_floor = []
        if floor.replace(".","",1).isdigit():
            floor = float(floor)
            for expense in My_expenses:
                for type in My_expenses[expense]:
                    if My_expenses[expense][type] > floor:
                        above_floor.append(type)
            print(f"\nThese are the expenses that were higher than ${floor:.2f} this month: {above_floor}")
        else:
            print("\nSeems like you didn't enter a positive number like I told you to.")
    elif choice == "4":
        choice_expense = ""
        choice2 = input("\nPlease enter a word or phrase. We will search for this word or phrase in this month's expenses. ").title()
        choice_ok = choice2.replace(".","",1).isdigit()
        if not choice_ok:
            for expense in My_expenses:
                for type in My_expenses[expense]:
                    if choice2 in type:
                        choice_expense = type + "-$" + str(My_expenses[expense][type]) + " "
            print(f"\nBased on your input of {choice2}, we found the following items: {choice_expense}")
        else:
            print("\nI SAID enter a word or phrase. Do not enter a number.")
    elif choice == "Done":
        choice = "Done" #This is kind of redundant, but it makes it so that typing 'done' doesn't print the else path stuff
    else:
        print("\nThat's not one of the options you goofer! Try again.")



                    
                    
