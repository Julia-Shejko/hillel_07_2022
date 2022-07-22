# Завдання 1
# Реалізуйте клас «Car».
# Необхідно зберігати в полях класу: назву моделі, рік випуску, виробника, об'єм двигуна, колір машини, ціну.
# Реалізуйте методи класу для введення даних, виводу даних, реалізуйте доступ до окремих полів через методи класу.


# При виконанні не створювала доступу до всіх полів через методи класу, тільки до кількох з них.
# Просто створення - в завданні 2 і 3. Тут трішки взаємодії з користувачем :)
class Car:
    def __init__(self, model, year, manufacture, volume_of_engine, colour, price):
        self.model = model
        self.year = year
        self.manufacture = manufacture
        self.volume_of_engine = volume_of_engine
        self.colour = colour
        self.price = price

    def show_details(self):
        message = "This is a car."
        print(f"{message} Model: {self.model}\nYear of manufacture: {self.year}\nCar manufacturer: {self.manufacture}"
              f"\nVolume_of_engine: {self.volume_of_engine} liters\nColour: {self.colour}\nPrice: {self.price} $")

    def get_model(self):
        print(f"Model: {self.model}")

    def get_price(self):
        message = "You can choose this car!"
        print(f"{message} Model {self.model} has a price {self.price} $")

    def get_volume(self):
        print(f"Model: {self.model}\tVolume_of_engine: {self.volume_of_engine} liters")



skoda = Car(" Skoda Octavia", 2012, "Skoda Auto", 1.8, "grey", 9000)
hyundai = Car("Hyundai Elantra", 2011, "Hyundai Motors", 1.6, "black", 7000)
bmw = Car("BMW 3-Series", 2019, "Bayerische Motoren Werke AG", 2.0, "white", 35000)


if __name__ == "__main__":
    cars = [skoda, hyundai, bmw]
    allowed_options = "[list/names/price/volume/exit]"

    while True:
        desision = input(f"There are a lot of cars. What should I do?{allowed_options}: ")
        if desision == "list":
            for some_car in cars:
                some_car.show_details()
        elif desision == "names":
            for some_car in cars:
                some_car.get_model()
        elif desision == "price":
            for some_car in cars:
                some_car.get_price()
        elif desision == "volume":
            print("What volume of engine do you prefer? We have:")
            for some_car in cars:
                some_car.get_volume()
        elif desision == "exit":
            print("Exiting...")
            break
        else:
            print(f"Please use allowed options! {allowed_options}")

