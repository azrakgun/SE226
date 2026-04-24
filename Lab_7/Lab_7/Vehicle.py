class Vehicle:
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model = model
        self.year = int(year)

    def __str__(self):
        return f"VID: {self.vid} | {self.model} ({self.year})"

    def __eq__(self, other):
        if isinstance(other, Vehicle):
            return self.vid == other.vid
        return False

    def is_new(self, n):
        return (2026 - self.year) <= n


class Car(Vehicle):
    def __init__(self, vid, model, year, fuel_type, doors):
        super().__init__(vid, model, year)  # Üst sınıfın (Vehicle) özelliklerini miras alıyoruz.
        self.fuel_type = fuel_type
        self.doors = int(doors)

    def __str__(self):
        return f"[Car] {super().__str__()} | Fuel: {self.fuel_type} | {self.doors} Doors"


class Truck(Vehicle):
    def __init__(self, vid, model, year, max_load, axles):
        super().__init__(vid, model, year)
        self.max_load = int(max_load)
        self.axles = int(axles)

    def __str__(self):
        return f"[Truck] {super().__str__()} | Load: {self.max_load}kg | {self.axles} Axles"

class Motorcycle(Vehicle):
    def __init__(self, vid, model, year, engine_cc, bike_type):
        super().__init__(vid, model, year)
        self.engine_cc = int(engine_cc)
        self.type = bike_type

    def __str__(self):
        return f"[Motorcycle] {super().__str__()} | Eng: {self.engine_cc}cc | Type: {self.type}"


def save_fleet_to_file(vehicles, filename):
    with open(filename, 'w') as file:
        for v in vehicles:
            if isinstance(v, Car):
                file.write(f"Car,{v.vid},{v.model},{v.year},{v.fuel_type},{v.doors}\n")
            elif isinstance(v, Truck):
                file.write(f"Truck,{v.vid},{v.model},{v.year},{v.max_load},{v.axles}\n")
            elif isinstance(v, Motorcycle):
                file.write(f"Motorcycle,{v.vid},{v.model},{v.year},{v.engine_cc},{v.type}\n")


def load_fleet_from_file(filename):
    vehicles = []
    try:
        print(f"Loading fleet data from '{filename}'...")
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if not data or len(data) < 4:
                    continue

                v_type = data[0]
                vid = data[1]
                model = data[2]
                year = int(data[3])

                if v_type == "Car":
                    vehicles.append(Car(vid, model, year, data[4], data[5]))
                elif v_type == "Truck":
                    vehicles.append(Truck(vid, model, year, data[4], data[5]))
                elif v_type == "Motorcycle":
                    vehicles.append(Motorcycle(vid, model, year, data[4], data[5]))

        print(f" {len(vehicles)} vehicles loaded successfully.")
    except FileNotFoundError:
        print("File not found.")

    return vehicles


if __name__ == "__main__":
    fleet = [
        Car("V01", "Tesla", 2023, "Electric", 4),
        Truck("T01", "Volvo", 2020, 25000, 6),
        Motorcycle("M01", "Yamaha", 2024, 998, "Sport"),
        Car("V02", "BMW", 2026, "Petrol", 4),
        Truck("T02", "Mercedes", 2021, 18000, 4),
        Motorcycle("M02", "Suziki", 2015, 1200, "Cruiser")
    ]

    save_fleet_to_file(fleet, "fleet.txt")

    loaded_fleet = load_fleet_from_file("fleet.txt")

    print("\n All Vehicles ")
    for v in loaded_fleet:
        print(v)

    print("\n Recent Vehicles (Last 4 Years) ")
    for v in loaded_fleet:
        if v.is_new(4):
            print(v)

    print("\nElectric Cars Only ")
    for v in loaded_fleet:
        if isinstance(v, Car) and v.fuel_type == "Electric":
            print(v)