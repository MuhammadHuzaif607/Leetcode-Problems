strs = ["dog","racecar","car"]
def longestCommonPrefix(strs):
    best = ''
    for index in range(len(min(strs))):
        curr = strs[0][index]
        i = 0
        while i < len(strs):
            if curr != strs[i][index]:
                return best
            i += 1

        best += curr

    return best

print(longestCommonPrefix(strs))

        
    