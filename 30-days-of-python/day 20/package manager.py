#pip is the default package manager for python and to use it you write : pip install
import requests
import re
romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(romeo_and_juliet)
text = response.text
words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
most_frequent = sorted(
    word_count.items(),
    key=lambda x: x[1],
    reverse=True
)
print(most_frequent[:10])