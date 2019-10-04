import statistics
import random

#a
wynik1 = 45 * 678
print("1: " + str(wynik1))

#b
arr1 = [ 7,4,2,0,9 ]
arr2 = [ 2,1,5,3,3 ]


#c
def arr_sum(inp_arr_1, inp_arr_2):
	
	len1 = len(inp_arr_1)
	len2 = len(inp_arr_1)
	if len1 != len2:
		return None;
		
	result = []
	
	for i in range(len1):
		result.append(inp_arr_1[i] + inp_arr_2[i])
		
	return result


wynik2 = arr_sum(arr1,arr2)
print("2: " + str(wynik2))


#d
def arr_coord_mul(inp_arr_1, inp_arr_2):
	
	len1 = len(inp_arr_1)
	len2 = len(inp_arr_1)
	if len1 != len2:
		return None;
		
	result = []
	
	for i in range(len1):
		result.append(inp_arr_1[i] * inp_arr_2[i])
		
	return result


wynik3 = arr_coord_mul(arr1, arr2)
print("3: " + str(wynik3))


#e
def arr_dot_product(inp_arr_1, inp_arr_2 ):
	
	len1 = len(inp_arr_1)
	len2 = len(inp_arr_1)
	if len1 != len2 :
		return None
		
	result = 0
	
	for i in range(len1):
		result = result + (inp_arr_1[i] * inp_arr_2[i])
		
	return result


wynik4 = arr_dot_product(arr1, arr2)
print("4: " + str(wynik4))

#f
matrix1 = [[0,2,1],[1,6,4],[5,0,3]]
matrix2 = [[9,8,7],[1,2,7],[4,9,2]]


def matrix_mul(inp_matrix_1, inp_matrix_2):

	height1 = len(inp_matrix_1)
	height2 = len(inp_matrix_2)
	
	width1 = len(inp_matrix_1[0])
	width2 = len(inp_matrix_2[0])
	
	if height2 != width1:
		return None
		
	result = [[0 for row in range(width2)] for col in range(height1)]
	
	for i in range(height1):
		for j in range(width2):
			for k in range(width1):
				result[i][j] += (inp_matrix_1[i][k] * inp_matrix_2[k][j])
			print(result[i][j])
			print(i)
			print(j)
			
			
	return result


wynik5 = matrix_mul(matrix1, matrix2)
print("5: " + str(wynik5))

#g
wynik6 = list(range(1, 101))
print("6: " + str(wynik6))


#h
print("6 avg: " + str(statistics.mean(wynik6)))
print("6 sum: " + str(sum(wynik6)))
print("6 dev: " + str(statistics.stdev(wynik6)))

#i
wynik7 = []
for i in range(50):
	wynik7.append(random.randint(0, 51))

print("7: " + str(wynik7))

#j
print("7 min:" + str(min(wynik7)))
print("7 max:" + str(max(wynik7)))
