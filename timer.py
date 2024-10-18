# timer.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import QTimer,Qt

class Timer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)

        # 倒计时显示
        self.time_label = QLabel("00:00")
        self.time_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.time_label)

        # 输入框用于设置分钟和秒数
        input_layout = QHBoxLayout()
        self.minutes_input = QLineEdit("Minutes")
        input_layout.addWidget(self.minutes_input)

        self.seconds_input = QLineEdit("Seconds")
        input_layout.addWidget(self.seconds_input)

        self.layout.addLayout(input_layout)

        # 控制按钮
        button_layout = QHBoxLayout()
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start)
        button_layout.addWidget(self.start_button)

        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset)
        button_layout.addWidget(self.reset_button)

        self.layout.addLayout(button_layout)

        # 定时器用于倒计时
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.time_left = 0

    def start(self):
        try:
            minutes = int(self.minutes_input.text())
            seconds = int(self.seconds_input.text())
            self.time_left = minutes * 60 + seconds
            self.update_display()
            self.timer.start(1000)
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter valid numbers for minutes and seconds.")

    def reset(self):
        self.timer.stop()
        self.time_left = 0
        self.update_display()

    def update_time(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.update_display()
        else:
            self.timer.stop()
            QMessageBox.information(self, "Time's Up", "The countdown has finished!")

    def update_display(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        self.time_label.setText(f"{minutes:02}:{seconds:02}")
