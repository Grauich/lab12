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
    def __init__(self, restaurant_name, cuisine_type, location, hours, rating=0):
        super().__init__(restaurant_name, cuisine_type, rating)
        self.location = location
        self.hours = hours
        self.flavors = []

    def add_flavors(self, *flavors):
        self.flavors.extend(flavors)

    def remove_flavors(self, *flavors):
        for flavor in flavors:
            if flavor in self.flavors:
                self.flavors.remove(flavor)

    def check_flavor(self, flavor):
        return flavor in self.flavors

    def show_flavors(self):
        print(f"Сорта мороженого в '{self.restaurant_name}':")
        for flavor in self.flavors:
            print(f"- {flavor}")

    def describe_stand(self):
        print(f"Кафе-мороженое '{self.restaurant_name}' расположено по адресу '{self.location}'. Часы работы: {self.hours}. Рейтинг: {self.rating}.")
