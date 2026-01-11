
# Solved this problem. 11/01/2026
digits = [9]
n = ""

for i in digits:
    n += str(i)

n = int(n)
n = n + 1
 
digits = []

for i in str(n):
    digits.append(int(i))

print(digits)