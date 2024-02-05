#In this Kata, you will be given an integer array and your task is to return the sum of elements occupying prime-numbered indices.
#The first element of the array is at index 0.

def total(arr):
    def is_prime(k):
        if k <= 1:
            return False
        elif k == 2:
            return True
        elif k % 2 == 0:
            return False
        else:
            for i in range(3, int(k**0.5) + 1, 2):
                if k % i == 0:
                    return False
            return True
    
    return sum([v for k, v in enumerate(arr) if is_prime(k)])