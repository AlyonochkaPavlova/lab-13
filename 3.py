class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, initial_rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = initial_rating

    def describe_restaurant(self):
        print(f'Название ресторана: {self.restaurant_name}')
        print(f'Тип кухни: {self.cuisine_type}')
        print(f'Рейтинг: {self.rating}')

    def update_rating(self, new_rating):

        if isinstance(new_rating, (int, float)):
            self.rating = new_rating
        else:
            print("Ошибка: введенное значение должно быть числом.")
first_restaurant = Restaurant('Самовар', 'Русская кухня', 4.7)
second_restaurant = Restaurant('Паста-пицца', 'Итальянская кухня', 4.3)
third_restaurant = Restaurant('Васаби', 'Японская', 4.8)
first_restaurant.describe_restaurant()
second_restaurant.describe_restaurant()
third_restaurant.describe_restaurant()
first_restaurant.update_rating(4.9)