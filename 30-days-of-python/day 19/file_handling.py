#lvl1
#1
#f1=open("donald_speech.txt","r")
f2=open("melina_trump_speech.txt","r")
f3=open("obama_speach.txt","r")
f4=open("michelle_obama_speach.txt","r")
words=f2.read().split()
for word in words:
    print(word,words.count(word))
lines=f2.readlines()
for line in lines:
    print(line,lines.count(line))

#3
import json

def most_populated_countries(filename, n):
    with open(filename, 'r') as f:
        countries = json.load(f)

    countries.sort(key=lambda x: x['population'], reverse=True)

    result = []

    for country in countries[:n]:
        result.append({
            'country': country['name'],
            'population': country['population']
        })

    return result


print(most_populated_countries('countries_data.json', 10))

