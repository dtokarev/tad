from domain import player as pl
from service import game_service, player_service


def play():
    print("game started")

    player = pl.build()

    while True:
        action = game_service.get_action("Your command: ")

        if action == "q":
            print("exiting")
            break
        elif action in ["i"]:
            player.print_inventory()
        elif action == "s":
            player.move(0, -1)
            game_service.explore_tile(player)
            game_service.print_nearby_map(player)
        elif action == "w":
            player.move(0, 1)
            game_service.explore_tile(player)
            game_service.print_nearby_map(player)
        elif action == "a":
            player.move(-1, 0)
            game_service.explore_tile(player)
            game_service.print_nearby_map(player)
        elif action == "d":
            player.move(1, 0)
            game_service.explore_tile(player)
            game_service.print_nearby_map(player)
        elif action == "f":
            player_service.eat(player)
        elif action == "m":
            game_service.print_nearby_map(player)

        if not player.is_alive():
            print("GAME OVER")
            break


if __name__ == "__main__":
    play()
