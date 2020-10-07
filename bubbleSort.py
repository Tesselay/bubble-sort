NUMBER_COMPARED = 0
NUMBER_SWITCHED = 0


def find_smallest_index(numbers):
    smallest_val: int = min(numbers)
    return numbers.index(smallest_val)


def iteration(numbers, iterator):
    try:
        global NUMBER_COMPARED
        global NUMBER_SWITCHED
        if numbers[iterator] > numbers[iterator + 1]:
            NUMBER_COMPARED += 1
            NUMBER_SWITCHED += 1

            first_val = numbers[iterator]
            second_val = numbers[iterator + 1]
            numbers[iterator] = second_val
            numbers[iterator + 1] = first_val
            iterator += 1
        else:
            NUMBER_COMPARED += 1
            iterator += 1
    except IndexError:
        iterator = 0

    return numbers, iterator


def move_to_end(numbers, number):
    takeout = numbers.pop(number)
    numbers.append(takeout)

    return numbers


def bubble_sort(numbers):
    iterator: int = 0

    numbers = move_to_end(numbers, find_smallest_index(numbers))

    while find_smallest_index(numbers) != 0:
        numbers, iterator = iteration(numbers, iterator)

    global NUMBER_COMPARED
    global NUMBER_SWITCHED
    print("Numbers compared: {}".format(NUMBER_COMPARED))
    print("Numbers switched: {}".format(NUMBER_SWITCHED))
    NUMBER_COMPARED = 0
    NUMBER_SWITCHED = 0

    return numbers
