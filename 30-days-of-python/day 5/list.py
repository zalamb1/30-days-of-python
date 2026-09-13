l=[]
lst=[1,2,3,4,5]
print(len(lst))
print(lst[0],lst[len(lst)-1],lst[len(lst)//2])
mixed_data_types=["zalambi",20,182,"married","germanica"]
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print(it_companies)
print(len(it_companies))
print(it_companies[0],it_companies[len(it_companies)-1],it_companies[len(it_companies)//2])
it_companies.append("meta")
it_companies.insert(5,"Twitter")
print(it_companies)
x=it_companies[0]
x=x.upper()
it_companies[0]=x
print(it_companies)
text="#".join(it_companies)
print(text)
print("FACEBOOK" in it_companies)

print(it_companies.sort())
print(it_companies.reverse())
print(it_companies[0:3])
print(it_companies[-4:-1])
print(it_companies.remove(it_companies[0]))
print(it_companies.remove(it_companies[len(it_companies)//2]))
print(it_companies.remove(it_companies[-1]))
print(it_companies.clear())
del it_companies
front_end=['html','css','js','react','redux']
back_end=['node','express','mongodb']
joined=front_end+back_end
full_stack=joined.copy()
full_stack.append("python")
full_stack.append("SQL")
full_stack.append("Redux")
#lvl2
ages=[19,22,19,24,20,25,26,24,25,24]
ages.sort()
min_age=ages[0]
max_age=ages[len(ages)-1]
ages.append(min_age)
ages.append(max_age)
median_age=ages[len(ages)//2]
sum_age=sum(ages)
average_age=sum_age/len(ages)
range_age=max_age-min_age
(min_age-average_age)==(max_age-average_age)






