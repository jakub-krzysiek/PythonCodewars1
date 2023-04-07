def abbrev_name(name):
    initial=""
    if (len(name) == 0):
        return

    first_middle_last = name.split(" ")
    for word in first_middle_last:
        initial = initial+word[0].upper()+"."
    return initial[:-1]