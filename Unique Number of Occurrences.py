from collections import defaultdict
dict1 = defaultdict(int)
arr = [1,2,2,1,1,3]
arr1 = []
for el in arr:
     dict1[el] += 1
        
for el in dict1:
     if dict1[el] in arr1:
          print(False)
     arr1.append(dict1[el])