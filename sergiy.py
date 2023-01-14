import requests
from bs4 import BeautifulSoup


class Music:
    def __init__(self, artist:str, song:str, duration:str):
        self.artist = artist
        self.song = song
        self.duration = duration

    def __str__(self):
        res = self.artist + ' - ' + self.song + ' ' + f'({self.duration})'
        return res


songs = []
url = 'https://music.xn--41a.ws/'

headers = {}
headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 ' \
                        '(KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'



def find_table():
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    music_list = soup.find('ul', class_='playlist favorites')
    return music_list

def find_song_info(music_list):
    for music in music_list:
        try:
            name = music.find('h2').find('em').find('a').text.strip()
            artist = music.find('b').find('a').text.strip()
            duration = music.find('span', class_='playlist-duration').text.strip()

            songs.append(Music(song=name, artist=artist, duration=duration))
        except:
            pass

table = find_table()
find_song_info(table)
for song in songs:
    print(song)