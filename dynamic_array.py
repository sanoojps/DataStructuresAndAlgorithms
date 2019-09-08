# Incrementally increasing in size

import ctypes

# Logic:
# Resize the array after it reaches initially
# assigned capacity

class Dynamic_Array(object):

    def __init__(self):
        super(Dynamic_Array, self).__init__()

        self.count = 0
        self.capacity = 1

        self.internal_storage_array = \
            self.make_array(self.capacity)

    def __len__(self):
        return self.count


    def __getitem__(self,k):

        if not 0 <= k < self.count:
            return IndexError('K in of bounds!')

        return self.internal_storage_array[k]


    def append(self, element):

        if self.count == self.capacity:
            # 2x if capacity isn't enough
            self._resize(2*self.capacity)

        self.internal_storage_array[self.count] = \
            element;
        self.count += 1

    def _resize(self,new_capacity):

# make new array
        new_temp_array = \
            self.make_new_array(new_capacity)

# copy all elements to that array
        for index in range(self.count):
            new_temp_array[index] = \
                self.internal_storage_array[index]

        self.internal_storage_array = \
            new_temp_array

        self.capacity = new_capacity


    def make_array(self,new_capacity):

        return (new_capacity * ctypes.py_object)()





    
        
