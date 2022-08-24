def isoperCheck(s):
    oper = "+-/^*"
    closingbrac = ")]}"
    valid = True
    for i in range(len(s)):
        if i + 1 < len(s):
            if (s[i] in oper) and (s[i + 1] in oper):
                valid = False
                break
            elif (s[i].isalpha() and s[i + 1].isalpha()):
                valid = False
                break
            elif s[-1] in oper:
                valid = False
                break
            elif (s[i] in closingbrac and s[i + 1].isalpha()):
                valid = False
                break
            elif (s[i] in oper and s[i + 1] in closingbrac):
                valid = False
                break
    return valid


s = input("Enter the string")
print(isoperCheck(s))
