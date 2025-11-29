def calc_trip_details(miles, gallons):
  """Calculates miles per gallon and cost of gas."""
  miles_per_gallon = miles / gallons
  cost_of_gas = gallons * 3.00
  return miles_per_gallon, cost_of_gas

Number_of_trips = 0
total_miles_traveled = 0
total_cost_of_gas = 0

while True:
  start_trip = input("Do you want to enter a new trip? (Yes or No): ")
  if start_trip.lower() != "yes":
    break

  destination_city = input("Enter the destination city: ")
  miles_str = input("Enter the miles travelled: ")
  gallons_str = input("Enter the gallons used: ")

  try:
    miles_traveled = float(miles_str)
    gallons_used = float(gallons_str)
  except ValueError:
    print("Invalid input. Please enter a number for miles and gallons.")
    continue

  miles_per_gallon, cost_of_gas = calc_trip_details(miles_traveled, gallons_used)

  print(f"\n--- Trip Details ---")
  print(f"Destination: {destination_city}")
  print(f"Miles Travelled: {miles_traveled:.2f}")
  print(f"Gallons Used: {gallons_used:.2f}")
  print(f"Miles Per Gallon: {miles_per_gallon:.2f}")
  print(f"Gas Cost: ${cost_of_gas:.2f}")

  Number_of_trips += 1
  total_miles_traveled += miles_traveled
  total_cost_of_gas += cost_of_gas

print("\n--- Trip Summary ---")
print(f"Total number of trips: {Number_of_trips}")
print(f"Total miles travelled: {total_miles_traveled:.2f}")
print(f"Total gas cost: ${total_cost_of_gas:.2f}")
