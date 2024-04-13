# Initialize an empty array to store the user inputs
user_inputs = []

# Ask for user input 10 times using a loop
for i in range(10):
    user_input = int(input(f"Enter input {i+1}: "))
    user_inputs.append(user_input)

# Find the largest number in the array
largest_number = max(user_inputs)

# Print the largest number
print("Largest number entered:", largest_number)