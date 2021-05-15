from PyQt5.QtWidgets import QMessageBox

def validate(obj, num):
    try:
        num = int(num)
        check = True
    except ValueError:
        QMessageBox.critical(obj, '?????????', "?????? Mày đang làm cái gì thế ?????", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
        check = False
    if check:
        if num > 500:
            confirm = QMessageBox.warning(obj, 'oh no', "Số thread m nhập vượt quá 500? M có chắc máy đủ khoẻ để gánh đc nó chứ ?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
            if (confirm == QMessageBox.Yes):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
