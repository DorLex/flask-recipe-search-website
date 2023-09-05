from random import randint


def _get_random_num():
    random_num = randint(1, 10)
    return random_num


def get_ingredient_num(used_numbers):
    while True:
        random_num = _get_random_num()

        if not used_numbers.get(random_num):
            used_numbers[random_num] = True

            return random_num
