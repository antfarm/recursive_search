#!/usr/bin/env python3

# find all elements in a list that satisfy a given condition

def search(elements, condition):
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
    return search(strings, lambda e: string_has_prefix(e, prefix))


def string_has_prefix(string, prefix):
    return string[:len(prefix)] == prefix


# find all phone numbers with matching area code

phone_numbers = ["0223 788834", "0201 657543", "0435 287784", "0348 394947", "0201 658843"]
area_codes = ["0201", "0204", "0223"]

for area_code in area_codes:
    matching_numbers = prefix_search(phone_numbers, area_code)
    print("{} : {}".format(area_code, matching_numbers))
