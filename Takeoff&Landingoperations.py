def main():
    while True:
        print("Welcome to the system to calculate takeoffs and landing in an airplane Cessna 172N for internal flights in Guatemala")
        eleccion = input("What calculation would you like to perform? \n1. Landing \n2. Takeoff \n3. Both Calculations \nChoose an option (1, 2, 3): ")

        if eleccion not in ["1", "2", "3"]:
            print("Please, choose a valid option.")
            continue

        if eleccion in ["1", "3"]:
            print("\nTakeoff Calculation:")
            show_airport_list()
            departure_airport = input("Please, enter the departure airport/aerodrom indicator: ").upper()
            try:
                temperture = float(input("Please, enter the temperature of the departure airport (in Celsius degrees): "))
                headwind = float(input("Do you have headwind? (knots): "))
                tailwind = float(input("How many knots of tailwind do you have? "))
            except ValueError:
