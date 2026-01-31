def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print("The result is:", result)
    finally:
        print("This is the finally block. It always executes.")

divide(10, 2) 

divide(10, 0)