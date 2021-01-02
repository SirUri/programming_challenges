def mergingLetters(s, t):
    """
    Merges the letters of s and t alternating
    """
    result = ""
    order = True
    i = 0
    j = 0
    while (i + j) <= (len(s) + len(t) - 2):
        if order and i < len(s):
            result += s[i]
            i += 1
            if j < len(t):
                order = not order
        elif j < len(t):
            result += t[j]
            j += 1
            if i < len(s):
                order = not order
    return result

mergingLetters("aaaaa","bbb")