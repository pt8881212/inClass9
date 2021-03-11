#fibonacci 

def look(x):
	n1 = 0;
	n2 = 1;
	counter = 0;
	if (x == 0):
		return 0;

	elif (x == 1):
		return 1;

	else:
		while (counter < x):
			temp = n1 + n2;
			n1 = n2;
			n2 = temp;
			counter += 1;
		return n1;


def factorial(y):
	factor = 1;

	for i in range(1, y + 1):
		factor = factor * i;

	return factor;