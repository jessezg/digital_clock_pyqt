# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QVBoxLayout, QWidget, QHBoxLayout, QPushButton
from alarm_clock import AlarmClock
from stopwatch import Stopwatch
from timer import Timer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Digital Clock Application")
        self.setGeometry(100, 100, 600, 500)

        # 主窗口的中心小部件
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # 创建堆叠小部件，用于切换不同的功能页面
        self.stack = QStackedWidget()
        main_layout.addWidget(self.stack)

        # 初始化各个功能模块
        self.alarm_clock = AlarmClock()
        self.stopwatch = Stopwatch()
        self.timer = Timer()

        # 将功能模块添加到堆叠小部件中
        self.stack.addWidget(self.alarm_clock)
        self.stack.addWidget(self.stopwatch)
        self.stack.addWidget(self.timer)

        # 创建底部按钮，用于切换各个功能
        button_layout = QHBoxLayout()
        alarm_button = QPushButton("Alarm Clock")
        alarm_button.clicked.connect(self.show_alarm_clock)
        button_layout.addWidget(alarm_button)

        stopwatch_button = QPushButton("Stopwatch")
        stopwatch_button.clicked.connect(self.show_stopwatch)
        button_layout.addWidget(stopwatch_button)

        timer_button = QPushButton("Timer")
        timer_button.clicked.connect(self.show_timer)
        button_layout.addWidget(timer_button)

        # 将按钮布局添加到主布局中
        main_layout.addLayout(button_layout)

        # 默认显示闹钟功能
        self.show_alarm_clock()

        # 设置样式
        self.set_style()

    def show_alarm_clock(self):
        self.stack.setCurrentWidget(self.alarm_clock)

    def show_stopwatch(self):
        self.stack.setCurrentWidget(self.stopwatch)

    def show_timer(self):
        self.stack.setCurrentWidget(self.timer)

    def set_style(self):
        # QSS样式表设置
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QPushButton {
                font-size: 16px;
                padding: 8px;
                border-radius: 5px;
                background-color: #4CAF50;
                color: white;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QLabel {
                font-size: 20px;
            }
            QLineEdit {
                font-size: 16px;
                padding: 4px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            QCheckBox {
                font-size: 16px;
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
