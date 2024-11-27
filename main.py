def water_ground():
	trade(Items.Empty_Tank)
	use_item(Items.Water_Tank)

def buy_tank():
	trade(Items.Empty_Tank)

def move_drone(n, direction, func):
	for _ in range(n):
		for _ in range(n):
			harvest_plant()
			water_ground()
			func()
			move(direction)
		move(East)

def plant_bush():
	plant(Entities.Bush)

def plant_carrot():
	trade(Items.Carrot_Seed)
	plant(Entities.Carrots)

def harvest_plant():
	if can_harvest():
		harvest()
	
	
move_drone(4, North, till)

count = 0

while True:
	print(count)
	if count % 1 == 0:
		trade(Items.Carrot_Seed)
		trade(Items.Empty_Tank)
	
	count += 1

	move_drone(4, North, plant_bush)
	move_drone(4, North, plant_carrot)