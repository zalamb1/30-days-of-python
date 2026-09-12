word=["thirty","days","of","python"]
result=" ".join(word)
print(result)
word2=["coding","for","all"]
result2=" ".join(word2)
print(result2)
company="Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company.removeprefix("Coding"))
print(company.index("Coding"))
print(company.replace("Coding","Python"))
print(company.split(" "))
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))
print(company[0])
print(company[-1])
print(company.index("C"))
print(company.index("F"))
print(company.rfind("l"))
sentence="You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))
print(sentence.rindex("because"))
print(sentence[sentence.index("because"):sentence.rindex("because")])
print(company.startswith("Coding"))
print(company.endswith("Coding"))
print("   Coding For All      ".strip())
if ("30DaysOfPaython".isidentifier()):
    print("30DaysOfPaython is a valid identifier")
else :
    print("thirty_days_of_python is a valid identifier")

library=["Django","Flask","Bottle","Pyramid","Falcon"]
print("#".join(library))
print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
r=int(input("Enter radius: "))
area=3.14*r**2
print(f"The area of the circle with radius {r} is {area}.")
print("{}+{}={}".format(8,6,8+6))
print("{}+{}={}".format(8,6,8+6))
print("{}+{}={}".format(8,6,8+6))
print("{}/{}={}".format(8,6,8/6))
print("{}%{}={}".format(8,6,8%6))
print("{}//{}={}".format(8,6,8//6))
print("{}**{}={}".format(8,6,8**6))




