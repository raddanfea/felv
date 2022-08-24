a = 1
b = 2
x = 1
y = 2

n = "(a + b + (x - y))"

left = 0
right = 0

for l in n:
    if l == '(':
        left += 1
    elif l == ')':
        right += 1

print(left == right)
print((a + b + (x - y)))
