
# 21/12/2025
n = str(input())

rev_n = []
for i in n:
    rev_n.insert(0, i)

pal_n = ""
for i in rev_n:
    pal_n += i

if (n == pal_n):
    print(True)
else:
    print(False)
