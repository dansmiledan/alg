def compute_next(s):
    n = len(s)
    k = -1
    j = 0
    nexta = list()
    nexta.append(-1)
    while (j < n-1):
        if k == -1 or s[k] == s[j]:
            k = k + 1
            j = j + 1
            if s[k] != s[j]:
                nexta.append(k)
            else:
                nexta.append(nexta[k])
        else:
            k = nexta[k]
    return nexta

def match(s, pattern):
    nextj = compute_next(pattern)
    if len(s) == 0 and len(pattern) == 0:
        return 0
    if len(pattern) == 0:
        return 0
    j = 0
    k = 0
    while j < len(s) and k < len(pattern):
        if k == -1 or s[j] == pattern[k]:
            k = k + 1
            j = j + 1
        else:
            k = nextj[k]
    if k == len(pattern):
        return j - k
    else:
        return -1

if __name__ == '__main__':
    print(match("abcdefgabcdbcf", "def"))
    print(match("abcdefgabcdbcf", "aaa"))
    print(match("abcdefgabcdbcf", "abcdefgabcdbcf"))
    print(match("abcdefgabcdbcf", "aaaaaaaaaa"))
    print(match("abcdefgabcdbcf", "cf"))
    print(match("abcdefgabcdbcf", "gab"))
