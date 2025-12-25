
s = "()"

matching = {
    ')': '(',
    ']': '[',
    '}': '{'
}

stack = []

for char in s:
    if char in matching.values():
        stack.append(char)
    else:
        if not stack:
            print(False)

        top = stack.pop()
        if top != matching[char]:
            print(False)

print(not stack)


