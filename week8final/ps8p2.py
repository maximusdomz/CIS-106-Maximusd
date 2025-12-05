class Car:
    def __init__(self, car_make, car_model, sticker_price):
        self.car_make = car_make
        self.car_model = car_model
        self.sticker_price = sticker_price

    def get_car_make(self):
        return self.car_make

    def get_car_model(self):
        return self.car_model

    def get_sticker_price(self):
        return self.sticker_price

    def get_discount_price(self):
        return self.sticker_price * 0.90

class Sport(Car):
    def __init__(self, car_make, car_model, sticker_price):
        super().__init__(car_make, car_model, sticker_price)
        self.sport_wheels = False
        self.sport_engine = False
        self.sport_interior = False
        self.updated_price = self.get_discount_price()

    def sportwheels(self, include_option):
        if include_option.upper() == "Yes":
            self.sport_wheels = True
            self.updated_price += 1000.00

    def sportengine(self, include_option):
        if include_option.upper() == "Yes":
            self.sport_engine = True
            self.updated_price += 3000.00

    def sportinterior(self, include_option):
        if include_option.upper() == "Yes":
            self.sport_interior = True
            self.updated_price += 2000.00

    def price_with_options(self):
        print(f"Price with options: ${self.updated_price:.2f}")

if __name__ == "__main__":
    my_sport_car = Sport("Acura", "MDX", 50000.00)

    print(f"Make: {my_sport_car.get_car_make()}")
    print(f"Model: {my_sport_car.get_car_model()}")
    print(f"Sticker Price: {my_sport_car.get_sticker_price()}")
    print(f"Discount Price: {my_sport_car.get_discount_price()}")

    my_sport_car.sportwheels("Y")
    my_sport_car.sportengine("N")
    my_sport_car.sportinterior("Y")

    my_sport_car.price_with_options()

    print("\n--- Another Sport Car Example ---")
    another_sport_car = Sport("Porsche", "911", 120000.00)
    another_sport_car.sportwheels("Y")
    another_sport_car.sportengine("Y")
    another_sport_car.sportinterior("N")
    another_sport_car.price_with_options()