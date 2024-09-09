from tabulate import tabulate

fare_rate = {
    "jeepney": [12, 10, 9.50],
    "tricycle": [50, 40, 38],
    "bus": [10, 12, 9.50]
}
class PUV:

    def __init__(self, vehicle):
        self.vehicle = vehicle
        if vehicle in fare_rate:
            headers = ["Category", "Fare (₱)"]
            data = [
                ["Regular", fare_rate[vehicle][0]],
                ["Student", fare_rate[vehicle][1]],
                ["Senior Citizen", fare_rate[vehicle][2]]
            ]
            print(f"\nFare rate for {vehicle.capitalize()}:")
            print(tabulate(data, headers, tablefmt="rounded_grid",colalign=("center", "center")))
        else:
            print("!!!!!!! Invalid Input !!!!!!!!!!!")

while True:
    print("----------------------- List of vehicles -----------------------\n"
          "                         ↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n"
          "                          -> Jeepney\n"
          "                          -> Tricycle\n"
          "                          -> Bus")
    choose_vehicle = input("What vehicle do you want to ride? (or type [x] to quit): ").lower()
    if choose_vehicle == 'x':
        print("Exiting the Vehicle fare checker. Have a nice day!")
        break
    PUV(choose_vehicle)
