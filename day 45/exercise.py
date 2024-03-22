from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# print(soup.prettify())

article_text = soup.select_one(selector=".titleline a").getText()
article_link = soup.select_one(selector=".titleline a").get("href")
article_upvote = soup.find(name="span", class_="score").getText()

print(article_text)
print(article_link)
print(article_upvote)