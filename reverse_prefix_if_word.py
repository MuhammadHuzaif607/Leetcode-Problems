def reversePrefix(word, ch):
    ch_index = word.find(ch)
    if ch_index != -1:
        prefix_word = word[:ch_index+1][::-1] + word[ch_index+1:]
    else:
        return word
    return prefix_word
    
print(reversePrefix( "abcdefd",'d'))