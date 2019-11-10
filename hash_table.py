# key vale pair
# each position in a hash table u called slot
# mapping between an item and the slot where the item belongs
#   in the hash table is called hash function 
# slot index genrated by hash function
# an example of a hash function is mod
# load factor = number_of_item_table_size
# folding  method
# ***************
#  divide item into equal size
#  eg: phone number 436-555-4601
#      divide digits into two groups 
    #       (43,65,55,46,01)
    #    we add 43+65+55+46+01 = 210
    #    hash table has 11 slots
    #    210 % 11 = 1 .. so phone number goes to slot 1
# mid-square  method
# ***************
#  first square the item
#  extract some portion of the resulting digits
#  eg: number 44
#      compute square 44*44 = 1936
    #     extract middle 2 digits 93
    #     hash table has 11 slots
    #    93 % 11 = 5 .. so phone number goes to slot 5
# hash number for no integer values
#  using ordinal value
# eg: wor 'cat' be thought to be a sequence of ordinal values
# Collision Resolution
# ********************
#  open addressing
    #  tries to find thenext open slot by sequentially moving across slots
#  linear probing
# 