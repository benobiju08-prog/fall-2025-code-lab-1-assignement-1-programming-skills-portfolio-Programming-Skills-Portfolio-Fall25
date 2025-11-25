# Collecting user's biography information
name= input("Enter your full name: ")
hometown= input("Enter your hometown: ")
age= input("Enter your age: ")
#checks if that age is a number
while age.isdigit()==False:
    print("Invalid input. Please enter a number for age.")
    age= input("Please enter age in numbers: ")
#Displays the collected information
print('full name:', name, '\nhometown:', hometown, '\nage:', int(age))