def bubble_sort(unsorted_list):

    tmp_list = unsorted_list

    for o_index in range(len(tmp_list)):
        
        for i_index in range(len(tmp_list)):
        
            if tmp_list[o_index] < \
                tmp_list[i_index]:
                
                tmp = tmp_list[i_index]
                tmp_list[i_index] = \
                    tmp_list[o_index]
                tmp_list[o_index] = tmp

    return tmp_list
    
print(
    bubble_sort(
        [5,2,3,1,8]
    )
)




# version format 1.1.1
# version seperator "."
def compare_version_number(version_number_lhs,version_number_rhs):
    # split with separator
    # assume equal size
    # convert to number
    # compare each index 
    pass

def comparator(operator):
    pass

def is_greater(version_number_lhs,version_number_rhs):

    version_number_lhs_list = \
        version_number_lhs.split(".")

    version_number_rhs_list = \
        version_number_rhs.split(".")


    # find the shortest
    shortest_list = \
        version_number_lhs_list if \
            len(version_number_lhs_list) < len(version_number_rhs_list)\
                else version_number_rhs_list

    # loop
    for index,element in enumerate(shortest_list):
        # if both are equal 
        # proceed
        if int(version_number_lhs_list[index]) == \
            int(version_number_rhs_list[index]):
            continue

        if int(version_number_lhs_list[index]) > \
            int(version_number_rhs_list[index]):
            return True
        else:
            return False

    if len(version_number_lhs_list) > len(version_number_rhs_list):
        return True
    else:
        return False

        
def bubble_sort_v(unsorted_list):
    
    tmp_list = unsorted_list

    for o_index in range(len(tmp_list)):
        
        for i_index in range(len(tmp_list)):
        
            if is_greater(
                tmp_list[i_index],
                tmp_list[o_index]
                ):
                
                tmp = tmp_list[i_index]
                tmp_list[i_index] = \
                    tmp_list[o_index]
                tmp_list[o_index] = tmp

    return tmp_list

# print(
#     is_greater(
#     "1.2.1",
#     "1.2.3.4"
#     )
# )
    


# print(
#     sorted(
#      ["1.2.3.4","1.2.3"],
#      cmp=is_greater
#      )
# )

# print(
#     sorted(
#      ["1.2.3.4","1.2.5"],
#      cmp=is_greater
#      )
# )


print(
    bubble_sort_v(
        [
            "1.2.3.4",
            "1.2.5",
            "1.2.2.4",
            "1.2.6"
        ]
    )
)