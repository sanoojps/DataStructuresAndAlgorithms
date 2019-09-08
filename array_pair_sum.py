# find all pairs of elements that produce a given sum

def get_char_count_map(char_list):
    char_count_map = dict()

    for char in char_list:
        lowercased_char = char

        if isinstance(char,str):
            lowercased_char = char.lower()
        
        if lowercased_char in char_count_map:
            char_count = char_count_map[lowercased_char]
            new_char_count = char_count + 1
            char_count_map[lowercased_char] = new_char_count

        else:
            if isinstance(char,str):
                if not char.isspace():
                    char_count_map[lowercased_char] = 1
            else:
                 char_count_map[lowercased_char] = 1
            

    print("char_count_map: {} ".format(char_count_map))

    return char_count_map

def increment_char_count(char_count_map,lowercased_char):
    
    if lowercased_char in char_count_map:
            char_count = char_count_map[lowercased_char]
            new_char_count = char_count + 1
            char_count_map[lowercased_char] = new_char_count

    else:
        char_count_map[lowercased_char] = 1
    
    return char_count_map

def pairs_with_sum(sum, array):
    # make an array 
    common_sum_pairs = list()

    char_count_map = dict()

    current_index = 0
    for o_index,o_element in enumerate(array):
        current_index = o_index

        char_count_map = \
        increment_char_count(
            char_count_map,
            o_element
            )

        # add first element to pair
        for i_index,i_element in enumerate(array):
            # skip the element at current index
            if i_index == current_index:
                continue
            else:
                # sum
                t_sum = o_element + i_element
                # check if sum == given sum
                if t_sum == sum:
                    # check if inner element is in the char map
                    if i_element in char_count_map:
                        # get the count of inner and outer elements
                        i_char_count = char_count_map[i_element]
                        o_char_count = char_count_map[o_element]
                        # check if both counts are greater than one
                        # this ensures unique pairing
                        if i_char_count >= 1  \
                            and o_char_count >= 1:
                            # move the unique pairs to array
                            common_sum_pairs.append(
                            [o_element,i_element]
                            )
                            # decrement char count 
                            # fetch char count first
                            # to handle the edge case where
                            # both inner and outer elements are the same
                            # as we are mutating the char map
                            i_char_count = char_count_map[i_element]
                            char_count = i_char_count - 1
                            char_count_map[i_element] = \
                                char_count

                            o_char_count = char_count_map[o_element]
                            char_count = o_char_count - 1
                            char_count_map[o_element] = \
                                char_count
                    

    print(char_count_map)
    print(common_sum_pairs)


# //expected output
# (4,0),(3,1)
print(
    "is_anagram: {} ".format(
        pairs_with_sum(
        4,
        [1,2,1,4,4,0,3],
        )
    )
)

# //expected output
# (4,0),(3,1),(4,0)
print(
    "is_anagram: {} ".format(
        pairs_with_sum(
        4,
        [1,2,1,4,4,0,3,0],
        )
    )
)


print(
    "is_anagram: {} ".format(
        pairs_with_sum(
        2,
        [1,2,1],
        )
    )
)

print(
    "is_anagram: {} ".format(
        pairs_with_sum(
        3,
        [1,2,1],
        )
    )
)

print(
    "is_anagram: {} ".format(
        pairs_with_sum(
        4,
        [1,2,1],
        )
    )
)