from googlesearch import search

topic = input("Enter topic: ")

url = []

for i in search(topic, stop=10):
    url.append(i)

with open('Links.txt', 'w') as f:
    for i in url:
        f.write(i)
        f.write('\n')

print(*url, sep='\n')