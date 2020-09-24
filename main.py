def find_greatest_index(numbers):
    greatest_val: int = max(numbers)
    return numbers.index(greatest_val)


def find_smallest_index(numbers):
    smallest_val: int = min(numbers)
    return numbers.index(smallest_val)


if __name__ == '__main__':
    list = [2,5,1,3,7,9,12,15,21,13,4, 16, 92, -2, 3]

    iterator = 0

    smallest_index = find_smallest_index(list)
    takeout = list.pop(smallest_index)
    list.append(takeout)

    while find_smallest_index(list) != 0:
        try:
            if list[iterator] > list[iterator+1]:
                first_val = list[iterator]
                second_val = list[iterator+1]
                list[iterator] = second_val
                list[iterator+1] = first_val
            else:
                iterator += 1
        except IndexError:
            iterator = 0

    print(list)