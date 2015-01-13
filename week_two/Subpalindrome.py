# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 



def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    if not text:return (0,0)
    text = text.upper()
    return max([getPalindromeAt(i, text) for i in xrange(len(text))],
               key=lambda index: index[1] - index[0]) 
               

def getPalindromeAt(position, string):
    longest = (position, position)
    for lower, upper in [(position - 1, position + 1),
                         (position, position + 1)]:
        while lower >= 0 and\
              upper < len(string) and\
              string[lower] == string[upper]:
            upper += 1
            lower -= 1
        longest = max(longest, (lower + 1, upper - 1),
                      key = lambda a: a[1] - a[0])
    return longest[0],longest[1] + 1


    
def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()