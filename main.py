import requests
from bs4 import BeautifulSoup

travel_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{travel_date}/"
response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")
all_songs = soup.findAll(name="h3", class_="a-no-trucate")
song_list = [song.getText().strip() for song in all_songs]

print(song_list)
