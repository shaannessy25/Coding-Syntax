#Given a list of n numbers, determine if it contains any duplicate numbers.
	
	a = [1,3,5,7,9]
	def find_duplicate(a):
		for item in a:
			if item is item:
				return item
			else: 
				return None