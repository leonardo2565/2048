from G_2048 import g_2048
def main():
    new = g_2048()

    print("Controls: W (Up), A (Left), S (Down), D (Right), Q (Quit)")
    while True:
        new.print_2048()
        move = input("Enter move: ").strip().lower()
        
        if move == 'q':
            points = sum(x.value for x in new.field if x.value is not None)
            print(f"Game Over! You did {points} points")
            break
        elif move == 'w':
            new.merging_true("top")
        elif move == 's':
            new.merging_true("bottom")
        elif move == 'a':
            new.merging_true("left")
        elif move == 'd':
            new.merging_true("right")
        else:
            print("Invalid input. Use W/A/S/D to move, Q to quit.")

main()