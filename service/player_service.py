from domain.player import Player
from service import game_service


def eat(player: Player):
    if not player.food:
        print("No food")
        return
    if player.health >= Player.MAX_HEALTH:
        print("Your health is full")
        return

    for k, f in enumerate(player.food):
        print("{}: {} heals {}".format(k, f.name, f.heal_value))

    selected = int(game_service.get_action("Select food to eat: "))

    try:
        food = player.food[selected]
    except (IndexError, ValueError):
        print("Food not found")
        return

    player.food.remove(food)

    player.health = min(Player.MAX_HEALTH, food.heal_value + player.health)

    print("Your health {}".format(player.health))


