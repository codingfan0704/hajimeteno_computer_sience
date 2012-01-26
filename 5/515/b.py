def mystery_function(values):
	result = []
	for i in range(len(values[0])):
		result.append([values[0][i]])
		for j in range(1, len(values)):
			result[-1].append(values[j][i])
	return result

print mystery_function([[1,2,3,10], [4,5,6,], [7,8,9,11]])