from plant import *
from buy_items import *

count = 1
expand = 5

def water_ground():
	use_item(Items.Water_Tank)

def move_drone(n, direction, func):
	for _ in range(n):
		for _ in range(n):
			harvest_plant()
			func()
			move(direction)
		move(East)

def harvest_plant():
	if can_harvest():
		harvest()
		water_ground()
		
move_drone(expand, North, till)

while True:
	if count % 3 == 0:
		buy_items()
		move_drone(expand, North, plant_tree)

	move_drone(expand, North, plant_bush)
	# move_drone(expand, North, plant_carrot)
	move_drone(expand, North, plant_pumpkin)

	count += 1
