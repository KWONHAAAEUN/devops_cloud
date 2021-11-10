def make_powerd_list(numbers):
    new_numbers = []
    for number in numbers:
        new_numbers.append(number ** 2)
    return new_numbers


def make_powerd_list2(numbers):
    make_power = lambda number: number ** 2
    return list(map(make_power, numbers))
