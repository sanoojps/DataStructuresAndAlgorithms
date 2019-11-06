# Find the largest continuous sum from an array of +ve and -ve numbers

# def get_largest_continuous_sum(list):

#     current_sum = None

#     for element in list:

#         if current_sum is None:
#             current_sum = element
#         else:

map = {
    1:20,
    2:30,
    3:30,
    4:23,
    5:22,
    6:21,
    7:27,
    8:25,
    9:26,
    10:20
    }

def find_sequence(temp_map):

    current_mean = 0
    current_min = 0 
    current_max = 0

    main_sequence = []
    current_sequence = []

    for k,v in temp_map.items():
        
        if current_min == 0 and current_max == 0:
            current_min = v
            current_max = v
            continue

        if current_max < v:
            current_max = v

        if current_min > v:
            current_min = v

        if current_max - current_min < 5 and not 0:
            current_sequence.append(k)
        else :
            current_min = v
            current_max = v
            if len(main_sequence) == 0:
                main_sequence = current_sequence
            else:
                main_sequence.append(current_sequence)
                current_sequence = []
            continue

    return current_sequence

    
find_sequence(map)
    

            



    


    




