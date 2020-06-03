def bsearch(a, v):
    l = 0
    r = len(a)
    while l < r:
        mid = l + (r - l) // 2
        if a[mid] < v:
            l = mid + 1
        else:
            r = mid
    
    return l


def bsearch2(a, v):
    l = 0
    r = len(a)
    while l < r:
        mid = l + (r - l) // 2
        if a[mid] <= v:
            l = mid + 1
        else:
            r = mid
    
    return l

if __name__ == '__main__':
    a = [3,3,3,6,6,6,9,9,9,13,14,14,15,16,16]
    print(bsearch(a, 2))
    print(bsearch(a, 3))
    print(bsearch(a, 16))
    print(bsearch(a, 17))
    print(bsearch2(a, 2))
    print(bsearch2(a, 3))
    print(bsearch2(a, 16))
    print(bsearch2(a, 17))