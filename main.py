#Ask user for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#Ask user for operation to perform
print("Enter an operation to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

#Store user's choice in a variable
choice = int(input("Enter choice (1/2/3/4): "))

#Perform operation based on user's choice
if choice == 1:
    result = num1 + num2
    print(num1,"+",num2,"=",result)
elif choice == 2:
    result = num1 - num2
    print(num1,"-",num2,"=",result)
elif choice == 3:
    result = num1 * num2
    print(num1,"*",num2,"=",result)
elif choice == 4:
    result = num1 / num2
    print(num1,"/",num2,"=",result)
else:
    print("Invalid input")