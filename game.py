from domain.player import Player
from service import game_service


def play():
    print("game started")

    player = Player.build()

    while True:
        action = get_action()

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

        print(player.get_current_tile())

        game_service.explore_tile(player)

        if not player.is_alive():
            print("GAME OVER")
            break



def get_action() -> str:
    return str(input("input command: ")).lower()

if __name__ == "__main__":
    play()
