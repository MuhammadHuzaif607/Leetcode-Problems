def mergeIntervals(intervals):
    sorted_intervals  = sorted(intervals,key=lambda x: x[0])
    mergedIntervals = [sorted_intervals[0]]
    sorted_intervals = sorted_intervals[1:]
    for interval in sorted_intervals:
        if interval[0] <= mergedIntervals[-1][-1]:
            mergedIntervals[-1][-1] = max(interval[-1],mergedIntervals[-1][-1])
        else:
            mergedIntervals.append(interval)
    
    return mergedIntervals        

intervals = [[1,4],[2,3]]
print(mergeIntervals(intervals))