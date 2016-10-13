#!/usr/bin/env python3

import inspect

# find all elements in a list that satisfy a given condition

def search(elements, condition):
    assert isinstance(elements, list), "first argument should be a list"
    assert callable(condition), "second argument should be callable"
    assert len(inspect.getargspec(condition).args) == 1, "second argument should take exactly one argument"

    if len(elements) == 0:
        return []

    elif len(elements) == 1:
        element = elements[0]
        return [element] if condition(element) else []

    else:
        index = int(len(elements) / 2)
        return search(elements[:index], condition) \
             + search(elements[index:], condition)


# find all strings in a list that have a given prefix

def prefix_search(strings, prefix):
    assert isinstance(strings, list), "first argument should be a list"
    assert isinstance(prefix, str), "second argument should be a string"

    return search(strings, lambda s: string_has_prefix(s, prefix))


def string_has_prefix(string, prefix):
    assert isinstance(string, str), "first argument should be a string"
    assert isinstance(prefix, str), "second argument should be a string"

    return string[:len(prefix)] == prefix


# find all phone numbers with matching area code

phone_numbers = ["0223 788834", "0201 657543", "0435 287784", "0348 394947", "0201 658843"]
area_codes = ["0201", "0204", "0223"]

for area_code in area_codes:
    matching_numbers = prefix_search(phone_numbers, area_code)
    print("{} : {}".format(area_code, matching_numbers))
