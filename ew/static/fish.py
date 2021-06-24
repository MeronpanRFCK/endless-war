import json
import os

from ..model.fish import EwFish

# All the fish, baby!
fish_list = []
with open(os.path.join('json', 'fish.json')) as f:
    fish = json.load(f)
    for i in fish:
        i = fish[i]
        fish_list.append(
            EwFish(
                id_fish=i['id_fish'],
                str_name=i['str_name'],
                size=i['size'],
                rarity=i['rarity'],
                catch_time=i['catch_time'],
                catch_weather=i['catch_weather'],
                str_desc=i['str_desc'],
                slime=i['slime'],
                vendors=i['vendors']
            ))

# A map of id_fish to EwFish objects.
fish_map = {}

common_fish = []
uncommon_fish = []
rare_fish = []
promo_fish = []

rainy_fish = []
night_fish = []
day_fish = []

rarity_to_list = {
    "common": common_fish,
    "uncommon": uncommon_fish,
    "rare": rare_fish,
    "promo": promo_fish
}

# A list of fish names.
fish_names = []

# Populate fish map, including all aliases.
for fish in fish_list:
    fish_map[fish.id_fish] = fish
    fish_names.append(fish.id_fish)
    # Categorize fish into their rarities
    rarity_to_list[fish.rarity].append(fish)
    if fish.catch_weather == "rainy":
        rainy_fish.append(fish)
    if fish.catch_time == "night":
        night_fish.append(fish)
    elif fish.catch_time == "day":
        day_fish.append(fish)
    for alias in fish.alias:
        fish_map[alias] = fish
