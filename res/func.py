
from PyQt5.QtWidgets import QMessageBox
from res.ggmodule import ggfunc
import threading
from queue import Queue
from res.sitelib.truyenvn import truyenVN


def validate(obj, num):
    try:
        num = int(num)
        check = True
    except ValueError:
        QMessageBox.critical(obj, '?????????', "?????? Mày đang làm cái gì thế ?????", QMessageBox.Cancel, QMessageBox.Cancel)
        check = False
    if check:
        if num > 500:
            confirm = QMessageBox.warning(obj, 'oh no', "Số thread m nhập vượt quá 500? M có chắc máy đủ khoẻ để gánh đc nó chứ ?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
            if (confirm == QMessageBox.Yes):
                return ggfunc.login()
            else:
                return False
        else:
            return ggfunc.login()
    else:
        return False

def getInfo(service):
    return ggfunc.identity(service).getEmail()

class control():
    def __init__(self, Form):
        super().__init__()
        self.Form = Form
        self.loginGoogleButton_clicked()
    def worker(self, q):
        while True:
            print("[{}]  => Đang get job\n".format(threading.current_thread().name))
            item = q.get()
            if (item is None):
                print("[{}]  => Hết job".format(threading.current_thread().name))
                q.task_done()
                break
            print("[{}]  => Success -> Working\n".format(threading.current_thread().name))
            chapnew = truyenVN.getAllChap(item)
            print(chapnew)
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
        # print(answer)
        if (servicefromoauth is not False):
            self.Form.labelInfoUser.setHidden(0)
            self.Form.labelInfoUser.setText("Hi " + getInfo(servicefromoauth[2]))
            self.Form.loginGoogleButton.setHidden(1)      
            list_chap = self.Form.plainTextEdit.toPlainText().splitlines()
            thread_num = int(self.Form.threadnum.text())
            threading.Thread(target=self.controller, args=(list_chap, thread_num)).start()