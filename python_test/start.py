import sys
from UI import UI
from get_music_in_web import *
from Analysis import Visualization, Analysis
from utils.action import GetMusicList
from utils.settings import MusicPath

a = sys.argv[1]
if not a or a == "u":  # 启动播放器
    music_list = GetMusicList(MusicPath)
    ui = UI(music_list)
    ui.showMusicList(music_list)
    ui.UI_Show()
elif a == "s":  # 爬取音乐
    artist_id = input("你喜欢的歌手 ID:")
    data = getID(artist_id)
    for id, name in data:
        get_music(id, name)
elif a == "a":  # 分析日记
    _, df = Analysis()
    Visualization(df)
