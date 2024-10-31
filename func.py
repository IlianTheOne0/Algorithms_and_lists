import random

def main():
    numbers = [random.randint(-100, 100) for temp in range(15)]

    a, b, c, d, e = is_negative_and_positive(numbers)

    print(f'Initial values: {numbers}\nMinimum and maximum values: {min_and_max(numbers)}\
            \nNumber of negative numbers: {a, b}\nNumber of positive numbers: {c, d} \
            \nNumber of zeros: {e}')

def min_and_max(numbers) -> tuple:
    min = numbers[0]
    max = numbers[0]

    for digit in range(1, len(numbers)):
        if numbers[digit] < min:
            min = numbers[digit]
        if numbers[digit] > max:
            max = numbers[digit]

    return min, max

def is_negative_and_positive(numbers) -> tuple:
    number_of_negative = 0
    negative_numbers = list()
    number_of_positive = 0
    positive_numbers = list()
    number_of_zero = 0

    for digit in range(len(numbers)):
        if numbers[digit] < 0:
            number_of_negative += 1
            negative_numbers.append(numbers[digit])
        elif numbers[digit] != 0:
            number_of_positive += 1
            positive_numbers.append(numbers[digit])
        else:
            number_of_zero += 1

    return number_of_negative, negative_numbers, number_of_positive, positive_numbers, number_of_zero