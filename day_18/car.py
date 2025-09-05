class Car:
    def __init__(self, model, year, mileage):
        self.model = model
        self.year = year
        self.mileage = mileage

    def display_info(self):
        print("\n Car Information")
        print("="*30)
        print(f"Model   : {self.model}")
        print(f"Year    : {self.year}")
        print(f"Mileage : {self.mileage} km/l")
        print("="*30)


car1 = Car("Tesla Model S", 2022, 15)
car2 = Car("Hyundai i20", 2020, 20)

car1.display_info()
car2.display_info()
