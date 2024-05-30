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
        self.types_of_ice_cream = {
            "на палочке": [],
            "мягкое мороженое": [],
            "в рожке": [],
            "в стаканчике": []
        }

    def describe_stand(self):
        print(f"Кафе-мороженое '{self.restaurant_name}' расположено по адресу '{self.location}'. Часы работы: {self.hours}. Рейтинг: {self.rating}.")

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

    def add_ice_cream(self, ice_cream_type, *ice_creams):
        if ice_cream_type in self.types_of_ice_cream:
            self.types_of_ice_cream[ice_cream_type].extend(ice_creams)
        else:
            print(f"Тип мороженого '{ice_cream_type}' не существует.")

    def show_ice_cream_types(self):
        for ice_cream_type, ice_creams in self.types_of_ice_cream.items():
            print(f"{ice_cream_type.capitalize()}:")
            for ice_cream in ice_creams:
                print(f"- {ice_cream}")

ice_cream_stand = IceCreamStand("Frozen Delights", "Кафе-мороженое", "ул. Пушкина, д. 10", "с 10:00 до 22:00", 4.2)

ice_cream_stand.add_flavors("Шоколадное", "Ванильное", "Клубничное", "Фисташковое")

ice_cream_stand.show_flavors()

ice_cream_stand.remove_flavors("Клубничное")

print(f"Есть ли Клубничное мороженое? {'Да' if ice_cream_stand.check_flavor('Клубничное') else 'Нет'}")

ice_cream_stand.add_ice_cream("на палочке", "Шоколадное на палочке", "Клубничное на палочке")
ice_cream_stand.add_ice_cream("мягкое мороженое", "Ванильное мягкое мороженое")
ice_cream_stand.add_ice_cream("в рожке", "Фисташковое в рожке")

ice_cream_stand.show_ice_cream_types()
ice_cream_stand.describe_stand()