import pytube
import requests
from bs4 import BeautifulSoup
import os

def download_playlist(URL):
    #URL = f"https://www.youtube.com/watch?v=JGwWNGJdvx8&list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj"
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    headers = {"user-agent" : USER_AGENT}
    resp = requests.get(URL, headers=headers)
    soup = BeautifulSoup(resp.content, "html.parser")
    results = []
    for g in soup.find_all('a', class_="spf-link playlist-video clearfix yt-uix-sessionlink spf-link"):
        link = g['href']
        link = "https://www.youtube.com" + link
        results.append(link)

    for i in range (len(results)):
        youtube = pytube.YouTube(results[i])
        video = youtube.streams.first()
        path = os.path.abspath(os.getcwd())
        video.download(path)
    return "Check :", path

