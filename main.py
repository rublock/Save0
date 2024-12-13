from plant import *
from buy_items import *

count = 1
expand = 5

def water_ground():
	use_item(Items.Water)

def move_drone(n, direction, plant_some):
	for _ in range(n):
		for _ in range(n):
			harvest_plant()
			plant_some()
			move(direction)
		move(East)

def harvest_plant():
	if can_harvest():
		harvest()
		# water_ground()
		
move_drone(expand, North, till)

while True:
	if count % 3 == 0:
		move_drone(expand, North, plant_tree)

	move_drone(expand, North, plant_bush)
	move_drone(expand, North, plant_carrot)
	move_drone(expand, North, plant_pumpkin)
	move_drone(expand, North, plant_sunflowers)

	count += 1
