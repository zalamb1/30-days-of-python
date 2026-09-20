import random
#1
def random_user_id():
    characters = "0123456789abcdef"
    user_id = ""
    for i in range(6):
        user_id += random.choice(characters)
    return user_id
print(random_user_id())
#2
def user_id_gen_by_user():
    characters = "0123456789abcdefghijklmnopqrstuvwxyz"
    n=int(input("how manny ids do you want: "))
    m=int(input("how many letters are in the ids: "))
    j=0
    while j<n:
        user_id=""
        for i in range(m):
            user_id += random.choice(characters)

        print(user_id)
        j=j+1
print(user_id_gen_by_user())
#i got the hand of it i think      