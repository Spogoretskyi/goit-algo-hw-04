import timeit
import random


# Генеруємо список чисел від 1 до n
def generate_unique_numbers(n):
    numbers = list(range(1, n + 1))
    random.shuffle(numbers)
    return numbers


# Timsort сортування
def tim_sort_sorted(array):
    return sorted(array)


def tim_sort_sort(array):
    return array.sort()


numbers = generate_unique_numbers(1000)

execution_time = timeit.timeit(lambda: tim_sort_sorted(numbers), number = 1)
print(f"Час виконання 'tim_sort_sorted': {execution_time} секунд")

execution_time = timeit.timeit(lambda: tim_sort_sort(numbers), number = 1)
print(f"Час виконання 'tim_sort_sort': {execution_time} секунд")