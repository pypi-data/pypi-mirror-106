import requests
from yandex_music.client import Client
from yandex_music.utils.difference import Difference
from yandex_music.utils.request import Request
import json
import time
from MoveMyMusic.yandexmusic import YandexMusic


ym = YandexMusic('xxx', 'xxx', export_data=None)
ym.get_auth()


# print(client.token)
# POST
url = 'https://music.yandex.ru/handlers/import.jsx'


playlist_id, playlist_rev, playlist_trackCount = ym.check_playlist('huila')
print(f'ID:{playlist_id}, REV:{playlist_rev}, COUNT:{playlist_trackCount}')
time.sleep(2)
playlist_id, playlist_rev, playlist_trackCount = ym.check_playlist('huila')
print(f'ID:{playlist_id}, REV:{playlist_rev}, COUNT:{playlist_trackCount}')

song_to_import = "хаски ай\nхаски панелька\nхаски бит шатает голову\nпошлая молли супермаркет\nпошлая молли мишка"
string_of_songs = song_to_import.replace(' ', '+')

json_values = {
               'content': string_of_songs
               }

while True:
    r1_import = requests.post(url, json=json_values, allow_redirects=False)
    if r1_import.status_code == 302:
        time.sleep(3)
    if r1_import.status_code == 200:
        id_import = json.loads(r1_import.text)['importCode']
        break
params={
    'code':id_import
}
time.sleep(3)

while True:
    resp = requests.get(url=url, params=params, allow_redirects=False)
    if resp.status_code == 200:
        resp = json.loads(resp.text)
        if resp['status'] == 'in-progress':
            time.sleep(3)
        elif resp['status'] == 'done':
            print('done')
            trackIds = resp['trackIds']
            print(trackIds)
            break
    else:
        print(resp.status_code)
        time.sleep(3)

playlist_id, playlist_rev, playlist_trackCount = ym.check_playlist('huila')
print(f'ID:{playlist_id}, REV:{playlist_rev}, COUNT:{playlist_trackCount}')
tracks_diff = [dict([('id', item.split(':')[0]), ('album_id', item.split(':')[1])]) for item in trackIds]
print(tracks_diff)
diff = Difference().add_insert(playlist_trackCount, tracks_diff)
print(diff)
ym.client.users_playlists_change(kind=playlist_id,diff=diff.to_json(),revision=playlist_rev)
