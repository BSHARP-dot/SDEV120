# Check if x is greater then y
def is_greater(x, y):
    if x > y:
        return "true"
    else:
        return "false"

# Loop to allow multiple entries or quit
while True:
    # User input for variables a and b
    a = input("Enter the value for a (or press 'q' to quit): ")
    
    if a.lower() == 'q':
        print("Exiting program.")
        break
    
    a = int(a)  
    b = int(input("Enter the value for b: "))  

    # Display true or false statement
    print(f"The statement {a} is greater than {b} is {is_greater(a, b)}")
