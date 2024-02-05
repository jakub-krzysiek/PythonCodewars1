#Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
#The output should be two capital letters with a dot separating them.
#It should look like this:
#Sam Harris => S.H
#patrick feeney => P.F

def abbrev_name(name):
    initial=""
    if (len(name) == 0):
        return

    first_middle_last = name.split(" ")
    for word in first_middle_last:
        initial = initial+word[0].upper()+"."
    return initial[:-1]