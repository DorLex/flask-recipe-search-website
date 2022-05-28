import time
from random import randint

from parser_href import *

PAGES_QUANTITY = 10


def main():
    for page in range(1, PAGES_QUANTITY + 1):
        as_some_page = get_recipes_a(page)
        hrefs_some_page = get_recipes_href(as_some_page)
        content = get_content(hrefs_some_page)

        print('\n'.join(content))
        # print('\n'.join(hrefs_some_page))

        print(f'Обработал {page}/{PAGES_QUANTITY} страниц')
        time.sleep(randint(2, 5))


if __name__ == '__main__':
    main()
