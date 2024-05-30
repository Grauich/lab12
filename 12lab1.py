class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' предлагает кухню типа '{self.cuisine_type}' и имеет рейтинг {self.rating}.")

    def open_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' сейчас открыт.")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана '{self.restaurant_name}' обновлен до {self.rating}.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        super().__init__(restaurant_name, cuisine_type, rating)
        self.flavors = []

    def add_flavors(self, *flavors):
        self.flavors.extend(flavors)

    def show_flavors(self):
        print(f"Сорта мороженого в '{self.restaurant_name}':")
        for flavor in self.flavors:
            print(f"- {flavor}")

ice_cream_stand = IceCreamStand("Frozen Delights", "Кафе-мороженое", 4.2)

ice_cream_stand.add_flavors("Шоколадное", "Ванильное", "Клубничное", "Фисташковое")

ice_cream_stand.show_flavors()
