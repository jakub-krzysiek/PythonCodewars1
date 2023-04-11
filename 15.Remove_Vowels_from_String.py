def disemvowel(string_):
    vowels = ['a','e','i','o','u']
    string_ = [letter for letter in string_ if letter.lower() not in vowels]
    string_ = ''.join(string_)
    return string_