item1 = input("Item one price: ")
item2 = input("Item two price: ")
item3 = input("Item three price: ")
senior = input("Senior citizen or not: ")
payment = input("Payment of the customer: ")

totalItem = (float(item1) + float(item2) + float(item3))
tax = totalItem * 0.1
itemWithTax = totalItem + tax
seniorDiscount = itemWithTax * 0.2



if senior == "yes" or senior == "Yes" or senior == "True" or senior == "true":
    seniorDiscountApplied = itemWithTax - seniorDiscount
    if float(payment) >= seniorDiscountApplied:
        change = float(payment) - seniorDiscountApplied
        print("\nTotal Amount: ", seniorDiscountApplied)
        print("\nYour payment: ", payment)
        print("\nYour change is: ", change)
    else:
        print("\ninsufficient payment")
else:
    if float(payment) >= itemWithTax:
        change = float(payment) - itemWithTax
        print("\nTotal Amount: ", itemWithTax)
        print("\nYour payment: ", payment)
        print("\nYour change is: ", change)
    else:
        print("\ninsufficient payment")



