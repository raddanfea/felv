from check_collison_file import check_collison
from check_valid_move_file import check_valid_move

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


def check_check(current_player):
    find_king = [-1, -1]
    for y, line in enumerate(matrix):
        for x, (player, pawn) in enumerate(line):
            if player == current_player and pawn == 'king':
                find_king = (x, y)
    # check for rooks
    for i in range(1, 8):
        try:
            if matrix[find_king[1] + i][find_king[0]][0] == current_player:
                break
            elif matrix[find_king[1] + i][find_king[0]][0] not in (0, current_player) and \
                    matrix[find_king[1] + i][find_king[0]][1] in ('rook', 'queen'):
                return 'rook'
        except IndexError:
            break
    for i in range(1, 8):
        try:
            if find_king[1] - i < 0: break
            if matrix[find_king[1] - i][find_king[0]][0] == current_player:
                break
            elif matrix[find_king[1] - i][find_king[0]][0] not in (0, current_player) and \
                    matrix[find_king[1] - i][find_king[0]][1] in ('rook', 'queen'):
                return 'rook'
        except IndexError:
            break
    for i in range(1, 8):
        try:
            if matrix[find_king[1]][find_king[0] + i][0] == current_player:
                break
            elif matrix[find_king[1]][find_king[0] + i][0] not in (0, current_player) and \
                    matrix[find_king[1]][find_king[0] + i][1] in ('rook', 'queen'):
                return 'rook'
        except IndexError:
            break
    for i in range(1, 8):
        try:
            if find_king[0] - i < 0: break
            if matrix[find_king[1]][find_king[0] - i][0] == current_player:
                break
            elif matrix[find_king[1]][find_king[0] - i][0] not in (0, current_player) and \
                    matrix[find_king[1]][find_king[0] - i][1] in ('rook', 'queen'):
                return 'rook'
        except IndexError:
            break
    # check for bishops
    for i in range(1, 8):
        try:
            if find_king[0] - i < 0: break
            if matrix[find_king[1] + i][find_king[0] - i][0] == current_player:
                break
            elif matrix[find_king[1] + i][find_king[0] - i][0] not in (0, current_player) and \
                    matrix[find_king[1] + i][find_king[0] - i][1] in ('rook', 'queen'):
                return 'bishop'
        except IndexError:
            break
    for i in range(1, 8):
        try:
            if find_king[1] - i < 0: break
            if matrix[find_king[1] - i][find_king[0] + i][0] == current_player:
                break
            elif matrix[find_king[1] - i][find_king[0] + i][0] not in (0, current_player) and \
                    matrix[find_king[1] - i][find_king[0] + i][1] in ('rook', 'queen'):
                return 'bishop'
        except IndexError:
            break
    for i in range(1, 8):
        try:
            if matrix[find_king[1] + i][find_king[0] + i][0] == current_player:
                break
            elif matrix[find_king[1] + i][find_king[0] + i][0] not in (0, current_player) and \
                    matrix[find_king[1] + i][find_king[0] + i][1] in ('rook', 'queen'):
                return 'bishop'
        except IndexError:
            break
    for i in range(1, 8):
        try:
            if find_king[1] - i < 0 or find_king[0] - i < 0: break
            if matrix[find_king[1] - i][find_king[0] - i][0] == current_player:
                break
            elif matrix[find_king[1] - i][find_king[0] - i][0] not in (0, current_player) and \
                    matrix[find_king[1] - i][find_king[0] - i][1] in ('rook', 'queen'):
                return 'bishop'
        except IndexError:
            break
    # check for knights
    positions = (1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)
    for x, y in positions:
        try:
            if matrix[find_king[1] + x][find_king[0] - y][0] not in (0, current_player) and \
                    matrix[find_king[1] - x][find_king[0] - y][1] == 'knight':
                return 'knight'
        except IndexError:
            continue
    # check for pawns
    if current_player:
        if matrix[find_king[1] - 1][find_king[0] - 1][0] not in (0, current_player) and \
                matrix[find_king[1] - 1][find_king[0] - 1][1] == 'pawn':
            pass
    return False


def swap_to_queen_if_pawn_at_right_position():
    pass


def main():
    current_player = 1
    start_pos()
    while True:
        display()
        print(f"Current player: {'White' if current_player == 1 else 'Black'}")
        global letters
        from_location = None

        # check if king is in check
        print("Check: ", check_check(current_player))
        chosen_piece = ""
        # current player's piece
        while not from_location:
            from_location = input('Choose piece to move:  ')

            # DEBUG: destroy a piece eg. kd1 destroys d1
            if from_location[0] == 'k' and False:
                matrix[8 - int(from_location[2])][letters.find(from_location[1])] = (0, empty_location)
                from_location = None
                break

            if from_location[0] in letters and 0 < int(from_location[1]) < 9 and len(from_location) == 2:
                horizontal_index_original = letters.find(from_location[0])
                if matrix[8 - int(from_location[1])][horizontal_index_original][0] == current_player:
                    chosen_piece = matrix[8 - int(from_location[1])][horizontal_index_original][1]
                    break
                else:
                    from_location = None

        # target location
        valid, what_is_there = False, False
        while from_location:
            target_location = input('Where to move piece:  ')
            if target_location \
                    and target_location[0] in letters \
                    and len(target_location) == 2 \
                    and 0 < int(target_location[1]) < 9:
                # index of letter
                horizontal_index_target = letters.find(target_location[0])
                # id of occupier
                is_occupied = matrix[8 - int(target_location[1])][horizontal_index_target][0]
                # checks if target is the current player, if yes asks again
                if is_occupied == current_player: continue
                # type of piece at target
                what_is_there = matrix[8 - int(target_location[1])][horizontal_index_target][1]
                # check is if  the move is valid type
                valid = check_valid_move(chosen_piece, current_player, from_location, target_location, matrix)
                if valid: break
            # reset from location if typed back
            if target_location == "back":
                from_location = None
                break
        # return to the start of the iteration if typed back
        if not from_location or target_location == "back":
            continue

        # making ta move
        collison = check_collison(chosen_piece, current_player, from_location, target_location, matrix)

        if valid and collison:
            if what_is_there in chess_pieces:
                taken.append((int(not bool(current_player - 1)) + 1, what_is_there))
            matrix[8 - int(target_location[1])][horizontal_index_target] = (current_player, chosen_piece)
            matrix[8 - int(from_location[1])][horizontal_index_original] = (0, empty_location)

            swap_to_queen_if_pawn_at_right_position()

            print(from_location, '>', target_location, chosen_piece)

            # swaps players
            # current_player = int(not bool(current_player - 1)) + 1
        else:
            print("Invalid move!")


if __name__ == '__main__':
    main()
