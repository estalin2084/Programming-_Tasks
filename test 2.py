employees = {
    123: {'First Name': 'Joe', 'Last Name': 'Black','Job position': 'Production Worker'},
    234: {'First Name': 'Veronica', 'Last Name': 'White','Job position': 'Production Worker'},
    421: {'First Name': 'Ali', 'Last Name': 'East','Job position': 'Manager'}
}

print("Hi! Use this program to update job position of an employee.")





employeeToPromote = int(input("\nPlease enter the employee id of the employee whose job position you would like to update: "))   
while not (employeeToPromote in employees.keys()):
    employeeToPromote = int(input("\nPlease enter the correct employee id of the employee whose job position you would like to update: "))
newPosition = (input("Please enter the new job position for the employee: "))

for employeeId, employeeInfo in employees.items():


    if employeeToPromote == employeeId:
    
    
        employees[employeeToPromote]['Job position'] = newPosition

        print("\nJob position of the employee with employee id {} has been changed to '{}'."
            "\nHere is the employees's current info on file: \n".format(employeeId, newPosition))
    
    
        print("Employee Id: \t{0} ".format(employeeId))

        for key in employeeInfo:
            print("{0}: \t{1}".format(key, employeeInfo[key]))

        break