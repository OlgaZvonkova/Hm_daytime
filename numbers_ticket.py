# lottery_numbers = get_numbers_ticket(1, 49, 6)
# print("Ваші лотерейні числа:", lottery_numbers)

import random

def get_numbers_ticket() -> list:
    lottery_numbers = random.sample(range(1, 50), 6)  # Виправлено діапазон та кількість чисел
    return lottery_numbers

res = get_numbers_ticket()  # Виклик функції для отримання чисел
print("Ваші лотерейні числа:", res)