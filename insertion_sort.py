import time
import random

x = []
for count in range(1,101):
	from random import randint
	random_number = randint(0,100000)
	x.append(random_number)

def insertion_sort(array):
	start_time = time.time()
	for starting_index in range (1,len(array)):
		previous_index = starting_index - 1
		current_index = starting_index
		while array[previous_index] > array[current_index]:
			array[current_index],array[previous_index] = array[previous_index],array[current_index]		
			previous_index -= 1
			current_index -= 1
			if current_index == 0:
				break
	end_time = time.time()			
	duration = (end_time - start_time) * 1000
	print array
	print str(duration) + " milliseconds"

insertion_sort(x)