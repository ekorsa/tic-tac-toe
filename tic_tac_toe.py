# field contain data like x + 3*y


CONTROL_LIST = (0, 1, 2)
def draw_field():
    print(f"  0 1 2")
    print(f"0 {field[0 + 3 * 0]} {field[1 + 3 * 0]} {field[2 + 3 * 0]}")
    print(f"1 {field[0 + 3 * 1]} {field[1 + 3 * 1]} {field[2 + 3 * 1]}")
    print(f"2 {field[0 + 3 * 2]} {field[1 + 3 * 2]} {field[2 + 3 * 2]}")


def do_move(a):
    while True:
        ask_move = input(f"Please enter coordinate for {a}, where format for X=1 and Y=2 should be like 12: ")
        if ask_move.isdigit() and len(ask_move) == 2 and int(ask_move[0]) in CONTROL_LIST and int(ask_move[1]) in CONTROL_LIST:
            coordinate = int(ask_move[0]) + 3 * int(ask_move[1])
            if field[coordinate] == '-':
                field[coordinate] = a
                break
            else:
                print(f"That move already done by {field[coordinate]}, please choose another move.")
                continue
        else:
            print(f"Coordinate should be in format like 12. Possibly values for X and Y should be in range {CONTROL_LIST}")
            continue

def check_winner(a):
    if any([field[0] == field[1] == field[2] ==a,
            field[3] == field[4] == field[5] ==a,
            field[6] == field[7] == field[8] ==a,
            field[0] == field[3] == field[6] ==a,
            field[1] == field[4] == field[7] ==a,
            field[2] == field[5] == field[8] ==a,
            field[0] == field[4] == field[8] ==a,
            field[2] == field[4] == field[6] ==a]):
        return True
    else:
        return False

print("Welcome to tic tac toe game. New round.")
round = 1
while True:
    field = ['-' for i in range(9)]
    print(draw_field())
    for i in range(1,10):
        print(f"There is {i} move.")
        current_player = 'Y' if i % 2 else 'X'
        do_move(current_player)
        print(draw_field())
        if i > 3 and check_winner(current_player):
            print(f"Winner is player {current_player}!")
            break
        elif i == 9:
            print("No winner in this round.")
    ask_next_round = input("Do you want to play one more round? 'Y' or 'y' for next round: ")
    if not ask_next_round.lower() == 'y':
        break
    round += 1
    print(f"{round} round.")




