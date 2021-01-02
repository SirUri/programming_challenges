def h_count(s):
    """
    Given a molecule, return the number of Hydrogen atoms.
    >>> "H20"
    2
    
    """
    count = 0
    for i in range(len(s)):
        if (i != len(s) - 1): #No es lo ultimo
            if s[i] == "H" and s[i+1].isdigit():
                count += int(s[i+1])
            elif s[i] == "H":
                count += 1
        elif s[i] == "H":
            count += 1
    return count


