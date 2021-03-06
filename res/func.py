
from PyQt5.QtWidgets import QMessageBox
from pyasn1.type.univ import Null
from res.ggmodule import ggfunc
import threading
import shutil
from queue import Queue
from res.sitelib.truyenvn import truyenVN
from res.text import string

def validate(obj, num):
    try:
        num = int(num)
        check = True
    except ValueError:
        QMessageBox.critical(obj, string['func']['title_alert_box'], string['func']['message_alert_box'], QMessageBox.Cancel, QMessageBox.Cancel)
        check = False
    if check:
        if num > 500:
            confirm = QMessageBox.warning(obj, string['func']['title_confirm_box'], string['func']['message_confirm_box'], QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
            if (confirm == QMessageBox.Yes):
                return ggfunc.login()
            else:
                return False
        else:
            return ggfunc.login()
    else:
        return False

def error_log(i):
    with open("log.txt", "a+", encoding="utf-8-sig") as r:
        r.write(i + ": LỖI\n")


class control():
    def __init__(self, Form):
        super().__init__()
        self.Form = Form
        self.loginGoogleButton_clicked()
    def worker(self, q):
        while True:
            # print("[{}]  => Đang get job\n".format(threading.current_thread().name))
            item = q.get()
            if (item is None):
                # print("[{}]  => Hết job".format(threading.current_thread().name))
                q.task_done()
                break

            print("[{}]  => Success -> Working\n".format(threading.current_thread().name))      
            data = item.split("|")
            item = data[0]
            chapnew = truyenVN.getAllChap(item)
            try:
                chap_begin = data[1]
                try:
                    chap_end = data[2]
                except:
                    chap_end = str(int(chapnew) - 1)
            except:
                chap_begin = 1
            drive = ggfunc.google_drive(self.servicefromoauth[1])
            foldergoogleid = (drive.create_folder(item.split(".com/")[1]))
            for i in range(int(chap_begin), int(chap_end)+1):
                i = str(i)
                idfolderchap = drive.create_folder("Chap " + (i), parent=foldergoogleid)
                url = [f"{item}-chuong-{i}.html", f"{item}-chuong-{i}-2.html"]
                try:
                    imglist = truyenVN.getImg(url)
                except:
                    error_log(i)
                    continue
                arrimg = truyenVN.saveImg(imglist, i, name=item.split(".com/")[1])
                for j in arrimg:
                    print(drive.upload_to_folder(j, idfolderchap))



                shutil.rmtree('rs' + i, ignore_errors=True)
                print("Chap " + i + " done")
            q.task_done()

    def controller(self, listchap, thread_num=10):
        q = Queue()
        for i in range(thread_num):
            threading.Thread(target=self.worker, args=(q,)).start()

        for i in listchap:
            q.put(i)

        for i in range(thread_num):
            q.put(None)

    def loginGoogleButton_clicked(self):
        servicefromoauth = validate(self.Form, self.Form.threadnum.text())
        self.servicefromoauth = servicefromoauth
        # print(answer)
        if (servicefromoauth is not False):
            self.Form.labelInfoUser.setHidden(0)
            self.Form.labelInfoUser.setText("Hi " + ggfunc.identity(servicefromoauth[2]).getName())
            self.Form.loginGoogleButton.setHidden(1)      
            list_chap = self.Form.plainTextEdit.toPlainText().splitlines()
            thread_num = int(self.Form.threadnum.text())
            threading.Thread(target=self.controller, args=(list_chap, thread_num)).start()