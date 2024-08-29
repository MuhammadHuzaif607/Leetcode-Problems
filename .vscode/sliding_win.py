arr = [100, 200, 300, 400] 
k = 2
window_sum = sum(arr[:k])
for i in range(len(arr) - k ):
    curr_sum = window_sum - arr[i] + arr[i+k]
    window_sum = max(window_sum,curr_sum)

print(window_sum)