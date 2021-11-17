# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# TErickson,11.10.2021,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# dicRow = {"Task":"1", "Priority":"Bob Smith"}
# dicRow1 = {"Task", "Priority"}
# List to File
objFile = open("ToDoList.txt", "w")
dicRow = {"task": "TASK", "priority": "PRIORITY"}
objFile.write(dicRow["task"] + ',' + dicRow["priority"] + '\n')
dicRow1 = {"task": "Pay Bills", "priority": "High"}
objFile.write(dicRow1["task"] + ',' + dicRow1["priority"] + '\n')
dicRow2 = {"task": "Feed the Cat", "priority": "High"}
objFile.write(dicRow2["task"] + ',' + dicRow2["priority"] + '\n')
dicRow3 = {"task": "Pull Weeds", "priority": "Low"}
objFile.write(dicRow3["task"] + ',' + dicRow3["priority"] + '\n')
objFile.close()
lstTable = [dicRow,dicRow1, dicRow2, dicRow3]


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("\n--- Current Data")
        for objRow in lstTable:
            print(objRow)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        while(True):
            strTask = input("Enter a Task: ")
            strPriority = input("Enter a Priority - High, Medium, or Low: ")
            lstTable.append({"task": strTask, "priority": strPriority})
            objFile = open("ToDoList.txt", "a")
            dicRow = {"task": strTask, "priority": strPriority}
            objFile.write(dicRow["task"] + ',' + dicRow["priority"] + '\n')
            objFile.close()
            strChoice1 = input("Exit? ('y/n'): ")
            if strChoice1.lower() == 'y':
                break
            continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        objFile = open("ToDoList.txt", "r")
        strTask = str(input('What task would you like to remove? '))
        for row in lstTable:
            if row["task"].lower() == strTask.lower():
                lstTable.remove(row)
                print('Row removed')
            else:
                print('Row not found')
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(str(row['task']) + ',' + str(row['priority']) + '\n')
        objFile.close()
        print(" Congratulations!  You saved the data!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Thank you for choosing this script! Have a great day!")
        break  # and Exit the program
