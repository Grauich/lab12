class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' предлагает кухню типа '{self.cuisine_type}'.")

    def open_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' сейчас открыт.")

restaurant1 = Restaurant("Bobr", "Польская кухня")
restaurant2 = Restaurant("Sushi World", "Японская кухня")
restaurant3 = Restaurant("El Mexicano", "Мексиканская кухня")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
