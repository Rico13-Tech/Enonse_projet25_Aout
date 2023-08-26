print ("Rico rent ")
class Vehicle:
    def __init__(self, make, model, year, daily_rate):
        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
    
    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Daily Rate: {self.daily_rate}")

class Car(Vehicle):
    def __init__(self, make, model, year, daily_rate, num_seats):
        super().__init__(make, model, year, daily_rate)
        self.num_seats = num_seats
    
    def display_info(self):
        super().display_info()
        print(f"Number of Seats: {self.num_seats}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, daily_rate, engine_type):
        super().__init__(make, model, year, daily_rate)
        self.engine_type = engine_type
    
    def display_info(self):
        super().display_info()
        print(f"Engine Type: {self.engine_type}")

class Bicycle(Vehicle):
    def __init__(self, make, model, year, daily_rate, frame_type):
        super().__init__(make, model, year, daily_rate)
        self.frame_type = frame_type
    
    def display_info(self):
        super().display_info()
        print(f"Frame Type: {self.frame_type}")

class Rental:
    def __init__(self, vehicle, rental_days):
        self.vehicle = vehicle
        self.rental_days = rental_days
    
    def calculate_total_cost(self):
        return self.vehicle.daily_rate * self.rental_days
    
    def display_receipt(self):
            print("Merci d'avoir choisi Rico Rent")
            print("Rental Receipt")
            self.vehicle.display_info()
            print(f"Rental Days: {self.rental_days}")
            print(f"Total Cost: {self.calculate_total_cost()}")


car = Car("Toyota", "Camry", 2023, 50.0, 5)
rental = Rental(car, 3)
rental.display_receipt()

motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2023, 80, "V-twin")
rental = Rental(motorcycle, 2)
rental.display_receipt()

bicycle = Bicycle("Trek", "FX", 2023, 15, "Hybrid")
rental = Rental(bicycle, 1)
rental.display_receipt()

#car = Car("Toyota", "Camry", 2023, 50.0, 5)
#motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2023, 80, "V-twin")
#bicycle = Bicycle("Trek", "FX", 2023, 15, "Hybrid")

#car.display_info()
#motorcycle.display_info()
#bicycle.display_info()

#rental_car = Rental(car, 3)
#rental_car.display_receipt()

#rental_motorcycle = Rental(motorcycle, 2)
#rental_motorcycle.display_receipt()

#rental_bicycle = Rental(bicycle, 1)
#rental_bicycle.display_receipt()