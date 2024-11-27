def water_ground():
	use_item(Items.Water_Tank)

def buy_tank():
	trade(Items.Empty_Tank)

def move_drone(n, direction, func):
	for _ in range(n):
		for _ in range(n):
			func()
			move(direction)
		move(East)

def plant_bush():
	use_item(Items.Water_Tank)
	plant(Entities.Bush)
	trade(Items.Empty_Tank)
	
move_drone(4, North, till)

while True:
	move_drone(4, North, plant_bush)
	move_drone(4, North, harvest)