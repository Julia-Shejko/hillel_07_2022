class Product:
    def __init__(self, name, color, price, amount, discount):
        self.name = name
        self.color = color
        self.price = price
        self.amount = amount
        self.discount = discount

    def get_product_description(self):
        return f"{self.name}/{self.color}: {self.price} | {self.amount}"

    def show_description(self):
        print(f"Description: {self.get_product_description()}")

    def get_price(self):
        final_price = round(self.price * self.discount, 2)
        print(f"The final price of {self.name} is {final_price}")
        return final_price


class Phone(Product):
    def __init__(self, name, color, price, amount, discount, lte=False):
        # Product.__init__(self, name, color, price, amount)
        super().__init__(name, color, price, amount, discount)
        self.lte = lte

    def get_product_description(self):
        additional = ", LTE" if self.lte else ""
        message = super().get_product_description()
        message += additional
        return message


class Laptop(Product):

    def __init__(self, name, color, price, amount, discount, motherboard_type, material):
        super().__init__(name, color, price, amount, discount)
        self.motherboard_type = motherboard_type
        self.material = material

    def get_product_description(self):
        additional = f"; specifications: {self.motherboard_type}, {self.material}"
        message = super().get_product_description()
        message += additional
        return message


iphone7 = Phone(name="iPhone 7", color="red", price=700.0, amount=1, discount=0.7)
iphone13 = Phone(name="iPhone 13", color="black", price=2000.0, amount=2, discount=0.92, lte=True)
lenovo = Laptop(name="Lenovo", color="grey", price=3000.0, amount=1, discount=0.87, motherboard_type="ThinkCentre M73",
                material="plastic")


iphone13.show_description()
iphone7.show_description()
lenovo.show_description()
iphone13.get_price()
lenovo.get_price()
