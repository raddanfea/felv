letters = 'abcdefgh'


def check_collison(chosen_piece, current_player, from_location, target_location, matrix):
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
                            matrix[8 - from_vertical_location - int(i * vertical // abs(vertical))][
                                from_horizontal_location][
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
            elif abs(vertical) > 1:
                for i in range(1, abs(vertical)):
                    if \
                            matrix[8 - from_vertical_location - int(i * vertical // abs(vertical))][
                                from_horizontal_location][
                                0] != 0:
                        return False
            elif abs(horizontal) > 1:
                for i in range(1, abs(horizontal)):
                    if matrix[8 - from_vertical_location][
                        from_horizontal_location + int(i * horizontal // abs(horizontal))][0] != 0:
                        return False
            return True
    return True
