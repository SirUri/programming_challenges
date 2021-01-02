def reduceTheNumber(number, k):
    """
    Algorithm. It splits the numbers into groups of size k (if possible,
    if not, the last element will be a different size). Sums the groups
    and joins them to form another number. Repeat until len(number) <= k
    """
    while len(number) > k:
        new_list = []
        ele2ap = ""
        len_group = 0
        for i in range(len(number)):
            ele2ap += number[i]
            len_group += 1
            if (len_group == k) or i == len(number)-1:
                new_list.append(ele2ap)
                ele2ap = ""
                len_group = 0
        for i in range(len(new_list)):
            new_list[i] = list(new_list[i])
            total_sum = 0
            for j in range(len(new_list[i])):
                total_sum += int(new_list[i][j])
            new_list[i] = str(total_sum)
            number = "".join(new_list)

reduceTheNumber("1111122222",3)