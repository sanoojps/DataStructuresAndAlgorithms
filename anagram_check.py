
def is_anagram(string_one,string_two):
    # Logic
    # count the letters in each word
    # if count of each letter in one string
    # matches the count of the same letter in the 
    # other string...
    # then it is an anagram

    char_count_map = dict()

    for char in string_one:
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

    for char in string_two:
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
            return False

    return is_zero

print(
    "is_anagram: {} ".format(
        is_anagram(
        "ban an a",
        "banana"
        )
    )
)

print(
    "is_anagram: {} ".format(
        is_anagram(
        "banana",
        "Ban an a",
        )
    )
)

print(
    "is_anagram: {} ".format(
        is_anagram(
        "Clint Eastwood",
        "Old West Action",
        )
    )
)
