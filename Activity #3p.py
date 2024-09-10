from tabulate import tabulate

class PUV:
    def __init__(self, vehicle: str, regular_rate: float, student_rate: float, senior_rate: float):
        self.vehicle = vehicle
        self.regular_rate = regular_rate
        self.student_rate = student_rate
        self.senior_rate = senior_rate

    def show_price(self):
        headers = ["Category", "Fare (₱)"]
        data = [
            ["Regular", self.regular_rate],
            ["Student", self.student_rate],
            ["Senior Citizen", self.senior_rate]
        ]
        print(f"\nFare rate for {self.vehicle.capitalize()}:")
        print(tabulate(data, headers, tablefmt="rounded_grid", colalign=("center", "center")))

def main():
    jeepney = PUV("jeepney", 12, 10, 9.50)
    tricycle = PUV("tricycle", 50, 40, 38)
    bus = PUV("bus", 12, 10, 9.50)

    while True:
        print("----------------------- List of vehicles -----------------------\n"
              "                         ↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n"
              "                          -> Jeepney\n"
              "                          -> Tricycle\n"
              "                          -> Bus")
        choose_vehicle = input("What vehicle do you want to ride? (or type [x] to quit): ").lower()

        if choose_vehicle in ["jeepney", "tricycle", "bus"]:
            if choose_vehicle == "jeepney":
                jeepney.show_price()
            elif choose_vehicle == "tricycle":
                tricycle.show_price()
            elif choose_vehicle == "bus":
                bus.show_price()
        elif choose_vehicle == 'x':
            print("Exiting the Vehicle fare checker. Have a nice day!")
            break
        else:
            print("Invalid Input. Please select a valid vehicle from the list.")

if __name__ == "__main__":
    main()
