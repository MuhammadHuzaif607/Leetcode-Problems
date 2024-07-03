pattern = "abba"
s = "dog cat cat dog"
occured_words = []
        
def wordPattern(pattern, s):
    if len(s_list) != len(pattern):
        return False
    s_list = s.split(" ")
    dict1 = {}
    for el in  range(len(pattern)):
        if pattern[el] not in dict1:
            if s_list[el] not in  occured_words:
                dict1[pattern[el]] = s_list[el]
                occured_words.append(s_list[el])
            else:
                return False
        else:
            if dict1[pattern[el]] != s_list[el]:
                return False
            
    return True

print(wordPattern(pattern,s))
    