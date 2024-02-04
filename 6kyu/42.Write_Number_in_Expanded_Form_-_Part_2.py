#You will be given a number and you will need to return it as a string in expanded form.
#For example:
#expanded_from(807.304); // Should return "800 + 7 + 3/10 + 4/1000"
#expanded_from(1.24); // should return "1 + 2/10 + 4/100"
#expanded_from(7.304); // should return "7 + 3/10 + 4/1000"
#expanded_from(0.04); // should return "4/100"

from fractions import Fraction

def expanded_form(num):
    x1, x2 = str(num).split('.')
    
    top = [str(int(x) * 10**(len(x1) - i - 1)) for i, x in enumerate(x1) if x != '0']
    bottom = [f"{x}/{10**(j+1)}" for j, x in enumerate(x2) if x != '0']
    
    return ' + '.join(top + bottom)