#You are given a message (text) that you choose to read in a mirror (weirdo). Return what you would see, complete with the mirror frame.

#Example:
#'Hello World'
#would give:

#'*********
#* olleH *
#* dlroW *
#*********'

#Words in your solution should be left-aligned.

def mirror(text):
    words = [word[::-1] for word in text.split(' ')]
    longest = max(words, key=len)
    mirror_frame = '*' * (len(longest) + 4)
    result = [mirror_frame] + ['* {:<{}} *'.format(word, len(longest)) for word in words] + [mirror_frame]
    return '\n'.join(result)