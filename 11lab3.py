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

restaurant = Restaurant("Bobr", "Польская кухня", 4.5)

restaurant.describe_restaurant()

restaurant.update_rating(4.8)
restaurant.describe_restaurant()
