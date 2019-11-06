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

print(
    "is_anagram: {} ".format(
        pairs_with_sum(
        4,
        [1,2,3,4],
        )
    )
)


# Logic O(n2)
#  --- we need to repeat elements in a par
#  --- the same number of times as they are in the array
# 1. Make a dict with element as key and count of element as value
# 2. loop  through the array
# 3. loop through the array
# 4. Compare each element to the adjacent element and check 
#       if teh sum is equal
#  5. If sum is equal
#        . Check if the elements count is zero
            # . if zero that mean we have already encountered the element
            #.. if not then we decrement the count 

# Logic O(n)
# Use 2 sets
#  loop through the array
#  add current number to  "already seen" set
#  we have a sum 
#  we have a number which is the current number
#  we check if  sum - current_number is present 
#    in the array
# add the pair to the output
def array_pair_sum_On(list,sum):

    seen = set()
    output = set()

    for element in list:

        target = sum - element

        if target not in seen:
            seen.add(element)

        else:
            output.add(
                (element,target)
            )

    print(
       output
    )

    
array_pair_sum_On(
    (1,3,2,2),
    4
)