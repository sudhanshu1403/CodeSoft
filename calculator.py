print ("Basic Mathematical Calculator")
num1 = input("enter the first number")
operator = input("Enter operator (+, -, *, /, %):")
num2 = input("Enter secnd Number")

if operator == "+":
    print(int(num1) + int(num2))

elif operator == "-":
    print(int(num1) - int(num2))

elif operator == "*":
    print(int(num1) * int(num2))

elif operator == "/":
    print(int(num1) / int(num2))

print("Thank You!")