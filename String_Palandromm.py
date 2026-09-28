def pal(word, index):
    print(word[index], word[len(word)-index - 1])
    if index >= len(word) / 2:
        return True
    if word[index] == word[len(word)-index -1]:
        return pal(word, index+1)
    return False






x = "madama"
res = pal(x,0)
print(res)