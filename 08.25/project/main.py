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


def check_collison(chosen_piece, current_player, from_location, target_location):
    from_horizontal_location = letters.find(from_location[0])
    target_horizontal_location = letters.find(target_location[0])
    from_vertical_location = int(from_location[1])
    target_vertical_location = int(target_location[1])
    match chosen_piece:
        case 'pawn':
            if current_player == 1:
                if from_vertical_location == 2:
                    if target_vertical_location == 4:
                        if matrix[8 - target_vertical_location][from_horizontal_location][0] != 0 \
                                or matrix[8 - from_vertical_location - 1][from_horizontal_location][0] != 0:
                            return False
                if target_vertical_location == from_vertical_location - 1:
                    if matrix[8 - from_vertical_location - 1][from_horizontal_location][0] != 0:
                        return False
            if current_player == 2:
                if from_vertical_location == 7:
                    if target_vertical_location == 5:
                        if matrix[8 - target_vertical_location][from_horizontal_location][0] != 0 \
                                and matrix[8 - from_vertical_location + 1][from_horizontal_location][0] != 0:
                            return False
                if target_vertical_location == from_vertical_location + 1:
                    if matrix[8 - from_vertical_location + 1][from_horizontal_location][0] != 0:
                        return False
            return True
        case 'bishop':
            vertical = target_vertical_location - from_vertical_location
            horizontal = target_horizontal_location - from_horizontal_location
            if abs(vertical) > 1:
                for i in range(1, abs(vertical)):
                    if matrix[8 - from_vertical_location - int(i * vertical // abs(vertical))][
                        from_horizontal_location + int(i * horizontal // abs(horizontal))][0] != 0:
                        return False
            return True
        case 'rook':
            vertical = target_vertical_location - from_vertical_location
            horizontal = target_horizontal_location - from_horizontal_location
            if abs(vertical) > 1:
                for i in range(1, abs(vertical)):
                    if \
                    matrix[8 - from_vertical_location - int(i * vertical // abs(vertical))][from_horizontal_location][
                        0] != 0:
                        return False
            elif abs(horizontal) > 1:
                print("h")
                for i in range(1, abs(horizontal)):
                    if matrix[8 - from_vertical_location][
                        from_horizontal_location + int(i * horizontal // abs(horizontal))][0] != 0:
                        return False
            return True
        case 'queen':
            vertical = target_vertical_location - from_vertical_location
            horizontal = target_horizontal_location - from_horizontal_location
            if abs(vertical) > 1 and abs(horizontal) > 1:
                for i in range(1, abs(vertical)):
                    if matrix[8 - from_vertical_location - int(i * vertical // abs(vertical))][
                        from_horizontal_location + int(i * horizontal // abs(horizontal))][0] != 0:
                        return False
            if abs(vertical) > 1:
                for i in range(1, abs(vertical)):
                    if \
                    matrix[8 - from_vertical_location - int(i * vertical // abs(vertical))][from_horizontal_location][
                        0] != 0:
                        return False
            elif abs(horizontal) > 1:
                print("h")
                for i in range(1, abs(horizontal)):
                    if matrix[8 - from_vertical_location][
                        from_horizontal_location + int(i * horizontal // abs(horizontal))][0] != 0:
                        return False
            return True


# checks if it would be a valid move  without considering other pieces in the way
# returns True or False except in special cases:
# pawn takeover move returns 'TAKEOVER'
def check_valid_move(chosen_piece, current_player, from_location, target_location):
    from_horizontal_location = letters.find(from_location[0])
    target_horizontal_location = letters.find(target_location[0])
    from_vertical_location = int(from_location[1])
    target_vertical_location = int(target_location[1])
    match chosen_piece:
        # pawn move up or down, vertical if TAKING
        case 'pawn':
            if current_player == 1:
                if target_vertical_location == from_vertical_location + 1 \
                        and abs(from_horizontal_location - target_horizontal_location) == 1:
                    return "TAKEOVER"
                elif from_vertical_location == 2:
                    if target_vertical_location in (3, 4) \
                            and target_horizontal_location == from_horizontal_location:
                        return True
                elif target_vertical_location == from_vertical_location + 1 \
                        and target_horizontal_location == from_horizontal_location:
                    return True
            else:
                if target_vertical_location == from_vertical_location - 1 and abs(
                        from_horizontal_location - target_horizontal_location) == 1:
                    return "TAKEOVER"
                elif from_vertical_location == 7:
                    if target_vertical_location in (6, 5) \
                            and target_horizontal_location == from_horizontal_location:
                        return True
                else:
                    if target_vertical_location == from_vertical_location - 1 \
                            and target_horizontal_location == from_vertical_location:
                        return True
            return False
        case 'knight':
            lateral = abs(from_horizontal_location - target_horizontal_location)
            vertical = abs(from_vertical_location - target_vertical_location)
            if lateral == 1 and vertical == 2:
                return True
            elif vertical == 1 and lateral == 2:
                return True
            return False
        # bishop
        # checks is if in diagonal line ex: (3, 3) to (4, 4)
        #                                   abs(3-4) = 1      abs(3-4) = 1
        #                                   1 = 1 so it is vertical
        case 'bishop':
            if abs(from_horizontal_location - target_horizontal_location) == abs(
                    from_vertical_location - target_vertical_location):
                return True
            return False
        # rook
        # checks is if in horizontal or vertical line ex:   (3, 3) to (3, 4)
        #                      x1 and x2 or y1 and y2 should be equal, both cannot be because that where we are
        case 'rook':
            if from_vertical_location != target_vertical_location and from_horizontal_location == target_horizontal_location:
                return True
            elif from_horizontal_location != target_horizontal_location and from_vertical_location == target_vertical_location:
                return True
            return False
        # queen is both bishop and rook at the same time
        case 'queen':
            if abs(from_horizontal_location - target_horizontal_location) == abs(
                    from_vertical_location - target_vertical_location):
                return True
            elif from_vertical_location != target_vertical_location and from_horizontal_location == target_horizontal_location:
                return True
            elif from_horizontal_location != target_horizontal_location and from_vertical_location == target_vertical_location:
                return True
            return False
        # king is checking neighbors
        case 'king':
            print(abs(from_horizontal_location - target_horizontal_location),
                  from_vertical_location == target_vertical_location)
            if abs(from_vertical_location - target_vertical_location) == 1 and from_horizontal_location == target_horizontal_location:
                return True
            elif abs(
                    from_horizontal_location - target_horizontal_location) == 1 and from_vertical_location == target_vertical_location:
                return True
            elif abs(from_horizontal_location - target_horizontal_location) == 1 \
                    and abs(from_vertical_location - target_vertical_location) == 1:
                return True
            return False


def main():
    current_player = 1
    start_pos()

    while True:
        print(f"Current player: {'white' if current_player == 1 else 'black'}")

        display()
        global letters
        from_location = None

        # current player's piece
        while not from_location:
            from_location = input('Choose piece to move:  ')
            if from_location[0] in letters and 0 < int(from_location[1]) < 9 and len(from_location) == 2:
                horizontal_index_original = letters.find(from_location[0])
                if matrix[8 - int(from_location[1])][horizontal_index_original][0] == current_player:
                    chosen_piece = matrix[8 - int(from_location[1])][horizontal_index_original][1]
                    break
            from_location = None

        # target location
        valid, what_is_there = False, False
        while True:
            target_location = input('Where to move piece:  ')
            if target_location \
                    and target_location[0] in letters \
                    and len(target_location) == 2 \
                    and 0 < int(target_location[1]) < 9:
                horizontal_index_target = letters.find(target_location[0])
                is_occupied = matrix[8 - int(target_location[1])][horizontal_index_target][0]
                if is_occupied == current_player: continue
                what_is_there = matrix[8 - int(target_location[1])][horizontal_index_target][1]
                valid = check_valid_move(chosen_piece, current_player, from_location, target_location)
                if valid: break

            if target_location == "back":
                from_location = None
                break
        if target_location == "back":
            continue

        # making ta move
        collison = check_collison(chosen_piece, current_player, from_location, target_location)

        if valid and collison:
            if what_is_there in chess_pieces:
                taken.append((int(not bool(current_player - 1)) + 1, what_is_there))
            matrix[8 - int(target_location[1])][horizontal_index_target] = (current_player, chosen_piece)
            matrix[8 - int(from_location[1])][horizontal_index_original] = (0, empty_location)

            print(from_location, '>', target_location, chosen_piece)

            # current_player = int(not bool(current_player - 1)) + 1
        else:
            print("Invalid move!")


if __name__ == '__main__':
    main()
