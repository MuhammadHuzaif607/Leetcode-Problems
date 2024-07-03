from collections import Counter
s = "anagram"
t = "nagaram"
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
    print(char_count_dict)   
    return True

print(isAnagram(s,t))
