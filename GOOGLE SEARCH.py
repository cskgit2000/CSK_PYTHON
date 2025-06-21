pip install google
from googlesearch import search

query = input("ASK ANYTHIN : ")

for url in search(query):
    print(url)
    