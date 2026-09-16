# sets
#lvl1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add('twitter')
it_companies.update(['x','nvidia','samsung'])
it_companies.remove('Facebook')
#if the governor says “remove Roger from prison!” but Roger is nowhere to be found, then there’s a problem that needs to be addressed.
#lvl2
print(A.union(B))
#q3 is weird too
print(A.issubset(B))
A.isdisjoint(B)
print(B.union(A))
print(A.union(B))
print(A.symmetric_difference(B))
del A
del B 
#lvl3
age_set=set(age)
print(age)
print (age_set)
print(len(age_set)<len(age))
#strings: is a a letter or a world and can contain numbers 
#list and tuples and set: are idk they just contain the same thing
