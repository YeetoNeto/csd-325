
# Noah McCarthy, 2/21/2025, Module 8.2 Assignment
#Project goal is to take a json file read it and write to it.
import json


#Function to show contents of file variable
def printStudentInfo(students):
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")
        

#Main function
def main():
    #Read JSON FILE contents and store in variable
    with open("Student.json", "r") as file:
        students = json.load(file)
    

    #Let user know it is original variable file
    print('Original Student List: \n')

    #go to function to print file
    printStudentInfo(students)


    #Adds information to the file variable
    addStudent = {
        'F_Name': 'Noah',
        'L_Name': 'McCarthy',
        'Student_ID':'00001',
        'Email':'netosisacoolone@gmail.com'
        }
    students.append(addStudent)

    print('Updated Student List: \n')
    #function prints updated variable file
    printStudentInfo(students)

    #Write to JSON file with new file variable so it is updated
    with open('Student.json', 'w') as file:
        json.dump(students,file,indent=5)

    #Let user know it is updated
    print('JSON File Updated')









#if check to potentially use this function in a future program without triggering main. Took inspiration from the textbook for this
if __name__ == '__main__': 
    main()
