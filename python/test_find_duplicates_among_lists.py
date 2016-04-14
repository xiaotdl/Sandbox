def find_duplicates(l1, l2):
    result = []
    if not l1 or not l1:
        return result

    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            i += 1
        elif l1[i] > l2[j]:
            j += 1
        else:
            result.append(l1[i])
            i += 1
            j += 1
            while i < len(l1) and l1[i] == l1[i - 1]: i += 1
            while j < len(l2) and l2[j] == l2[j - 1]: j += 1

    return result


if __name__ == '__main__':
    l1 = [1,3,4,4,4,4,5,5,6,7]
    l2 = [0,2,3,4,4,5,8]

    actual = find_duplicates(l1, l2)
    expect = set(l1) & set(l2)

    assert set(actual) == set(expect) and len(actual) == len(expect)
    print 'Cool!'
