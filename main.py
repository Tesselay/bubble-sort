def find_greatest_index(numbers):
    greatest_val: int = max(numbers)
    return numbers.index(greatest_val)


def find_smallest_index(numbers):
    smallest_val: int = min(numbers)
    return numbers.index(smallest_val)


def iteration(numbers, iterator):
    try:
        if numbers[iterator] > numbers[iterator + 1]:
            first_val = numbers[iterator]
            second_val = numbers[iterator + 1]
            numbers[iterator] = second_val
            numbers[iterator + 1] = first_val
        else:
            iterator += 1
    except IndexError:
        iterator = 0


def bubble_sort(numbers):
    iterator: int = 0

    smallest_index = find_smallest_index(numbers)
    takeout = numbers.pop(smallest_index)
    numbers.append(takeout)

    while find_smallest_index(list) != 0:
        iteration(numbers, iterator)

    return numbers