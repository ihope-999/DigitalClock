from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QIcon, QFontDatabase, QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QHBoxLayout, QWidget
import datetime
import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Digital Clock')
        self.setWindowIcon(QIcon('zzz.png'))
        self.setStyleSheet('background-color:black;')
        self.current_time = QTime.currentTime().toString('hh - mm - ss AP ')
        self.widget1 = QLabel(self.current_time,self)
        self.hbox = QHBoxLayout()
        self.font_id = QFontDatabase.addApplicationFont('DS-DIGIT.TTF')
        self.font_family = QFontDatabase.applicationFontFamilies(self.font_id)[0]
        self.my_font = QFont(self.font_family,150)
        self.central_widget= QWidget()
        self.timer = QTimer(self)
        self.initIU()
    def initIU(self):
        self.widget1.setFont(self.my_font)
        self.setCentralWidget(self.central_widget)
        self.hbox.addWidget(self.widget1)
        self.central_widget.setLayout(self.hbox)
        self.widget1.setStyleSheet('background-color:black;'
                                 'color: yellow;'
                                 'padding: 15px70px;'
                                   'margin: 10px;'
                                 )
        self.timer.timeout.connect(self.timeout_on)
        self.timer.start(1000)

    def timeout_on(self):
        self.current_time = QTime.currentTime().toString('hh - mm - ss AP ')
        self.widget1.setText(self.current_time)





def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()