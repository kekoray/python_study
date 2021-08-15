import requests
import re
from utils.settings import headers, proxies


def get_music(id, name, proxies=proxies, headers=headers):
    URL = "http://music.163.com/song/media/outer/url?id=%s.mp3" % id
    try:
        response = requests.get(URL, proxies=proxies, headers=headers)
        with open("%s.mp3" % name, "wb") as f:
            f.write(response.content)
            print("%s 下载成功" % name)
    except Exception:
          print("%s 下载失败" % name)


def getID(artist_id):
    URL = "https://music.163.com/artist?id=%s" % artist_id
    response = requests.get(URL, proxies=proxies, headers=headers)
    data = re.findall(r'<a href="/song\?id=([0-9]+)">(.*?)</a>', response.text)
    print(data)
    return data


# if __name__ == '__main__':
    # data = getID(12138269)
    # print(data)
    # # for id, name in data:
    # #     get_music(id, name)
    # get_music(569213220, '像我这样的人')
