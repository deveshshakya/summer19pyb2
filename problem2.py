from googlesearch import search
from bs4 import BeautifulSoup

topic = input("Enter topic: ")

url = []

for i in search(topic, stop=10):
    # print(i)
    url.append(i)

print(*url, sep='\n')
