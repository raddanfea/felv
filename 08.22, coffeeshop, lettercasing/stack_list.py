max_stack = 7
stack = [0] * max_stack
top1 = 0
top2 = max_stack - 1


def push():
    global top1, top2, stack
    if top1-1==top2:
        print("Stack overflow")
    else:
        where = int(input("0 top, -1 bottom:  "))
        ele = int(input("Element: "))
        if where == 0:
            stack[top1] = ele
            top1 += 1
        else:
            stack[top2] = ele
            top2 -= 1
    print(stack)


def pop():
    global top1, top2, stack
    where = int(input("0 top, -1 bottom:  "))
    if where == 0:
        if top1 == 0:
            print("Underflow ")
        else:
            stack[0:top1-1] = stack[1:top1]
            stack[top1] = 0
    else:
        if top2 == max_stack:
            print("Underflow ")
        else:
            stack[top2:max_stack-1] = stack[top2+1:max_stack]
            stack[top2] = 0
    print(stack)


while True:
    i = input("Menu: 0 pop 1 push:    ")
    if i:
        push()
    else:
        pop()
