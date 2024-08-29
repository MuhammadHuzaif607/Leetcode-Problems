s = "bbbb"
# i = 0
# j = 0
# set_strs = set()
# length = 0
# while i < len(s):
#     set1 = set()
#     for j in range(i,len(s)):
#         if s[j] not in set1:
#             set1.add(s[j])
#             set_strs.add(s[i:j+1])
#             if len(s[i:j+1]) > length:
#                 length = len(s[i:j+1])

#         else:
#             break

#     i += 1

# print(length)

chars = {}
max_len = 0
curr_len = 0
for index in range(len(s)):
    if s[index] in chars:
        chars = {}
        curr_len = 1
        chars[s[index]] = index
    else:
        chars[s[index]] = index
        curr_len += 1
        if curr_len > max_len:
            max_len = curr_len

    print(chars,curr_len,max_len)

print(max_len)

        










