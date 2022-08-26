
letters = 'abcdefgh'
# checks if it would be a valid move  without considering other pieces in the way
# returns True or False except in special cases:
# pawn takeover move returns 'TAKEOVER'
def check_valid_move(chosen_piece, current_player, from_location, target_location, matrix):
    from_horizontal_location = letters.find(from_location[0])
    target_horizontal_location = letters.find(target_location[0])
    from_vertical_location = int(from_location[1])
    target_vertical_location = int(target_location[1])
    match chosen_piece:
        # pawn move up or down, vertical if TAKING
        case 'pawn':
            if current_player == 1:
                if target_vertical_location == from_vertical_location + 1 \
                        and abs(from_horizontal_location - target_horizontal_location) == 1 \
                        and matrix[8 - target_vertical_location][target_horizontal_location][0] not in [0,
                                                                                                        current_player]:
                    return "TAKEOVER"
                elif from_vertical_location == 2:
                    if target_vertical_location in (3, 4) \
                            and target_horizontal_location == from_horizontal_location \
                            and matrix[8 - target_vertical_location][target_horizontal_location][0] == 0:
                        return True
                elif target_vertical_location == from_vertical_location + 1 \
                        and target_horizontal_location == from_horizontal_location \
                        and matrix[8 - target_vertical_location][target_horizontal_location][0] == 0:
                    return True
            else:
                if target_vertical_location == from_vertical_location - 1 and abs(
                        from_horizontal_location - target_horizontal_location) == 1 \
                        and matrix[8 - target_vertical_location][target_horizontal_location][0] not in [0,
                                                                                                        current_player]:
                    return "TAKEOVER"
                elif from_vertical_location == 7:
                    if target_vertical_location in (6, 5) \
                            and target_horizontal_location == from_horizontal_location \
                            and matrix[8 - target_vertical_location][target_horizontal_location][0] == 0:
                        return True
                else:
                    if target_vertical_location == from_vertical_location - 1 \
                            and target_horizontal_location == from_vertical_location \
                            and matrix[8 - target_vertical_location][target_horizontal_location][0] == 0:
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
            if abs(from_vertical_location - target_vertical_location) == 1 and from_horizontal_location == target_horizontal_location:
                return True
            elif abs(
                    from_horizontal_location - target_horizontal_location) == 1 and from_vertical_location == target_vertical_location:
                return True
            elif abs(from_horizontal_location - target_horizontal_location) == 1 and abs(
                    from_vertical_location - target_vertical_location) == 1:
                return True
            return False