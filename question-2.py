# stdlib
from typing import List

# project
from settings import EXAMPLE_LIST


def count_elements(elements_list: List[list]):
    duplicates = []
    result_with_count = []

    for x in elements_list:
        if x not in duplicates:
            count = elements_list.count(x)

            result_with_count.append(x + [count])

        duplicates.append(x)

    return result_with_count


def test_count_elements():
    result = count_elements(elements_list=EXAMPLE_LIST)

    assert result == [['665587', 2, 1], ['669532', 1, 2], ['669537', 2, 1], ['665587', 1, 1],], result
