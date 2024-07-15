number1 = int(input("Enter the number: "))  # Corrected variable name
add = 0 
 # Initialize add to 0 outside the loop
rem=0

while number1 != 0:
    rem = number1 % 10   
    add = add + rem   
    number1 = number1 // 10  # Update number1 by removing the last digit

# Print the sum after the loop completes
print("The sum of digits is:", add)
