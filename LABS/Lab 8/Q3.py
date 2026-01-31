class InvalidAgeException(Exception):
    pass
try:
    input_num = int(input("Enter a number: "))
    if input_num < 18:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
        
except InvalidAgeException:
    print("Exception occurred: You Can't Vote")