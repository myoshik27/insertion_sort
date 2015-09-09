def bubble_sort(array):
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
	return array
x = []
for count in range(1,101):
	from random import randint
	random_number = randint(0,100)
	x.append(random_number)
y = bubble_sort(x)
