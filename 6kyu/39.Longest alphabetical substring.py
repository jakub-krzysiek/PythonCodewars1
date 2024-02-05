#Find the longest substring in alphabetical order.
#Example: the longest alphabetical substring in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".
#There are tests with strings up to 10 000 characters long so your code will need to be efficient.
#The input will only consist of lowercase characters and will be at least one letter long.
#If there are multiple solutions, return the one that appears first.
#Good luck :)

def longest(st):
    res = []
    temp = st[0]
    for i in range(1, len(st)):
        if ord(st[i]) >= ord(temp[-1]):
            temp += st[i]
        else:
            res.append(temp)
            temp = st[i]
    res.append(temp)

    return max(res, key=len)