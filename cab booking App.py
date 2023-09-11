import datetime
def main():
 time = datetime.datetime.now()
 print(""" 
 _______
 // ||\ \\
 _____//___||_\ \___
 ) _ _ \\
 |_/ \________/ \___|
 ___\_/________\_/______
 """)
 print("\n\tWELCOME TO SAFA CAB SERVICE!\n")
 print(f"\tCurrent date and time: {time}")
 while True:
 print("""
 ******** VEHICLE RENTEL SHOP ********
 1. Admin
 2. Unregistered Customer
 3. Registered Customer
 4. Exit the program
 """)
 try:
 choice = int(input("Enter your choice: "))
 except ValueError:
 print("Please enter a number!")
 continue
 if choice == 1:
 admin()
 elif choice == 2:
 unregistered_function()
 elif choice == 3:
 registered_function()
 elif choice == 4:
 break
 else:
 print("Please enter a choice between 1-4 only!")
def admin():
 nValue = input("Enter username: ")
 pValue = input("Enter password: ")
 admin_function()
def admin_function():
 while True:
 print("""
 ******** Access System ********
 1. Add Vehicle
 2. Remove Vehicle
3. Display All records of
 a. Vehicles available for Rent
b. Customer Payment for a specific time duration
 4. Assign a hire
5. Form assigned hire
6. Exit to main menu
""")
 try:
 choice = int(input("Enter a number: "))
 except ValueError:
 print("Please enter a number!")
 continue
 if choice == 1:
 add_vehicles()
 elif choice == 2:
 remove_vehicles()
 elif choice == 3:
 option = input("option a or b? ")
 if option == 'a':
 display_vehicles()
 else:
 print("""
 ******** Customer Payment for a specific 
time duration ********
Car:
 Vehicle : Suzuki Alto - Premium -
Manual
 Rate Per Month : 69,500.00
Rate Per Week : 22,500.00
Excess Mileage : 45
 Van:
 Vehicle : Toyota Regius - Petrol Auto 
Dual A/C
 Rate Per Month : 150,000.00
Rate Per Week : 48,500.00
 Excess Mileage : 65
 3 Wheelers:
 Vehicle : Bajaj RE
Rate Per Month : 35,000.00
Rate Per Week : 9,500.00
 Excess Mileage : 35
 Trucks:
 Vehicle : Toyota Prado
Rate Per Month : 450,000.00
Rate Per Week : 135,000.00
Excess Mileage : 175
 Lorry:
 Vehicle : Mitsubishi Montero
Rate Per Month : 395,000.00
 Rate Per Week : 120,000.00
 Excess Mileage : 145
 """)
 elif choice == 4:
 hire_vehicles()
 elif choice == 5:
 hire_vehicles()
 elif choice == 6:
 break
 else:
 print("Please enter a number between 1-6 only!")
def display_vehicles():
 print("""
 ******** Available Vehicles & Details ********
Car:
 maximum number of passengers - 3 and 4
 AC/ Non AC
 Van:
 Maximum number of passengers - 6 and 8
 AC/ Non AC
 3 Wheelers:
 Maximum number of passengers - 3
 
 Trucks:
 Size – 7 ft and 12 ft
 
 Lorry:
 Max load and size - 2500kg and 3500kg
 """)
def add_vehicles():
 with open("Displayvehicles_Data.txt", "a") as text:
 vehicles_type = input("Vehicle Type: ")
 brand = input("Brand: ")
 color = input("Color: ")
 year = input("Year: ")
 text.write("\n%s:%s:%s:%s" % (vehicles_type, brand, color, year))
 print("New Vehicle Added Successfully.....!")
def remove_vehicles():
 with open("Displayvehicles_Data.txt", "a") as text:
 vehicles_type = input("Type: ")
 brand = input("Brand: ")
 color = input("Color: ")
 year = input("Year: ")
 text.write("\n%s:%s:%s:%s" % (vehicles_type, brand, color, year))
 print("Vehicle Removed Successfully.....!")
def hire_vehicles():
 with open("Displayvehicles_Data.txt", "a") as text:
 vehicles_type = input("Vehicle Type: ")
 vehicle_No = input("Vehicle Number: ")
 customer_Name = input("Customer Name: ")
 address = input("Address: ")
 pickup_location_date_time = input("Pickup Location, Date, Time: ")
 text.write("\n%s:%s:%s:%s:%s" % (vehicles_type, vehicle_No, 
customer_Name, address, pickup_location_date_time))
 print()
 print("Vehicle Type:", (vehicles_type))
 print("Vehicle Number:",(vehicle_No))
 print("Customer name:",(customer_Name))
 print("Customer Address:",(address))
 print("Pickup Location/ Date/ Time:",(pickup_location_date_time))
def existing_users():
 nValue = input("Username: ")
 pValue = input("Password: ")
 return (nValue, pValue)
def unregistered_function():
 while True:
 print("""
 ******** For All Customers ********
 1. View all Vehicles available for rent
 2. Register 
 3. Exit to main menu
 """)
 try:
 choice = int(input("Enter a number: "))
 except ValueError:
 print("Please enter a number!")
 continue
 if choice == 1:
 display_vehicles ()
 elif choice == 2:
 get_new_users()
 break
 elif choice == 3:
 break
 else:
 print("Please enter a choice between 1-2 only!")
def get_new_users():
 with open("User_Data.txt", "a") as text:
 while True:
 name = input("Enter your name to register: ")
 password = input("Enter password: ")
 record = name + ":" + password
 text.write(record + "\n")
 print("Registered Successful...")
 break
def registered_Customer():
 nValue = input("Enter username: ")
 pValue = input("Enter password: ")
 registered_function()
def registered_function():
 while True:
 print("""
 ******** For Registered Customer ********
 1. Available Vehicles
 2. Booking Vehicles 
 3. Payment and Confirmation of Booking
 4. Exit to main menu
 """)
 try:
 choice = int(input("Enter your choice: "))
 except ValueError:
 print("Please enter a number!")
 continue
 if choice == 1:
 display_vehicles()
 elif choice == 2:
 book_cars()
 elif choice == 3:
 print("Your Payment is : 120,000.00")
 elif choice == 4:
 break
 else:
 print("Please enter a choice between 1-5 only!")
 return
def book_cars():
 with open("Displayvehicles_Data.txt", "a") as text:
 print("******** BOOK CAB NOW ********")
 type = input("Enter Vehicle type you want: ")
 name = input("Enter Your Name: ")
 mobile = input("Enter Mobile Number: ")
 pickup_location = input("Pickup Location: ")
 drop_location = input("Drop Location: ")
 pickup_date = input("Pickup Date: ")
 pickup_time = input("Pickup Time: ")
 text.write("\n%s:%s:%s:%s:%s:%s:%s" % (type, name, mobile, 
pickup_location, drop_location, pickup_date, pickup_time))
 print("******** Thankyou for booking cab... ********")
if __name__ == "__main__":
 main()
