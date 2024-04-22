user_inputs = []

for i in range(10):
    user_input = int(input(f"Enter input {i+1}: "))
    user_inputs.append(user_input)

largest_number = max(user_inputs)

print("Largest number entered:", largest_number)