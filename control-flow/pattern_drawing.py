    size = int(input("Enter the size of the pattern: "))
    
    if size <= 0:
        print("Error: Please enter a positive integer.")
    else:
        # Initialize a row counter
        row = 0
        
        # Use a while loop to iterate through each row
        while row < size:
            # Use a for loop to print asterisks in the current row
            for _ in range(size):
                print("*", end="")
            # Print a newline character to move to the next row
            print()
            # Increment the row counter
            row += 1
