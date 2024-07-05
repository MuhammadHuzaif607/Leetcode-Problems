from collections import Counter
strs = ["eat","tea","tan","ate","nat","bat"]
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

def groupanagrams(strs):
    # lst = []
    # for index in range(len(strs)):
    #     if isAnagram(strs[index],strs[index + 1]):
    pass


    