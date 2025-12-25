
strs = ["flower","flow","flight"]
strs = sorted(strs, key=len)

c_string = ""
for i in range(len(strs[0])):
    char = strs[0][i]
    for s in strs[1:]:
        if char != s[i]:
            print(c_string)
            exit()
    c_string += char

print(c_string)

