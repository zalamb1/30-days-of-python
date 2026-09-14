#lvl1
tup=tuple()
brothers=("jasser","hamma","nathem","hamadi")
sisters=("soumoud","jouri")
siblings=brothers+sisters
print("Number of siblings: ", len(siblings))
parents=("elhadi","moufida")
family_members=siblings+parents
#lvl2
family=family_members
print(family)
fruits=("banana","orange","mango","lemon")
vegetables=("tomato","potato","cabbage","onion","carrot")
animals=("lion","tiger","bear","zebra")
food_stuff=fruits+vegetables+animals
print("Food stuff: ", food_stuff)
food_stuff_lt=[food_stuff]
print(food_stuff_lt)
print(food_stuff[0:len(food_stuff)//2])
print(food_stuff[0:3])
print(food_stuff[-4:-1])
del food_stuff
nordic_countries=("denmark","finland","iceland","norway","sweden")
print("estonia" in nordic_countries)
print("iceland" in nordic_countries)