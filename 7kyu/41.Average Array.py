#Create a function that takes a 2D array as an input, and outputs another array that contains the average values for the numbers in the nested arrays at the corresponding indexes.
#Note: the function should also work with negative numbers and floats.

def avg_array(arrs):
    res = []
    counter = 0
    for i in range(len(arrs[0])):
        for arr in arrs:
            counter += arr[i]
        counter /= len(arrs)
        res.append(counter)
        counter = 0
    return res