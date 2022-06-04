import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QListWidgetItem


class Ui_MainWindow(QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    listWidget = QListWidget()
    window.setWindowTitle("Demo for QListWidget")

    path = 'D:/2022_Dicom_Sorted/nelson01082021/20210108/#-#_data_s168314_3tbcardiac_3tb7831/mid_sax_cine/'
    dir_list = os.listdir(path)
    for fn in dir_list:
        listWidget.addItem(fn)


    window_layout = QVBoxLayout(window)
    window_layout.addWidget(listWidget)
    window.setLayout(window_layout)

    window.show()

    sys.exit(app.exec_())
