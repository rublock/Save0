def till_ground(n, direction):
	for _ in range(n):
		for _ in range(n):
			till()
			move(direction)
		move(East)

def water_ground_and_by_tank(n, direction):
	for _ in range(n):
		for _ in range(n):
			trade(Items.Empty_Tank)
			use_item(Items.Water_Tank)
			move(direction)
		move(East)

def move_and_plant_tima(n, direction):
	for _ in range(n):
		for _ in range(n):
			plant(Entities.Bush)
			move(direction)
		move(East)

def move_and_harvest(n, direction):
	for _ in range(n):
		for _ in range(n):
			harvest()
			move(direction)
		move(East)

till_ground(4, North)

count = 0

while True:
	if count % 2 == 0:
		water_ground_and_by_tank(4, North)
	count += 1
	move_and_plant_tima(4, North)
	move_and_harvest(4, North)
