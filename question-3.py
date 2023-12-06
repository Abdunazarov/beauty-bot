# stdlib
from typing import List

# project
from settings import DIFF_LIST, JSON_NEW, JSON_OLD

def find_json_diff(json_old: dict, json_new: dict, diff_list: List[str]):
    result = {}

    for key in diff_list:
        if key in json_old['data'] and key in json_new['data']:
            old_value = json_old['data'][key]
            new_value = json_new['data'][key]

            if old_value != new_value:
                result[key] = new_value

    return result


def test_fin_json_diff():
    result = find_json_diff(
        json_old=JSON_OLD, json_new=JSON_NEW, diff_list=DIFF_LIST,
    )

    assert result == {
        'services': [{
            'id': 22222225, 'title': 'Стрижка', 'cost': 1500,
            'cost_per_unit': 1500, 'first_cost': 1500, 'amount': 1,
        }], 'datetime': '2022-01-25T13:00:00+03:00',
    }
