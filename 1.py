class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}. Тип кухни: {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' открыт!")
newRestaurant = Restaurant("Паста-пицца", "Итальянская")
print(f"Атрибуты экземпляра: Название ресторана - {newRestaurant.restaurant_name}, Тип кухни - {newRestaurant.cuisine_type}")
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()
