ransomNote = 'aab'
magazine = 'baa'

def canConstruct(ransomNote,magazine):
    dict1 = {
    }
    for el in magazine:
        if el in dict1:
            dict1[el] += 1
        else:
            dict1[el] = 1

    for el in ransomNote:
        if el in dict1:
            dict1[el] -= 1
            if dict1[el] == 0:
                dict1.pop(el)
        else:
            return False
        
    return True

print(canConstruct(ransomNote,magazine))
        
        