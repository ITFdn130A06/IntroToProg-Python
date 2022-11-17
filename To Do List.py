# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# Declare variables and constants
objFileName = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strChoice = ""  # Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, Load from ToDoFile.txt into a python Dictionary.
objFile = open(objFileName, "r")
for line in objFile:
    strData = line.split(",")
    dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# Step 2 - Display a menu of choices to the user
while(True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Your to-do list is as follows:")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        continue  # to show the menu
    # Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        strTask = str(input("What task would you like to add? ")).strip()
        strPriority = str(input("What priority is the task? [High/Low]")).strip()
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        print("Current Data in table:")
        print("Your to-do list is as follows:")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        continue
    # Step 5 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        #User specification of which row to delete is based on the task-type
        strKeyToRemove = input("Which task would you like removed? - ")
        blnItemRemoved = False  # Creating a boolean Flag
        intRowNumber = 0
        for row in lstTable:
            task, priority = dict(row).values()
            if task == strKeyToRemove:
                del lstTable[intRowNumber]
                blnItemRemoved = True
            intRowNumber += 1
        if(blnItemRemoved == True):
            print("Task removed.")
        else:
            print("Task not found.")
        print('Current list is as follows:')
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        continue
    # Step 6 - Save tasks to the ToDoFile.txt file
    elif(strChoice == '4'):
        print("Your to-do list is as follows: ")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):
            objFile = open(objFileName, "w")
            for dicRow in lstTable:
                objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
            objFile.close()
            input("Your data was saved. Press Enter to return to menu.")
        else:
            input("New data was not saved. Press Enter to return to menu.")
        continue 
    elif (strChoice == '5'):
        break   # and Exit the program
