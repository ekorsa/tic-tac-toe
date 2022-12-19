# field contain data like x + 3*y
CONTROL_LIST = (0, 1, 2)


def draw_field(f):
    print(f"  0 1 2")
    print(f"0 {f[0 + 3 * 0]} {f[1 + 3 * 0]} {f[2 + 3 * 0]}")
    print(f"1 {f[0 + 3 * 1]} {f[1 + 3 * 1]} {f[2 + 3 * 1]}")
    print(f"2 {f[0 + 3 * 2]} {f[1 + 3 * 2]} {f[2 + 3 * 2]}")


def do_move(f, a):
    while True:
        ask_move = input(f"Please enter coordinate for {a}, where format for X=1 and Y=2 should be like 12: ")
        if all([ask_move.isdigit(),
                len(ask_move) == 2,
                int(ask_move[0]) in CONTROL_LIST,
                int(ask_move[1]) in CONTROL_LIST]):
            coordinate = int(ask_move[0]) + 3 * int(ask_move[1])
            if f[coordinate] == '-':
                return coordinate
            else:
                print(f"That move already done by {f[coordinate]}, please choose another move.")
                continue
        else:
            print(f"Coordinates should be in format like 12. "
                  f"Possibly values for X and Y should be in range {CONTROL_LIST}")
            continue


def check_winner(f, a):
    if any([f[0] == f[1] == f[2] == a,
            f[3] == f[4] == f[5] == a,
            f[6] == f[7] == f[8] == a,
            f[0] == f[3] == f[6] == a,
            f[1] == f[4] == f[7] == a,
            f[2] == f[5] == f[8] == a,
            f[0] == f[4] == f[8] == a,
            f[2] == f[4] == f[6] == a]):
        return True
    else:
        return False


print("Welcome to tic tac toe game. New round.")
count_rounds = 1
while True:
    field = ['-' for i in range(9)]
    print(draw_field(field))
    for i in range(1, 10):
        print(f"There is {i} move.")
        current_player = 'X' if i % 2 else 'Y'
        cord = do_move(field, current_player)
        field[cord] = current_player
        print(draw_field(field))
        if i > 3 and check_winner(field, current_player):
            print(f"Winner is player {current_player}!")
            break
        elif i == 9:
            print("No winner in this round.")
    ask_next_round = input("Do you want to play one more round? 'Y' or 'y' for next round: ")
    if not ask_next_round.lower() == 'y':
        break
    count_rounds += 1
    print(f"{count_rounds} round.")
