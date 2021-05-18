import re, os
import requests

class truyenVN():
    def __init__(self):
        super().__init__()

    def getAllChap(link):
        r = requests.get(link)
        regex = r"Chapter mới nhất: (.*?) href=\"(.*?)\">(.*?)<\/a>"
        match = re.findall(regex, r.text)
        return (match[0][2].split()[1])

    def getImg(link):
        r = requests.get(link)
        str = r.text
        str = str.split('<input type="hidden" name="p" value="')
        str = str[1].split('">')
        p = (str[0])

        payload = {
            'action': 'z_do_ajax',
            '_action': 'load_imgs_for_chapter',
            'p': p
        }
        headers = {
            'x-requested-with': 'XMLHttpRequest',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        r = requests.post("https://truyenvn.com/wp-admin/admin-ajax.php", data=payload, headers=headers)
        imgList = []
        for i in r.json()['mes']:
            imgList.append(i['url'])

        return imgList
    def saveImg(imglist, chap):
        id = 0
        arr = []
        for i in imglist:
            print(i)
            r = requests.get(i.replace("\r", ""))
            file = 'rs{chap}/{id}.jpg'.format(id=id, chap=chap)
            try:
                with open(file, 'wb') as f:
                    f.write(r.content)
                    f.close()
            except Exception as e:
                os.system('mkdir rs{}'.format(chap))
                with open(file, 'wb') as f:
                    f.write(r.content)
                    f.close()
                print(e)
            id+=1
            arr.append(file)
        return arr