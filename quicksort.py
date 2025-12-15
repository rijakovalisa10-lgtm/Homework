from random import choice

def quicksort(array):
	if len(array) in (0, 1):
		return array
	
	pilot = choice(array)
	low = [x for x in array if x < pilot]
	mid = [x for x in array if x == pilot]
	high = [x for x in array if x > pilot]
	
	return quicksort(low) + mid + quicksort(high)
