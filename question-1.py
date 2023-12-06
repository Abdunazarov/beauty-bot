# stdlib
import re
from typing import List

# project
from settings import KEYS_PATTERN, LIST_KEYS, TEST_TEXT


def validate_keys(list_keys: List[str], text: str):
    keys_in_text = re.findall(KEYS_PATTERN, text)
    missing_keys = []
    existing_keys = []

    if text.count("{") != text.count("}"):
        return "Error: Unmatched opening and closing brackets"

    for key in keys_in_text:
        if key not in list_keys:
            missing_keys.append(key)
        else:
            existing_keys.append(key)

    missing_keys_not_found = list(set(list_keys) - set(existing_keys))

    return {
        "missing_keys_not_found": missing_keys_not_found,
        "missing_keys_in_text": missing_keys,
    }


def test_validate_keys():
    result = validate_keys(list_keys=LIST_KEYS, text=TEST_TEXT)

    assert result == {
        "missing_keys_not_found": [
            "end_time",
            "day_of_week",
        ],
        "missing_keys_in_text": ["record_link"],
    }, result
