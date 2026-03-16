# Vehicle Mileage Calculator

print("=== Vehicle Mileage Calculator ===")

# Input from user
distance = float(input("Enter distance travelled (in km): "))
fuel = float(input("Enter fuel used (in litres): "))

# Calculate mileage
mileage = distance / fuel

# Output
print("Vehicle Mileage =", round(mileage, 2), "km per litre")