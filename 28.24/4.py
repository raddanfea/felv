def count_digits(number):
    if not number:
        return 0
    return count_digits(number // 10) + 1


# print(count_digits(88761))

vowels = 'aeiou'


def count_vowels(string):
    if string == '':
        return 0
    elif string[-1] in vowels:
        return count_vowels(string[:-1]) + 1
    else:
        return count_vowels(string[:-1])


s = "if you are happy       that u got the job    .....  i appreciate your innocence    "


# print(count_vowels(s)

def recursive_space_equilazerrr(s, i=0):
    if i == len(s):
        return ""
    if s[i] == " " and s[i - 1] == " ":
        return recursive_space_equilazerrr(s, i + 1)
    else:
        return str(s[i]) + str(recursive_space_equilazerrr(s, i + 1))


print(recursive_space_equilazerrr(s))
