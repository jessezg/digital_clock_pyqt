# stopwatch.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton
from PyQt5.QtCore import QTimer,Qt

class Stopwatch(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)

        # 显示时间的标签
        self.time_label = QLabel("00:00:00")
        self.time_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.time_label)

        # 控制按钮
        self.buttons_layout = QHBoxLayout()
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start)
        self.buttons_layout.addWidget(self.start_button)

        self.pause_button = QPushButton("Pause")
        self.pause_button.clicked.connect(self.pause)
        self.buttons_layout.addWidget(self.pause_button)

        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset)
        self.buttons_layout.addWidget(self.reset_button)

        self.layout.addLayout(self.buttons_layout)

        # 定时器用于更新秒表时间
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.elapsed_time = 0

    def start(self):
        self.timer.start(1000)

    def pause(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.elapsed_time = 0
        self.update_display()

    def update_time(self):
        self.elapsed_time += 1
        self.update_display()

    def update_display(self):
        hours = self.elapsed_time // 3600
        minutes = (self.elapsed_time % 3600) // 60
        seconds = self.elapsed_time % 60
        self.time_label.setText(f"{hours:02}:{minutes:02}:{seconds:02}")
