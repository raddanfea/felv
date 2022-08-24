
def get_priority(c):
    if c in "+-":
        return 1
    elif c in "*/":
        return 2
    elif c == '^':
        return 3
    return 0


def move(prefix_stack, operator_stack):
    op_last = prefix_stack.pop()
    op_2nd_last = prefix_stack.pop()
    op = operator_stack.pop()
    prefix_stack.append(op + op_2nd_last + op_last)


def is_operator(c):
    return not c.isalpha()


def infix_to_prefix(infix):
    operator_stack = []
    prefix_stack = []

    for i in range(len(infix)):
        if infix[i] == '(':
            operator_stack.append(infix[i])
        elif infix[i] == ')':
            while len(operator_stack) != 0 and operator_stack[-1] != '(':
                move(prefix_stack, operator_stack)
            operator_stack.pop()
        elif not is_operator(infix[i]):
            prefix_stack.append(infix[i] + "")
        else:
            while len(operator_stack) != 0 and get_priority(infix[i]) <= get_priority(operator_stack[-1]):
                move(prefix_stack, operator_stack)
            operator_stack.append(infix[i])
    while len(operator_stack) != 0:
        move(prefix_stack, operator_stack)
    return prefix_stack[-1]


s = "(a+(b-c+d)/e*f^g-(h/i-(j-(k*l)*m)^n)+p)"
print(infix_to_prefix(s))


