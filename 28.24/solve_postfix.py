

s = "34*25*+"


def solve_prefix(s):
    stack = []
    s = [c for c in s]
    while s:
        item = s.pop(0)
        if item.isnumeric():
            stack.append(item)
        elif len(stack) > 1:
            stack[-2] = int(eval(f'{int(stack[-1])} {item} {int(stack[-2])}'))
            stack.pop()
        print(stack)
    return stack[0]

print(solve_prefix(s))