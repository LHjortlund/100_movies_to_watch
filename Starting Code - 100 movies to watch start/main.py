import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website = BeautifulSoup(response.text, "html.parser")

all_movies = website.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
#reverse list
movies =movie_titles[::-1]
# #or
# for n in range(len(movie_titles) -1, -1, -1):
#     print(movie_titles[n])
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")

