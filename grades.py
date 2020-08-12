# Program for grades

# Modules needed
import statistics as s

# For this work, we will have a pre-declared dictionary
gradeDict = {
    "Kelly":[89,88],
    "Jessy":[92,90],
    "Jack":[95,70],
    "Samantha":[78,80]
}

# This tuple has the user and password to use the program, tuple is used to ensure that no other user and password can be added
admin_user = ("Mario", "pass")

# This flag will work to exit the program
global_flag = 0

# This loop works as a login screen
while global_flag == 0:
    # We ask the user for their username and password
    user_info = input("Username: ")
    pass_info = input("Password: ")

    # Both inputs are checked with the tuple to verify that the information is correct
    if((user_info == admin_user[0]) & (pass_info == admin_user[1])):

        # If it is we let the user know and change the value of the flag to exit the loop
        print("Access granted")
        global_flag = 1

    else:

        # If not, we notify the user and the info will be asked again
        print("Access denied")


# This loop works as the main menu
while global_flag == 1:
    # First, we will print the menu
    print("Welcometo Grade Central")
    print("[1] - Enter Grades")
    print("[2] - Remove Student")
    print("[3] - Student Average Grades")
    print("[4] - Exit")

    # We ask the user what it wishes to do
    select = input("What would you like to do today? ")

    # Option 1 - Enter Grades
    if(select == "1"):
        # We ask for a student and the grade to add to the dictionary
        student = input("Student Name: ")
        grade = input("Grade: ")
        print("Adding Grade...")

        # The grade value needs to be turned to int
        int_grade = int(grade)

        # Now we add the grade to the student selected
        gradeDict[student].append(int_grade)

        # Show the updated dictionary
        print(gradeDict)



    # Option 2 - Remove Student
    if(select == "2"):
        # We ask for the student to delete
        student = input("Student Name: ")
        print("Deleting Student...")

        # We remove the student from the dictionary
        del gradeDict[student]
        print("Student Removed")

        # Show the updated dictionary
        print(gradeDict)



    # Option 3 - Student Average Grades
    if(select == "3"):
        # We ask for a student
        student = input("Student Name: ")
        print("Obtaining average...")

        # We get the grades from the dictionary
        grades = gradeDict[student]

        # From statistics, we use mean to get the average
        grade_ave = s.mean(grades)

        # The information is printed
        print("Student:", student)
        print("Average of Grades:", grade_ave)


    # Option 4 - Exit
    if(select == "4"):
        global_flag = 0