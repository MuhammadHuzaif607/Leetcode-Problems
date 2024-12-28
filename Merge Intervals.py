intervals = [[1,4],[5,6]]
start = intervals[0][0]
end = intervals[0][1]
merged = []
for interval in intervals[1:]:
    if end - interval[0] >= 0:
        merged.append([start,interval[1]])
        end = interval[1]
    else:
        merged.append([interval[0],interval[1]])
        
print(merged)
    