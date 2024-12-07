from operator import add, mul
from itertools import product

with open("./input.txt", "r") as file:
    values, all_numbers = [], []
    for line in file.readlines():
        value, numbers = line.strip().split(": ")
        values.append(int(value.strip()))
        all_numbers.append([int(number) for number in numbers.strip().split(" ")])


def concat(left: int, right: int):
    return int(str(left) + str(right))


def solve_equations(values, all_numbers):
    valid_equations_sum = 0
    for value, numbers in zip(values, all_numbers):
        operators = [(add, mul, concat) for _ in range(len(numbers) - 1)]
        for test_operators in product(*operators):
            test_value = numbers[0]
            for i, operator in enumerate(test_operators):
                test_value = operator(test_value, numbers[i + 1])
                if test_value > value:
                    break
            if test_value == value:
                valid_equations_sum += value
                break
    return valid_equations_sum


print(solve_equations(values, all_numbers))
