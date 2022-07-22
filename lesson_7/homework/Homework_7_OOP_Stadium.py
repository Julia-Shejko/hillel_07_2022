# Завдання 3
# Реалізуйте клас «Stadium».
# Необхідно зберігати в полях класу: назву стадіону, дату відкриття, країну, місто, розміщення.
# Реалізуйте методи класу для введення даних, виведення даних, реалізуйте доступ до окремих полів через методи класу.

class Stadium:
    def __init__(self, name, opening_date, country, city, adress):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.adress = adress

    def show_details(self):
        message = "This is a stadium."
        print(
            f'{message} Name: {self.name}\nOpening_date: {self.opening_date}\nCountry: {self.country}\n'
            f'City: {self.city}\nAdress: {self.adress}')

    def get_name(self):
        print(f"The stadium has a name '{self.name}'")

    def get_opening_date(self):
        print(f"The stadium was open {self.opening_date}")

    def get_country(self):
        print(f"The stadium is located in {self.country}")

    def get_city(self):
        print(f"{self.city} is the city where the stadium is located")

    def get_adress(self):
        print(f"Address of the stadium: {self.adress}")


vorskla = Stadium(
    name = "Vorskla",
    opening_date = "May 2, 1951",
    country = "Ukraine",
    city = "Poltava",
    adress = "Independence Square, 16")

vorskla.show_details()
vorskla.get_name()
vorskla.get_opening_date()
vorskla.get_country()
vorskla.get_city()
vorskla.get_adress()