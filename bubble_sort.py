import time

def bubble_sort(array):
	start_time = time.time()
	length = len(array)
	for value in array:
		for index in range(0,length-1):
			value1 = array[index]
			value2 = array[index + 1]
			value3 = 0;
			if value1 > value2:
				value3 = value1
				array[index] = value2
				array[index + 1] = value3
	end_time = time.time()
	duration = end_time - start_time
	print duration
	return array


x = []
for count in range(1,101):
	from random import randint
	random_number = randint(0,100000)
	x.append(random_number)


y = bubble_sort(x)
print y 

# optimize with while loop and counter