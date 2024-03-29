distanceMeters = float(input("Enter the distance the commuter will travel (in meters): "))

distanceKm = distanceMeters / 1000

if distanceKm <= 1:
    cost = 10
else:
    additionalDistance = distanceKm - 1
    additionalCost = additionalDistance // 2 * 2
    cost = 10 + additionalCost

print("Total distance traveled:", distanceKm, "km")
print("Cost of travel:", cost, "PHP")

payment = float(input("Enter the payment from the commuter: "))

if payment < cost:
    print("Payment is not sufficient.")
else:
    change = payment - cost
    print("Change of the commuter:", change, "PHP")