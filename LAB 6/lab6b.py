participants_quantity = int(input("Number of Participants: "))

minor = []
legal = []
senior = []

for i in range(participants_quantity):
    user_input = int(input(f"Age of participant {i+1}: "))
    if user_input < 18:
        minor.append(user_input)
    elif user_input >= 60:
        senior.append(user_input)
    else:
        legal.append(user_input)

# Print the number of participants in each category
print("Number of minors:", len(minor))
print("Number of legal participants:", len(legal))
print("Number of seniors:", len(senior))
