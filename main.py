import timeit
import random


# Генеруємо список чисел від 1 до n
def generate_unique_numbers(n):
    numbers = list(range(1, n + 1))
    random.shuffle(numbers)
    return numbers


# Timsort сортування
def timsort(array):
    return sorted(array)

# Вимір часу виконання функції
execution_time = timeit.timeit(timsort(generate_unique_numbers(1000)), number = 1)

# Виведення результатів
print(f"Час виконання: {execution_time} секунд")