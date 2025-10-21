import requests
import json

query=input("what ttype of news are you intrested in?: ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2024-02-27&sortBy=publishedAt&apiKey=b07cc5ad48054ba997143e20358a1a22"
r = requests.get(url)
news= json.loads(r.text)
# print(news,type(news))
for article in news["articles"]:
  print(article["title"])
  print("#####################################################")
  print(article["description"])
  print("----------------------------------------------------------")
