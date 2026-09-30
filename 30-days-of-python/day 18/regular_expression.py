import re
#1
paragraph = """I love teaching. If you do not love teaching what else can you love.
I love Python if you do not love something which can give you all the capabilities
to develop an application what else can you love."""

words = re.findall(r'\w+', paragraph)
count = {}
for word in words:
    count[word] = words.count(word)
print(sorted(count.items(), key=lambda x: x[1], reverse=True))
#2
def is_valid_variable(name):
    return bool(re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name))
print(is_valid_variable('yahya_mannai'))
#3
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
def clean_text(ch):
    return(re.sub(r'[^A-Za-z\s]',"",ch))
print(clean_text(sentence))
