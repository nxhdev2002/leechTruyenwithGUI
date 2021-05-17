import re
import requests

class truyenVN():
    def __init__(self):
        super().__init__()

    def getAllChap(link):
        r = requests.get(link)
        regex = r"Chapter mới nhất: (.*?) href=\"(.*?)\">(.*?)<\/a>"
        match = re.findall(regex, r.text)
        return (match[0][2].split()[1])
