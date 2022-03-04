"""
Exercise 3: Algorithmic Test
Write a Python program to convert an integer to a roman numeral. Roman digits are:
digits = ["M", "CM", "D", "CD”, "C", "XC", "L", "XL”, "X", "IX", "V", "IV", "I"]

The implementation is a function that takes an integer and returns a string.
The return string is roman numeral.
Roman numeral system has 13 digits. These are mapped from string representation,
    creating a dictionary of translation from Hindu-arabic system to Roman system.

In roman numeral, the letter M represent thousands.

$ python3 ex3_numalgo.py

3 III
10 X
100 C
5432 MMMMMCDXXXII

This solution is yet to optimize. Only one pass and some input samples were tested.
Time: one hour coding original solution, plus 10 minutes review and tests.

Time: took about two hours I think.
See that there are some leetcode solutions, but chose to do this myself.
So this is still a version 1.
"""
# digits are given (13)
# digits = ["M", "CM", "D", "CD”, "C", "XC", "L", "XL”, "X", "IX", "V", "IV", "I"]

# Reference https://en.wikipedia.org/wiki/Roman_numerals
# 1. mapping from integer to roman numeral
int2roman = {   1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L",
                40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"   }
# 2. mapping from roman numeral to integer
roman2int = {   "M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50,
                "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1   }

def value_between(int_val, lower, upper):
    """Determine if the integer is betwen two values."""
    if (int_val >= lower) and (int_val <= upper):
        return True
    return False

def roman_1to9(int_val):
    """Return roman numeral for integer value 1-9.
        Zero also return empty string."""
    d = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX", 0:""}
    return d[int_val]

def roman_10to99(int_val):
    """Return roman numeral for integer value 10-99.
        Exception are: L=50,XL=40,XC=90. Zero returns empty string.
        99 is XCXI. 90 is XC.
        80 is LXXX and 89 is LXXXXI"""
    fc = str(int_val)[0] # first char
    m = int_val % 10 # modulo of ten
    # 90-99. Starts with 90 then append the 1to9 digits.
    if value_between(int_val, 90, 99):
        output = roman2int[90] + roman_1to9(m) # 'XC' append modulo
        return output
    # 50-89. Starts with dictionary of first digit then append the 1to9 digits.
    if value_between(int_val, 50, 89):
        output = {"5": "L", "6": "LX", "7": "LXX", "8": "LXXX"}
        output = output[fc] + roman_1to9(m) # 'LXXX' append modulo
        return output
    # 40-49. Starts with dictionary of first digit then append the 1to9 digits.
    if value_between(int_val, 40, 49):
        output = roman2int[40] + roman_1to9(m) # 'XC' append modulo
        return output
    # 10-39. Starts with dictionary of first digit then append the 1to9 digits.
    if value_between(int_val, 10, 39):
        output = {"1": "X", "2": "XX", "3": "XXX"}
        return output[fc] + roman_1to9(m) # 'LXXX' append modulo
    if int_val == 0:
        return ""
    # SHOLD NOT GET HERE

def roman_100to999(int_val):
    assert len(str(int_val)) == 3
    fc = str(int_val)[0] # first char
    sc = str(int_val)[1] # second char. Can also use modulo of 100.
    m = int_val % 10 # modulo of ten
    # combine second digit with last digit and get the last portion.
    last2digits = int(sc+str(m)) # Or  int_val % 100
    last2digits = roman_10to99(last2digits)
    # hundreds
    hundreds = {"1": "C", "2": "CC", "3": "CCC", "4": "CD", "5": "D", "6": "DC", "7": "DCC", "8": "DCCC", "9": "CM"}
    output = hundreds[fc] # the roman representation for hundreds
    output += last2digits # then append the last two digits
    return output

def roman_number(int_val):
    """Takes integer value and returns roman numeral string."""
    assert int_val > 0 # greater than 0
    # make intger a string, so can inspect digits
    si = str(int_val)
    # count the length of integer representation
    nl = len(si)
    # case analysis
    # - first break down the integer into group of thousands.
    # - use subtraction of integer to get number of M digits.
    c = int_val # use the int value as counter
    m_count = 0
    output = ""
    while(c-1000 > 0):
        m_count += 1
        output += "M" # create M digits
        c -= 1000 # decrement counter
    # Get the hundreds
    remaind = int_val % 1000
    if value_between(remaind,100,999):
        output += roman_100to999(remaind)
    if value_between(remaind,10,99):
        output += roman_10to99(remaind)
    if value_between(remaind,0,9):
        output += roman_1to9(remaind)
    return output

if __name__ == '__main__':
    print(3,roman_number(3))
    print(10,roman_number(10))
    print(100,roman_number(100))
    print(5432,roman_number(5432))
