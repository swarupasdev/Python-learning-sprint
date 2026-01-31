def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print("The result is:", result)

divide(10, 2)  

divide(10, 0)