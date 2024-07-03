s = "paper"
t = "title"
def isIsomorphic(s,t):
    dict1 = {}
    str1 = ''
    for el in range(len(s)):
        if t[el] in str1:
            pass
        else:
            dict1[s[el]] = t[el]
            str1 += t[el]
        
    ns = ''
   
    for el in s:
        if el in dict1 :
            ns += dict1[el]


    if ns == t:
        return True
    return False


print(isIsomorphic(s,t))