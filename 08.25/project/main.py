matrix = [0] * 8

for x in range(len(matrix)):
    matrix[x] = [(0, " ")] * 8


def display():
    for i, line in enumerate(matrix):
        for piece in line:
            player, piece_id = piece
            if player == 1:
                print(w_chess.get(piece_id, '　').center(3), end="")
            else:
                print(b_chess.get(piece_id, '　').center(3), end="")
        print(8 - i)
    chars = 'ａｂｃｄｅｆｇｈ'
    for each in chars:
        print(each.center(3), end='')
    print()


order = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']

#       player id, piece id
piece = (0, 0)


def start_pos():
    for i in range(len(order)):
        matrix[0][i] = (2, order[i])
        matrix[1][i] = (2, 'pawn')
        matrix[7][i] = (1, order[i])
        matrix[6][i] = (1, 'pawn')


letters = 'abcdefgh'

b_chess = {
    'king': '♔',
    'queen': '♕',
    'rook': '♖',
    'bishop': '♗',
    'knight': '♘',
    'pawn': '♙'
}
w_chess = {
    'king': '♚',
    'queen': '♛',
    'rook': '♜',
    'bishop': '♝',
    'knight': '♞',
    'pawn': '♟'
}


# checks if it would be a valid move  without considering other pieces in the way
# return True or False by default
# SPECIAL CASES:
# pawn takeover move returns TAKEOVER
def check_valid_move(chosen_piece, current_player, from_location, target_location):
    f_l_location = letters.find(from_location[0])
    t_l_location = letters.find(target_location[0])
    from_location_line = int(from_location[1])
    target_location_line = int(target_location[1])
    match chosen_piece:
        case 'pawn':
            if current_player == 1:
                if target_location_line == from_location_line + 1 and abs(f_l_location - t_l_location) == 1:
                    return "TAKEOVER"
                elif from_location_line == 2:
                    if target_location_line in (2, 3) and target_location[0] == from_location[0]:
                        return True
                else:
                    if target_location_line == from_location_line - 1 and target_location[0] == from_location[0]:
                        return True
            else:
                if target_location_line == from_location_line - 1 and abs(f_l_location - t_l_location) == 1:
                    return "TAKEOVER"
                elif from_location_line == 7:
                    if target_location_line in (6, 5) and target_location[0] == from_location[0]:
                        return True
                else:
                    if target_location_line == from_location_line + 1 and target_location[0] == from_location[0]:
                        return True
            return False
        case 'knight':
            pass
        case 'bishop':
            pass
        case 'rook':
            pass
        case 'queen':
            pass
        case 'king':
            pass


def main():
    current_player = 1
    start_pos()

    while True:
        print(f"Current player: {'white' if current_player == 1 else 'black'}")

        display()
        global letters
        while True:
            from_location = input('Choose piece to move:  ')

            if from_location[0] in letters and 0 < int(from_location[1]) < 9 and len(from_location) == 2:
                l_index = letters.find(from_location[0])
                if matrix[8 - int(from_location[1])][l_index][0] == current_player:
                    chosen_piece = matrix[8 - int(from_location[1])][l_index][1]
                    break

        while True:
            target_location = input('Where to move piece:  ')
            letters = 'abcdefgh'
            if target_location[0] in letters and 0 < int(target_location[1]) < 9 and len(target_location) == 2:
                l_index = letters.find(target_location[0])
                is_occupied = matrix[8 - int(target_location[1])][l_index][0]
                what_is_there = matrix[8 - int(target_location[1])][l_index][1]
                v = check_valid_move(chosen_piece, current_player, from_location, target_location)
                print(v)
                if v: break

        print(from_location, '>', target_location, matrix[8 - int(from_location[1])][l_index][1])

        current_player = int(not bool(current_player - 1)) + 1


if __name__ == '__main__':
    main()
