try:
    f = open("Anurag.txt","w")
    text = ["Hello, My name is Anurag.\n","I am MCA B3 Student.\n","Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n","sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n","Ut enim ad minim veniam.\n","quis nostrud exercitation ullamco laboris.\n","nisi ut aliquip ex ea commodo consequat.\n","Duis aute irure dolor in reprehenderit.\n","in voluptate velit esse cillum dolore eu.\n","fugiat nulla pariatur Excepteur sint."]
    f.writelines(text)
except:
    print("Unable to Open file")
finally:       
    f.close()

