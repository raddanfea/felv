# rules
# if people step on you, you return to start
# dice 1-3
# too many steps = stay
import random

length = 9
empty = " "
positions = [empty] * length
players = {
    1: "■",
    2: "▲"
}
player = True

ui_hardcoded_dict = [
    (1, 3),
    (1, 5),
    (3, 5),
    (5, 5),
    (5, 3),
    (5, 1),
    (3, 1),
    (1, 1),
    (3, 3),
]


def print_ui(positions):
    size = 7
    matr = []
    for i in range(size):
        matr.append([0] * size)

    for i in range(size):
        matr[i] = ["."] * size

    for each in range(length):
        x, y = ui_hardcoded_dict[each]
        matr[y][x] = positions[each]

    print(f"Current Player: {players[int(player + 1)]}".center(27))
    print(f" {'-' * 25} ")
    for row, line in enumerate(matr):
        for col, item in enumerate(line):
            if row == 3 and col == 1 and item == ' ':
                print(str("STRT").center(4), end='')
            elif row == 3 and col == 3 and item == ' ':
                print(str("HOME").center(4), end='')
            else:
                print(str(item).center(4), end="")

        print("")
    print(f" {'-' * 25} ")


def move_to_new_pos(x, current_player, pos=0):
    if positions[pos + x] != empty:
        positions[0] = players[int((not player) + 1)]
    positions[pos + x] = players[current_player]


def play_game():
    global player

    while True:
        x = random.randint(1, 3)

        input("Press ENTER for next round.")

        current_player = int(player + 1)

        if players[current_player] not in positions:
            move_to_new_pos(x, current_player)
        else:
            pos = positions.index(players[current_player])
            if pos + x == length - 1:
                positions[pos] = empty
                positions[pos + x] = players[current_player]
                print_ui(positions)
                winner = players[current_player]
                break
            elif not pos + x > length - 1:
                positions[pos] = empty
                move_to_new_pos(x, current_player, pos)

        print_ui(positions)
        player = not player

    print(str(f"WINNER:  {winner}").center(27))


if __name__ == '__main__':
    while True:
        play_game()
        response = input("Would you like to play a new game? \nType q to quit.")
        if str(response).lower() == 'q':
            break

