from app.operations import addition, subtraction, division ,multiplication
def calculator():

    print("Welcome to the Calculator using REPL- Read ,Evaluate,Print,Loop")

    while True:

        calc_input = input ("Enter an operation to perform --> 'Add,Multiply,Subtract,Divide ")
        if calc_input.lower() == "exit" :
            print ("Exiting Calc... Have a good day!")
            break
        
        try:
            operation, num1, num2 =calc_input.split()

            num1 ,num2 = float(num1) ,float(num2)
        except ValueError:
             print("Entered Invalid Input ,Please follow format : <Operation> <num1> <num2> eg add 1 2")
        continue

        if  operation == "add":
            result = addition(num1, num2)
        elif operation == "subtract":
            result = subtraction(num1, num2)

