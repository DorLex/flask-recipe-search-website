from random import randint


def _get_random_num() -> int:
    return randint(1, 10)


def get_ingredient_num(used_numbers: set) -> int:
    while True:
        random_num: int = _get_random_num()

        if random_num not in used_numbers:
            used_numbers.add(random_num)

            return random_num
