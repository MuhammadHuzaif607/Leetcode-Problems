nums = [0,1,2,4,5,7]
start = nums[0]
end = None
out_arr = []

for index in range(len(nums)-1):
   if nums[index] != (nums[index+ 1] -1):
      if end == None:
         out_arr.append(f'{start}')
         start = nums[index+1]
      else:
         out_arr.append(f'{start}->{end}')
         start = nums[index+1]
         end = None
   else:
      end = nums[index+1]
    
if end == None:
   out_arr.append(f'{start}')
else:
   out_arr.append(f'{start}->{end}')

print(out_arr)