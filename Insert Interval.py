

def insertInterval(intervals,newInterval):
    if not intervals:
        return [newInterval]
    
    start = newInterval[0]
    end = newInterval[-1]
    merged = Falsegit add .
    
    if start != end:
        for index in range(len(intervals)):
            currentstart = intervals[index][0]
            currentend = intervals[index][-1]
            if start <= currentend and end <= currentend:
                intervals[index] = [min(start,currentstart),max(end,currentend)]
                merged = True
                break
            
        
    if not merged:
        intervals.append(newInterval)
        
    sorted_intervals  = sorted(intervals,key=lambda x: x[0])
    mergedIntervals = [sorted_intervals[0]]
    sorted_intervals = sorted_intervals[1:]
    for interval in sorted_intervals:
        if interval[0] <= mergedIntervals[-1][-1]:
            mergedIntervals[-1][-1] = max(interval[-1],mergedIntervals[-1][-1])
        else:
            mergedIntervals.append(interval)
            
    print(merged)
    
    return mergedIntervals  
    
        
        
    


intervals = []
newInterval = [5,7]
print(insertInterval(intervals,newInterval))
        
        