def first_uniq_char(s):
    n = len(s)
    for i in range(n):
        is_unique = True
        for j in range(n):
            if i != j and s[i] == s[j]:
                is_unique = False
            break
        if is_unique:
            return i

    return -1
