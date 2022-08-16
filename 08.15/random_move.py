import random

player = '■'
obstacle = '▲'
empty_stace = 'O'


def display():
    for i in range(len(l)):
        if i % n == 0:
            print()
        print(l[i], end="\t")
    print()


def move(direction):
    pos = l.index(player)
    if direction in ['8', 'w'] and pos > n - 1:
        if l[pos - n] is obstacle:
            l[pos], l[((n - 1) * n)] = empty_stace, player
        else:
            l[pos], l[pos - n] = empty_stace, player
    elif direction in ['2', 's'] and ((n - 1) * n) > pos:
        if l[pos + n] is obstacle:
            l[pos], l[((n - 1) * n)] = empty_stace, player
        else:
            l[pos], l[pos + n] = empty_stace, player
    elif direction in ['4', 'a'] and not pos % n == 0:
        if l[pos - 1] is obstacle:
            l[pos], l[((n - 1) * n)] = empty_stace, player
        else:
            l[pos], l[pos - 1] = empty_stace, player
    elif direction in ['6', 'd'] and not pos % n == n - 1:
        if l[pos + 1] is obstacle:
            l[pos], l[((n - 1) * n)] = empty_stace, player
        else:
            l[pos], l[pos + 1] = empty_stace, player
    if l[pos] == n*n:
        return True
    return False


def game():
    global l, n
    n = random.randint(3, 6)
    l = [empty_stace] * (n ** 2)
    l[((n - 1) * n)] = player
    gen_obstacles()


def gen_obstacles():
    obsticles_placed = 0
    for each in range(n * n):
        if l[each] is not player and random.random() > 0.7:
            l[each] = obstacle
            obsticles_placed += 1
        if obsticles_placed == n:
            break


game()
while True:
    display()
    inp = str(input("Where?"))
    result = move(inp)
    if result:
        print("WIN")