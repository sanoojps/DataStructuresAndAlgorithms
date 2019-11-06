#!/usr/bin/env python3

# 2 arrays
#  array2 is created by shuffling elements
#  of array 1 and then
#  deleting one random element
#  FInd the deleted element


def find_the_missing_element(list,shuffled_list):

    # if allowed to use sets
    #  convert both list to set and 
    # then take the difference

    # if not, loop through both and find
    #  the missing element

    # better solution is use a dictionary
    # that stores the count of all value

    largest = list if len(list) > len(shuffled_list) else shuffled_list
    
    char_count_map = dict()

    for char in largest:
        lowercased_char = char.lower()
        if lowercased_char in char_count_map:
            char_count = char_count_map[lowercased_char]
            new_char_count = char_count + 1
            char_count_map[lowercased_char] = new_char_count

        else:
            if not char.isspace():
                char_count_map[lowercased_char] = 1
            else:
                pass

    print("char_count_map: {} ".format(char_count_map))

    for char in shuffled_list:
        lowercased_char = char.lower()
        if not lowercased_char.isspace():
            # all characters in the second string
            # should be present in the first string
            if lowercased_char not in char_count_map:
                return False
            else:
                char_count = char_count_map[lowercased_char]
                new_char_count = char_count - 1
                char_count_map[lowercased_char] = new_char_count

        else: 
            pass

    # check if all values in the count map is zero
    is_zero = False
    for value in char_count_map.values():
        print("value: {} ".format(value))
        if value is 0:
            is_zero = True
        else:
            print("Missing value: {} ".format(value))
            return False




