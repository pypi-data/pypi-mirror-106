from . import VK
from .spotify import Spotify
from .yandexmusic import YandexMusic
from .config import Default


# Попытка авторизоваться и получить объекты класса + плейлисты соурса
def init_class_objects(source, s_login, s_pass, target, t_login, t_pass):
    data = {
        "YM": {
            "artists": [],
            "albums": [],
            "playlists": {},
            "alltracks": []
        },
        "SP": {
            "artists": [],
            "albums": [],
            "playlists": {},
            "alltracks": []
        },
        "VK": {
            "artists": [],
            "albums": [],
            "playlists": {},
            "alltracks": []
        }
    }
    if source == 'sp':
        sp_obj = Spotify(s_login, scope=Default.SCOPE, data=data)
        s_playlists = sp_obj.get_playlists()
        if target == 'ym':
            ym_obj = YandexMusic(login=t_login, password=t_pass, export_data=data)
        else:
            return 'unexpected target'
        return sp_obj, ym_obj, s_playlists

    elif source == 'ym':
        ym_obj = YandexMusic(login=t_login, password=t_pass, export_data=data)
        s_playlists = ym_obj.get_playlists()
        if target == 'sp':
            sp_obj = Spotify(s_login, scope=Default.SCOPE, data=data)
        else:
            return 'unexpected target'
        return ym_obj, sp_obj, s_playlists

    elif source == 'vk':
        vkaudio = VK.get_auth(s_login,s_pass)
        s_playlists = VK.get_playlists(vkaudio)
        print(s_playlists)
        if target == 'ym':
            t_obj = YandexMusic(login=t_login, password=t_pass, export_data=data)
        elif target == 'sp':
            t_obj = Spotify(s_login, scope=Default.SCOPE, data=data)
        return vkaudio, t_obj, s_playlists
