

n = 5
flip_bool = True

temp = n
while True:
    print(temp, end=" ")
    if flip_bool:
        temp -= 1
    else:
        temp += 1

    if temp == 1:
        flip_bool = False
    if temp == n+1:
        break
