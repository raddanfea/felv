def get_priority(c):
    if c in "+-":
        return 1
    elif c in "*/":
        return 2
    elif c == '^':
        return 3
    return 0


def to_postfix(infix):
    stack = []
    postfix = ''

    for c in infix:
        if c.isalpha():
            postfix += c
        else:
            if c == '(':
                stack.append(c)
            elif c == ')':
                operator = stack.pop()
                while not c == '(' and stack and operator != '(':
                    postfix += operator
                    operator = stack.pop()
            else:
                while stack and get_priority(c) <= get_priority(stack[-1]):
                    postfix += stack.pop()
                stack.append(c)

    return postfix + str(*list(reversed(stack)))


print(to_postfix("K+L-M*N+(O^P)*W/U/V*T+Q"))
