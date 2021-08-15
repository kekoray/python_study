import tkinter
from utils.action import play, end, GetMusicList
from utils.settings import MusicPath


class UI(object):

    def __init__(self, music_list):
        self.music_list = music_list
        self.music_list_listen = []
        self.index = 0
        self.UI_init()

    def UI_init(self):
        self.root = tkinter.Tk()  # UI的主窗体
        # self.root.geometry('400x400')  # 设置窗体的大小
        self.music = tkinter.StringVar()  # 工具字段，接受选中音乐名称
        # 列表窗口显示音乐列表，位置为第一行第一个
        self.listMusic = tkinter.Listbox(self.root)
        self.listMusic.grid(column=1, row=1)

        # 添加至播放列表
        self.listMusicListen = tkinter.Listbox(self.root)
        self.listMusicListen.grid(column=1, row=2)

        # 添加按钮
        self.add = tkinter.Button(text="添加", command=lambda: [self.select(), self.addListenList(self.music.get())])
        self.add.grid(column=2, row=1)

        self.play = tkinter.Button(text="播放", command=lambda: [end(), self.select_play(), play(MusicPath + self.music.get())])  # 音乐播放
        self.play.grid(column=2, row=2)
        # 上一曲和下一曲按钮
        self.next = tkinter.Button(text="下一曲", command=lambda: [end(), play(MusicPath + self.music_next())])
        self.next.grid(column=1, row=3)
        self.pre = tkinter.Button(text="上一曲", command=lambda: [end(), play(MusicPath + self.music_pre())])  # 上一首
        self.pre.grid(column=2, row=3)

        # 获取当前鼠标选中名称

    def select(self):
        self.music.set(self.listMusic.get(self.listMusic.curselection()))
        self.music_list_listen.append(self.music.get())

        # 获取要添加至播放列表的音乐名称

    def select_play(self):
        self.music.set(self.listMusicListen.get(self.listMusicListen.curselection()))

        # 添加选中音乐到播放区

    def addListenList(self, name):
        self.listMusicListen.insert(0, name)

    def showMusicList(self, music_list):
        for music in music_list:
            self.listMusic.insert(0, music)

    def music_next(self, ):
        if self.index < len(self.music_list_listen) - 1:
            self.index += 1
        else:
            self.index = 0
        return self.music_list_listen[self.index]

    def music_pre(self, ):
        if self.index > 0:
            self.index -= 1
        else:
            self.index = len(self.music_list_listen) - 1
        return self.music_list_listen[self.index]

    def UI_Show(self):
        self.root.mainloop()


if __name__ == '__main__':
    music_list = GetMusicList(MusicPath)
    ui = UI(music_list)
    ui.showMusicList(music_list)
    ui.UI_Show()
