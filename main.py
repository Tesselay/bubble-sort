

def find_greatest_index(numbers):
    greatest_val: int = max(numbers)
    return numbers.index(greatest_val)


def find_smallest_index(numbers):
    smallest_val: int = min(numbers)
    return numbers.index(smallest_val)


if __name__ == '__main__':
    list = [2,5,1,3]

    iterator = 0

    smallest_index = find_smallest_index(list)
    takeout = list.pop(smallest_index)
    list.append(takeout)

    while find_greatest_index(list) != len(list) - 1:
        try:
            if list[iterator] > list[iterator+1]:
                takeout = list.pop(iterator)
                list.append(takeout)
            else:
                iterator += 1
        except IndexError:
            iterator = 0

    print(list)