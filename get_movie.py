import requests
import json

API_KEY = "32aaf156"
movie_title = "Spider-Man: No Way Home"

url = f"https://www.omdbapi.com/?apikey={API_KEY}&t={movie_title}"
response = requests.get(url)
data = response.json()

with open("movie.json", "w") as file:
    json.dump(data, file, indent=4)

print("Movie data saved to movie.json")