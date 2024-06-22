import random


def generate_order_info():
    name_list = ['Саша', 'Паша', 'Маша', 'Гоша']
    surname_list = ['Сашкин', 'Пашкин', 'Машкина', 'Гошкин']
    address_list = ['Москва, Красная площадь, чудесный дом',
                    'СПБ, Невский пр-т, дом еще чудеснее',
                    'Курск, Бабушкина ул., бабушкин дом']
    duration_list = ["сутки", "двое суток", "трое суток", "четверо суток",
                     "пятеро суток", "шестеро суток", "семеро суток"]

    random_order_info = {
        "name": random.choice(name_list),
        "surname": random.choice(surname_list),
        "address": random.choice(address_list),
        "metro": f"{random.randint(1, 237)}",
        "phone": f"+7{random.randint(1000000000, 9999999999)}",
        "date": f"{random.randint(1, 25)}.{random.randint(1, 12)}.{random.randint(2024, 2050)}",
        "duration": random.choice(duration_list)
    }

    return random_order_info

