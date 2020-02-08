'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # Functions gets in an input of a string
    # Looking for "th" occurences exactly, lower case 
    # Has to use recursion
    # Can't have "th" if string length is only 1

    # Check if first index and the one right after are "th"
    # If it is then return 1 + recursion
    # return recursion

    if len(word) <= 1:
        return 0
    
    if word[0] is "t" and word[1] is "h":
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])
