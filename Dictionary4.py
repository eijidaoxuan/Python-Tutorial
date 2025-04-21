def main():
    history("Move: ")

def history(x):
    movement = []
    while True:
        try:
            move = input(x).lower()
            if move == "up" or move == "down" or move == "right" or move == "left":
                movement.append(move)
            elif move == "stop":
                print("Thanks for playing.")
                break
            elif move == "clear":
                movement.clear()
            elif move == "back":
                gone = movement.pop()
                print(f"Deleted: {gone}")
            else:
                print("Please enter the right movement.")
            print(movement)
        except IndexError:
            print("Please do a movement.")

if __name__ == "__main__":
    main()