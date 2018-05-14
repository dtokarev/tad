from domain.player import Player


def play():
    print("game started")

    player = Player.build()

    while True:
        action = get_action()
        print(player.get_current_tile())

        if action == "q":
            print("exiting")
            break
        elif action in ["i"]:
            player.print_inventory()
        elif action == "s":
            player.move(0, 1)
        elif action == "w":
            player.move(0, -1)
        elif action == "a":
            player.move(-1, 0)
        elif action == "d":
            player.move(1, 0)


def get_action() -> str:
    return str(input("input command: ")).lower()

if __name__ == "__main__":
    play()
