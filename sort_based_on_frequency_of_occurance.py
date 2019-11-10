# tree to be sorted as "eert

def sort_based_on_frequency_of_occurrance(word_to_sort):
    
    class CharToCountMap:
        def __init__(self):
            self.__char = None
            self.__count = None

        @property
        def char(self):
            return self.__char

        @char.setter
        def char(self,char):
            self.__char = char;

        @property
        def count(self):
            return self.__count

        @count.setter
        def count(self,count):
            self.__count = count

        def __eq__(self, value):
                return self.__char.__eq__(value.char)

        def __hash__(self):
                return self.__char.__hash__()

        def __repr__(self):
                return "char: {}, count: {}".format(self.char,self.count)


    charToCountMapSet = set()

    def get_matching_element_from_list(object,a_list):
        is_present = None  
        for element in a_list:
            if type(a_list) is set:
                if element == object:
                    is_present = element
                    break
            else:
                if element.char == object.char:
                    is_present = element
                    break
        return is_present

    for char in word_to_sort:
        # check if word in set
        # if yes
        #    then get "count"
        #    increment count
        # if no
        #     then create charToCountMap
        #     add count = 1
        newCharCountMap = CharToCountMap()
        newCharCountMap.char = char
        newCharCountMap.count = 1
        element = get_matching_element_from_list(newCharCountMap,charToCountMapSet)
        if element is not None:
            newCharCountMap.count = element.count + 1
            charToCountMapSet.remove(newCharCountMap)
        
        charToCountMapSet.add(newCharCountMap)

    def comperator(lhs,rhs):
        if lhs.count >= rhs.count:
            return lhs.count
        else:
            return rhs.count    

    # default sort is ascending
    sortedCharToCountMapSet = sorted(
            charToCountMapSet,key=lambda item: item.count, reverse=True
        )
    print(
        sortedCharToCountMapSet
    )

    def replicate_string(string,times):
        string_accrue = ""
        for index in range(0,times):
            string_accrue = string_accrue + string
        return string_accrue



    sortedString = ""
    for charToCountMap in charToCountMapSet:
        stringFromCharToCountMap = replicate_string(charToCountMap.char,charToCountMap.count)
        sortedString = sortedString + stringFromCharToCountMap

    print(sortedString)

    # newCharCountMap = CharToCountMap()
    # newCharCountMap.char = "t"
    # newCharCountMap.count = 1

    # newCharCountMapSingleSet =  set([newCharCountMap])

    # print(
    #     charToCountMapSet
    # )

    # print(
    #     newCharCountMap in charToCountMapSet
    # )

    # print(
    #     charToCountMapSet.intersection(
    #         newCharCountMapSingleSet
    #         )   
    # )

    # print(
    #     set([newCharCountMap]).difference_update(
    #         newCharCountMapSingleSet
    #     )  
    # )

    # print(
    #     newCharCountMapSingleSet.difference_update(
    #         set([newCharCountMap])
    #     )  
    # )




sort_based_on_frequency_of_occurrance("treee") # return eeert
sort_based_on_frequency_of_occurrance("trrrreee") # return rrrreeet



