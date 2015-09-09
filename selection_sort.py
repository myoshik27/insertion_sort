import time
import random

x = []
for count in range(1,101):
	from random import randint
	random_number = randint(0,100000)
	x.append(random_number)

def selection_sort(array):
	start_time = time.time()
	for starting_index in range(len(array)-1):
		min_index = starting_index
		for current_index in range(starting_index+1,len(array)):
			if array[min_index] > array[current_index]:
				min_index = current_index
		array[min_index],array[starting_index] = array[starting_index],array[min_index]
	end_time = time.time()
	duration = (end_time - start_time) * 1000
	print array
	print str(duration) + " milliseconds"

selection_sort(x)
