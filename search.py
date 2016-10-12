#!/usr/bin/env python3

# find all strings in a list that have a given prefix

def prefix_search(strings, prefix):
    assert(isinstance(strings, list))
    assert(isinstance(prefix, str))

    if len(strings) == 0:
        return []

    elif len(strings) == 1:
        string = strings[0]
        if string[:len(prefix)] == prefix:
            return [string]
        else:
            return []

    else:
        index = int(len(strings) / 2)
        return prefix_search(strings[:index], prefix) \
             + prefix_search(strings[index:], prefix)


# find all phone numbers with matching area code

phone_numbers = ["0223 788834", "0201 657543", "0435 287784", "0348 394947", "0201 658843"]
area_codes = ["0201", "0204", "0223"]

for area_code in area_codes:
    matching_numbers = prefix_search(phone_numbers, area_code)
    print("{} : {}".format(area_code, matching_numbers))
