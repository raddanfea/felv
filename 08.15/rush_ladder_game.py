import random
import sys

to_char = {
    0: ".",
    1: '■',
    2: '▲',
    3: '■▲',
    4: "?",
    5: "="
}

player1 = 1
player2 = 2
target = 4
players = player1, player2
current_player = 1
other_player = 2
obstacle = 5
empty_stace = 0
a_posm, b_pos = 0, 0
points = [0, 0]


def display():
    for i in range(len(l)):
        if i % n == 0:
            print()
        print(str(to_char[l[i]]), end="\t")
    print()


def check_player(new_p, pos):
    if 0 <= new_p < len(l):
        if l[new_p] == target:
            l[pos] -= current_player
            l[new_p] = current_player
            display()
            print(f'{to_char[player1]} Player 1: {points[0]} points \n{to_char[player2]} Player 2: {points[1]} points')
            sys.exit()
        elif l[new_p] is not obstacle:
            l[pos] -= current_player
            if l[new_p] > 0:
                if l[0] not in [other_player, 3]:
                    l[0] += other_player
                points[(current_player - 1)] += 1
            l[new_p] = current_player
        else:
            l[pos] -= current_player
            l[0] += current_player
    return False


def move(direction, distance):
    global current_player, other_player
    try:
        pos = l.index(current_player)
    except:
        try:
            pos = l.index(3)
        except:
            l[0] = 3
            return 0

    other_player = int(not current_player - 1) + 1

    if direction in ['8', 'w'] and pos > n - 1:
        check_player(pos - n*distance, pos)
    elif direction in ['2', 's'] and ((n - 1) * n) > pos:
        check_player(pos + n*distance, pos)
    elif direction in ['4', 'a'] and not pos % n == 0:
        check_player(pos - 1*distance, pos)
    elif direction in ['6', 'd'] and not pos % n == n - 1:
        check_player(pos + 1*distance, pos)

    if l[pos] == n * n:
        return True

    if current_player == 1:
        current_player = 2
    else:
        current_player = 1

    return False


def game():
    global l, n
    n = 7
    l = [empty_stace] * (n ** 2)
    l[0] = 3
    l[-1] = target
    for i in [4, 5, 6, 15, 14, 16, 19, 20, 28, 31, 32, 33, 34, 42, 43, 44]:
        l[i] = obstacle
    # gen_obstacles()


game()
while True:
    display()
    inp = random.choice(['w', "s", "a", "d"])
    mch = random.randint(1, 6)
    print(f'Player: {to_char[current_player]} Direction: {inp}, Dice: {mch}')
    result = move(inp, mch)
