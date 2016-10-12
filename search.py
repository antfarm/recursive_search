#!/usr/bin/env python3

# search strings by prefix

def prefix_search(strings, prefix):
    if len(strings) == 1:
        string = strings[0]
        if string[:len(prefix)] == prefix:
            return [string]
        else:
            return []
    else:
        index = int(len(strings) / 2)
        return prefix_search(strings[:index], prefix) \
             + prefix_search(strings[index:], prefix)


# use function to search phone numbers with matchong area code

phone_numbers = ["0223 788834", "0201 657543", "0435 287784", "4348 394947", "0201 658843"]
area_codes = ["0201", "0204", "0223"]

for area_code in area_codes:
    matching_numbers = prefix_search(phone_numbers, area_code)
    print("{} : {}".format(area_code, matching_numbers))
