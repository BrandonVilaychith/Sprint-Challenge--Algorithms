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
        # Keep adding 1 if it matches and all the 
        # 1's will bubble back up and add to a total
        return 1 + count_th(word[1:])
    else:
        # if not a match then won't add one and skip 
        # adding 1 during bubbling
        return count_th(word[1:])

# [th]htthht
# 1 + count
# t[hh]tthht  // hhtthht
# count
# th[ht]thht  // htthht
# count
# thh[tt]hht  // tthht
# count
# thht[th]ht // thht
# 1 + count
# thhtt[hh]t  // hht
# count       
# thhtth[ht]  // ht
# count 
# ENDS HERE ON BASE CASE  // t (t is now passed in and is only 1 character long)
