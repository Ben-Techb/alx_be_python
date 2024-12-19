num1 =float(input("enter the first number  "))
num2 = float(input("enter the second number"))
operatoin = input("Choose the operation (+, -, *, /):")
match operatoin:
    case "+":
        result = num1 + num2
        print(f"The result is{result}")
    case "-":
        result = num1 - num2
        print(f"the result is {result}")
    case "*" :
        result = num1 * num2 
        print(f" the result is {result}")
    case "/" :
        if num2 != 0 :
            result = num1 / num2
            print(f"the result is {result}")
        else:
            print("error number can't be divided by zero")
