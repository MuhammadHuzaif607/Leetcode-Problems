from collections import Counter
strs = ['eat','tea','ate','tan','nat','bat','tab']
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    char_count = Counter(s)
    char_count_dict = dict(char_count)
    for word in t:
        try:
            if char_count_dict[word] != 0:
                char_count_dict[word] -= 1
            else:
                return False
        except KeyError:
            return False   
    return True

def groupAnagrams(strs):
    # i = 0
    # out_arr = []
    # while i < len(strs):
    #     j = i + 1
    #     arr = []
    #     while j < len(strs):
    #         isValid = isAnagram(strs[i],strs[j])
    #         if isValid:
    #             arr.append(strs[j])
    #             strs.pop(j)
    #         else:
    #             j += 1

    #     arr.append(strs[i])
    #     out_arr.append(arr)
    #     i += 1

    # return out_arr
    res = dict()
    for word in strs:
        count = [0] * 26
        for c in word:
            count[ord(c) - ord('a')] += 1

        if tuple(count) in res:
            res[tuple(count)].append(word)
        else:
            res[tuple(count)] = []
            res[tuple(count)].append(word)
        
        

    return list(res.values())


print(groupAnagrams(strs))

        







    