moves = []
movestowin = ['right', 'down', 'left', 'up']
movesleft = len(movestowin)
while True:
    # assuming the user enters valid input
    move = input("Enter your move (to make a square 2x2): ")
    if move.lower() == 'restart':
        moves.clear()
        print("restarted")
    elif move.lower() == 'undo':
        rmmove = moves.pop()
        print(f"undone: {rmmove}")
    moves.append(move)
    if moves == movestowin:
        print("You win!")
        break  
    elif len(moves) == len(movestowin) and moves != movestowin:
        print("You lose!")
        break
    movesleft -= 1
    print(f"Moves: {moves}, Moves left: {movesleft}")