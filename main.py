
def nww(first, second):
    first_prime_factors = get_prime_factors(first)
    second_prime_factors = get_prime_factors(second)
    first_size = len(first_prime_factors)
    second_size = len(second_prime_factors)
    shorter_list = []
    if first_size < second_size:
        shorter_list.append(first_prime_factors)
    else:
        shorter_list.append(second_prime_factors)
    to_remove = []
    for element in shorter_list:
        occur = shorter_list.count()





def get_prime_factors(number):
    current = number
    prime_factors = []
    if number < 2:
        return prime_factors

    while current != 1:
        for divider in range(2, current + 1):
            if is_prime_number(divider):
                if current % divider == 0:
                    current = int(current / divider)
                    prime_factors.append(divider)

    return prime_factors


def is_prime_number(number):
    if number == 2:
        return True
    if number <= 1:
        return False
    if number % 2 == 0 and number > 2:
        return False
    dividers = range(2, number)
    for divider in dividers:
        if number % divider == 0:
            return False

    return True


for _number in range(0, 100):
    # print(str(_number) + ": " + str(is_prime_number(_number)))
    print(str(_number) + ": " + str(get_prime_factors(_number)))


