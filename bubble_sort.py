import time

def bubble_sort(array):
	checked = 0
	start_time = time.time()
	length = len(array)
	sorted = False
	while not sorted:
		sorted = True
		for index in range(checked,length-1):
			value1 = array[index]
			value2 = array[index + 1]
			value3 = 0;
			if value1 > value2:
				value3 = value1
				array[index] = value2
				array[index + 1] = value3
				sorted = False
			checked += 1
	end_time = time.time()
	duration = (end_time - start_time) * 1000
	print array
	print str(duration) + " milliseconds"

x = []
for count in range(1,101):
	from random import randint
	random_number = randint(0,100000)
	x.append(random_number)


bubble_sort(x)

# optimize with while loop and counter