# Importing required libraries
from bs4 import BeautifulSoup
import requests

# URL of the webpage to scrape
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Sending a request to the webpage and getting the HTML content
response = requests.get(URL)
website_html = response.text

# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(website_html, "html.parser")

# Finding all elements with the tag 'h3' and class 'title' (which contains movie titles)
movies = soup.find_all(name="h3", class_="title")

# Extracting movie titles from each element and storing them in a list
movie_titles = [movie.getText() for movie in movies]

# Reversing the order of movie titles
movie_titles.reverse()

# Writing the movie titles into a text file named 'movie_list.txt'
with open("movie_list.txt", "w") as writer:
    for movie in movie_titles:
        writer.write(f"{movie}\n")