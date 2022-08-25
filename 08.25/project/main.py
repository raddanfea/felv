matrix = [0] * 8

for x in range(len(matrix)):
    matrix[x] = [(0, " ")] * 8


def display():
    for i, line in enumerate(matrix):
        for piece in line:
            player, piece_id = piece
            if player == 1:
                print(w_chess.get(piece_id, '　').center(2), end="")
            else:
                print(b_chess.get(piece_id, '　').center(2), end="")
        print(8 - i)
    chars = 'ａｂｃｄｅｆｇｈ'
    for each in chars:
        print(each.center(2), end='')
    print()

empty_location = " "
chess_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
taken = []


# player id, piece id
piece = (0, 0)


def start_pos():
    for i in range(len(chess_pieces)):
        matrix[0][i] = (2, chess_pieces[i])
        matrix[1][i] = (2, 'pawn')
        matrix[7][i] = (1, chess_pieces[i])
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
# returns True or False except in special cases:
# pawn takeover move returns 'TAKEOVER'
def check_valid_move(chosen_piece, current_player, from_location, target_location):
    from_horizontal_location = letters.find(from_location[0])
    target_horizontal_location = letters.find(target_location[0])
    from_vertical_location = int(from_location[1])
    target_vertical_location = int(target_location[1])
    match chosen_piece:
        case 'pawn':
            if current_player == 1:
                if target_vertical_location == from_vertical_location + 1 and abs(from_horizontal_location - target_horizontal_location) == 1:
                    return "TAKEOVER"
                elif from_vertical_location == 2:
                    if target_vertical_location in (2, 3) and target_location[0] == from_location[0]:
                        return True
                elif target_vertical_location == from_vertical_location + 1 and target_location[0] == from_location[0]:
                        return True
            else:
                if target_vertical_location == from_vertical_location - 1 and abs(from_horizontal_location - target_horizontal_location) == 1:
                    return "TAKEOVER"
                elif from_vertical_location == 7:
                    if target_vertical_location in (6, 5) and target_location[0] == from_location[0]:
                        return True
                else:
                    if target_vertical_location == from_vertical_location - 1 and target_location[0] == from_location[0]:
                        return True
            return False
        case 'knight':
            lateral = abs(from_horizontal_location - target_horizontal_location)
            vertical = abs(from_vertical_location - target_vertical_location)
            print(lateral, vertical)
            if lateral == 1 and vertical == 2:
                return True
            elif vertical == 1 and lateral == 2:
                return True
            return False
        case 'bishop':
            if abs(from_horizontal_location - target_horizontal_location) == abs(from_vertical_location - target_vertical_location):
                return True
            return False
        case 'rook':
            if from_vertical_location != target_vertical_location and from_horizontal_location == target_horizontal_location:
                return True
            elif from_horizontal_location != target_horizontal_location and from_vertical_location == target_vertical_location:
                return True
            return False
        case 'queen':
            if abs(from_horizontal_location - target_horizontal_location) == abs(from_vertical_location - target_vertical_location):
                return True
            elif from_vertical_location != target_vertical_location and from_horizontal_location == target_horizontal_location:
                return True
            elif from_horizontal_location != target_horizontal_location and from_vertical_location == target_vertical_location:
                return True
            return False
        case 'king':
            if abs(from_vertical_location - target_vertical_location) == 1 and from_horizontal_location == target_horizontal_location:
                return True
            elif abs(from_horizontal_location - target_horizontal_location) == 1 and from_vertical_location == target_vertical_location:
                return True
            return False


def main():
    current_player = 1
    start_pos()

    while True:
        print(f"Current player: {'white' if current_player == 1 else 'black'}")

        display()
        global letters

        # current player's piece
        while True:
            from_location = input('Choose piece to move:  ')
            if from_location[0] in letters and 0 < int(from_location[1]) < 9 and len(from_location) == 2:
                l_index = letters.find(from_location[0])
                if matrix[8 - int(from_location[1])][l_index][0] == current_player:
                    chosen_piece = matrix[8 - int(from_location[1])][l_index][1]
                    break

        # target location
        while True:
            target_location = input('Where to move piece:  ')
            if target_location[0] in letters and 0 < int(target_location[1]) < 9 and len(target_location) == 2:
                l_index = letters.find(target_location[0])
                is_occupied = matrix[8 - int(target_location[1])][l_index][0]
                what_is_there = matrix[8 - int(target_location[1])][l_index][1]
                valid = check_valid_move(chosen_piece, current_player, from_location, target_location)
                if valid: break

        if valid:
            if what_is_there in chess_pieces:
                taken.append(what_is_there)
            matrix[8 - int(target_location[1])][l_index] = (current_player, chosen_piece)
            matrix[8 - int(from_location[1])][l_index] = (0, empty_location)

        print(from_location, '>', target_location, chosen_piece)

        current_player = int(not bool(current_player - 1)) + 1


if __name__ == '__main__':
    main()
