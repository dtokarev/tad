from domain.player import Player
from service import game_service


def eat(player: Player):
    food_list = player.food

    if not food_list:
        print("No food")
        return
    if player.health >= Player.MAX_HEALTH:
        print("Your health is full")
        return

    for k, f in enumerate(food_list):
        print("{}: {} heals {}".format(k, f.name, f.heal_value))

    selected = int(game_service.get_action("Select food to eat: "))

    try:
        food = food_list[selected]
    except IndexError:
        print("Food not found")
        return

    food_list.remove(food)

    player.health += food.heal_value

    if player.health > Player.MAX_HEALTH:
        player.health = Player.MAX_HEALTH

    print("Your health {}".format(player.health))


