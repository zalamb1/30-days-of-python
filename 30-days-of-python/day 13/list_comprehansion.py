numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers=[ i for i in numbers if i<=0]
print (negative_numbers)
#2
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)  
#3
list_numbers=[(i,i**0,i**1,i**2,i**3,i**4,i**5) for i in range(11)]
print(list_numbers)
#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
result = []
for country in countries:
    name, capital = country[0]
    result.append([name.upper(), name[:3].upper(), capital.upper()])
print(result)
#5
result = []
for country in countries:
    name, city = country[0]
    result.append({'country': name.upper(),'city': city.upper()})
print(result)
#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
result = []
for name in names:
    first, last = name[0]
    result.append(first + ' ' + last)
print(result)