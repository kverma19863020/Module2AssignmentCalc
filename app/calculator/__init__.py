from app.operations import addition, subtraction, division ,multiplication
def calculator():

    print("Welcome to the calculator REPL! Type 'exit' to quit")

    while True:

        calc_input = input ("Enter an operation (add, subtract, multiply, divide) and two numbers, or 'exit' to quit: "))
        if calc_input.lower() == "exit" :
            print ("Exiting Calc... Have a good day!")
            break
        
        try:
            operation, num1, num2 =calc_input.split()
            num1 ,num2 = float(num1) ,float(num2)
        except ValueError:
             print("Invalid input. Please follow the format: <operation> <num1> <num2>")
             continue

        if  operation == "add":
            result = addition(num1, num2)
        elif operation == "subtract":
            result = subtraction(num1, num2)
        elif operation == "multiply":
            result = multiplication(num1, num2)
        elif operation =="divide":
            try:
                result = division(num1, num2)
            except ValueError as e:
                print(e)
                continue
        else:
            print(f"Unknown operation: {operation}. Please use add, subtract, multiply, or divide.")
            continue
        print(f"Result: {result}")
        


