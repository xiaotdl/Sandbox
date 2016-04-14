l1 = [1,3,4,4,4,4,5,5,6,7]
l2 = [0,2,3,4,4,5,8]

def find_duplicates(l1, l2):
    result = []
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

actual = find_duplicates(l1, l2)
expect = set(l1) & set(l2)
assert set(actual) == set(expect) and len(actual) == len(expect)
print 'Cool!'
