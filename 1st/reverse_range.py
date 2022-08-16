n = 9

reverse = reversed(range(1, n+1))
output = []
last = n//2+1
for i in range(1, last+1):
    rev = next(reverse)
    if i == last:
        if str(rev) not in output:
            output.append(str(rev))
    else:
        output.append(str(rev))
        output.append(str(i))

print(" ".join(output))