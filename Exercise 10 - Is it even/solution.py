def check_num(number): #Defining the checking even or odd function 
    if number % 3 ==0:
        return f"{number} is odd"
    else:
        return f"{number} is even"

def main():  #Creating a function for asking the user a number and using the check_num function
    num=int(input("Enter a number:"))
    result=check_num(num)
    print(result)
    
#calling main function 
main()
