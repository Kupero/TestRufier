from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *
from PyQt5.QtGui import QFont
from thirdWindow import *

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.Lb_name = QLabel(txt_name)
        self.Lb_age = QLabel(txt_age)
        self.Lb_test1 = QLabel(txt_test1)
        self.Lb_test2 = QLabel(txt_test2)
        self.Lb_test3 = QLabel(txt_test3)
        self.Lb_timer = QLabel(txt_timer)
        self.Lb_timer.setFont(QFont('Times', 36, QFont.Bold))

        self.Le_name = QLineEdit(txt_hintname)
        self.Le_age = QLineEdit(txt_hintage)
        self.Le_test1 = QLineEdit(txt_hinttest1)
        self.Le_test2 = QLineEdit(txt_hinttest2)
        self.Le_test3 = QLineEdit(txt_hinttest3)
        
        self.btn_test1 = QPushButton(txt_starttest1)
        self.btn_test2 = QPushButton(txt_starttest2)
        self.btn_test3 = QPushButton(txt_starttest3)
        self.btn_next = QPushButton(txt_sendresults)

        self.h_line = QHBoxLayout()
        self.v_line_l = QVBoxLayout()
        self.v_line_r = QVBoxLayout()

        self.v_line_l.addWidget(self.Lb_name, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.Le_name, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.Lb_age, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.Le_age, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.Lb_test1, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.btn_test1, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.Le_test1, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.Lb_test2, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.btn_test2, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.Lb_test3, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.btn_test3, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.Le_test2, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.Le_test3, alignment=Qt.AlignLeft)
        self.v_line_l.addWidget(self.btn_next, alignment=Qt.AlignCenter)
        
        self.v_line_r.addWidget(self.Lb_timer, alignment=Qt.AlignCenter)
        self.h_line.addLayout(self.v_line_l)
        self.h_line.addLayout(self.v_line_r)
        self.setLayout(self.h_line)

    def connects(self):
        self.btn_next.clicked.connect(self.next_window)
        self.btn_test1.clicked.connect(self.timer1)
        self.btn_test2.clicked.connect(self.timer2)
        self.btn_test3.clicked.connect(self.timer3)

    def next_window(self):
        self.hide()
        self.win_3 = ThirdWindow()

    def timer1(self):
        self.time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1_event)
        self.timer.start(1000)
    
    def timer1_event(self):
        self.time = self.time.addSecs(-1)
        self.Lb_timer.setText(self.time.toString('hh:mm:ss'))
        self.Lb_timer.setFont(QFont('Times', 36, QFont.Bold))
        self.Lb_timer.setStyleSheet('color: rgb(0,0,0);')
        if self.time.toString('hh:mm:ss') =='00:00:00':
            self.timer.stop()

    def timer2(self):
        self.time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2_event)
        self.timer.start(1500)
    
    def timer2_event(self):
        self.time = self.time.addSecs(-1)
        self.Lb_timer.setText(self.time.toString('hh:mm:ss')[6:8])
        self.Lb_timer.setFont(QFont('Times', 36, QFont.Bold))
        self.Lb_timer.setStyleSheet('color: rgb(0, 100, 0);')
        if self.time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer3(self):
        self.time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3_event)
        self.timer.start(1000)
    

    def timer3_event(self):
        self.time = self.time.addSecs(-1)
        self.Lb_timer.setText(self.time.toString('hh:mm:ss'))
        self.Lb_timer.setFont(QFont('Times', 36, QFont.Bold))
        if int(self.time.toString('hh:mm:ss')[6:8]) >= 45:
            self.Lb_timer.setStyleSheet('color: rgb(0, 200, 0);')
        elif int(self.time.toString('hh:mm:ss')[6:8]) <= 15:
            self.Lb_timer.setStyleSheet('color: rgb(0, 200, 0);')
        else:
            self.Lb_timer.setStyleSheet('color: rgb(0, 0, 0);')
        if self.time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()