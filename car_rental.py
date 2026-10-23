# ----------------------------
# Simple Car Rental Project 🚗
# ----------------------------
# This python code lets a user rent cars, return them, and check which ones are available.

# Car data — this is our mini "database"
cars = { #this is a dictionary with car names as keys and another dictionary as values containing price and availability
    "Toyota Camry": {"price_per_day": 45, "available": True},
    "Honda Civic": {"price_per_day": 40, "available": True},
    "Tesla Model 3": {"price_per_day": 100, "available": True},
    "BMW 3 Series": {"price_per_day": 85, "available": True},
}

# Function to show available cars
def show_available_cars():
    print("\n--- Available Cars ---")
    for car, info in cars.items(): 
        if info["available"]: #checks if the car is available
            print(f"{car} - ${info['price_per_day']} per day")
    print("-----------------------")

# Function to rent a car
def rent_car():
    show_available_cars()
    car_name = input("\nEnter the name of the car you want to rent: ")

    # Check if the car exists and is available
    if car_name in cars:
        if cars[car_name]["available"]: #check if the car is available
            days = int(input("How many days do you want to rent it for? "))
            total = days * cars[car_name]["price_per_day"]
            print(f"\n✅ You rented the {car_name} for {days} days. Total cost: ${total}")
            cars[car_name]["available"] = False  # car is now taken
        else:
            print("\n❌ Sorry, that car is already rented.")
    else:
        print("\n⚠️ That car doesn't exist in our system.")

# Function to return a car
def return_car():
    car_name = input("\nEnter the name of the car you're returning: ")

    if car_name in cars:
        if not cars[car_name]["available"]:
            cars[car_name]["available"] = True
            print(f"\n🚗 Thanks for returning the {car_name}!")
        else:
            print("\n🤔 That car wasn’t rented out.")
    else:
        print("\n⚠️ That car isn’t in our system.")

# Main menu loop
def main():
    while True:
        print("\n========== CAR RENTAL SYSTEM ==========")
        print("1. Show available cars")
        print("2. Rent a car")
        print("3. Return a car")
        print("4. Exit")
        print("=======================================")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_available_cars()
        elif choice == "2":
            rent_car()
        elif choice == "3":
            return_car()
        elif choice == "4":
            print("\n👋 Thanks for using our car rental system!")
            break
        else:
            print("\n⚠️ Invalid option, try again.")

# Run the main menu
main()
