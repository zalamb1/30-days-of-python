numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers=[ i for i in numbers if i<=0]
print (negative_numbers)
#2
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)  