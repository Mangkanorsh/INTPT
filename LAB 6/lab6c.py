while True:
    voltage = float(input("Enter the input voltage (in volts): "))

    if voltage == 5:
        print("Voltage is ACTIVE!")
    elif voltage < 5:
        print("Voltage is CUTOFF.")
        break  # Terminate the loop if CUTOFF voltage is entered
    else:
        print("Voltage is BREAKDOWN.")
        break  # Terminate the loop if BREAKDOWN voltage is entered