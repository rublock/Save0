def check_if_zero_coordinates():
	# Проверка на 0 координаты
	return get_pos_x() == 0 and get_pos_y() == 0

def move_to_zero_coordinates(col):
	# Двигаться пока не будут 0 координаты
	for _ in range(col): 
		move(South)
		if check_if_zero_coordinates():
			return True
		for _ in range(col): 
			move(West)
			if check_if_zero_coordinates():
				return True
		
while True:
	if move_to_zero_coordinates(4):
		break

def move_and_plant(n, direction, item):
	if item == None:
		for _ in range(n):
			if can_harvest():
				harvest()
			move(direction)
		move(East)
	elif item == Entities.Bush:
		for _ in range(n):
			if can_harvest():
				harvest()
				plant(Entities.Bush)
			else:
				plant(Entities.Bush)
			move(direction)
		move(East)
	elif item == Entities.Carrots:
		for _ in range(n):
			trade(Items.Carrot_Seed)
			if can_harvest():
				harvest()
				till()
				plant(Entities.Carrots)
			else:
				till()
				plant(Entities.Carrots)
			move(direction)
		move(East)
		
def main():				
	while True:
		#move_and_plant(4, North, None)
		move_and_plant(4, North, Entities.Bush)
		#move_and_plant(4, North, Entities.Carrots)

main()
	
				