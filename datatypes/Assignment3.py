print("You are welcome to the basic operators of the following arithmetic operations: addition, subtraction, multiplication, modulo, and division")

response = True

while response:
    operation = input("Enter operation (addition, subtraction, multiplication, modulo, division:)").lower()

   
    value1 = int(input("What is the first value you would like to operate on? "))
    value2 = int(input("What is the second value you would like to operate on? "))

    if operation == 'addition':
        answer = value1 + value2
    elif operation == 'subtraction':
        answer = value1 - value2
    elif operation == 'multiplication':
        answer = value1 * value2
    elif operation == 'division':
        answer = value1 / value2
    elif operation == 'modulo':
        answer = value1 % value2
    elif operation == 'exponet':
        answer = value1 ** value2
    else:
        print(f'{operation} is an Invalid Input')

    print(f"The answer of {value1} {operation} {value2} is = {answer}")
    print('That is a simple operation you should know, anyways i am here for you')

    further_request = input("Do you want to continnue with other calculation, Enter y/n:")

    if further_request.lower() == "n":
        print('Thanks for using our service')
        response = False
    elif further_request.lower() == "y":
        response = True
    else:
        print("Invalid Input try again!, we would continue the operation.")

