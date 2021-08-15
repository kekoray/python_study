# 存放一些音乐播放的逻辑函数

import time
import os
from playsound import playsound
from multiprocessing import Process
from utils.settings import AudioFormat, MusicPath
from utils.decorator import Count


def GetMusicList(MusicPath):
    dir_list = os.listdir(MusicPath)
    music_list = [i for i in dir_list if i[-3:] in AudioFormat]
    return music_list


l = []


@Count
def play(path):
    p = Process(target=playsound, args=(path,))
    l.append(p)
    p.daemon = True
    p.start()


def end():
    try:
        l[0].terminate()
        l.pop(0)
    except IndexError:
        pass


if __name__ == '__main__':
    p = Process(target=playsound, args=("../music_data/chengdu.mp3",))
    p.start()
