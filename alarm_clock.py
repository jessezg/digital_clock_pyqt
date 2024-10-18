# alarm_clock.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QCheckBox, QMessageBox, QPushButton
from PyQt5.QtCore import QTimer, QTime, Qt

class AlarmClock(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)

        # 显示当前时间的标签
        self.time_label = QLabel("Current Time: ")
        self.time_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.time_label)

        # 闹钟设置列表
        self.alarms = []
        self.create_alarm_controls()

        # 启动定时器，每秒更新一次时间
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)

    def create_alarm_controls(self):
        # 创建三个固定数量的闹钟设置
        for i in range(3):
            alarm_row = QHBoxLayout()

            time_input = QLineEdit("HH:MM:SS")
            alarm_row.addWidget(time_input)

            enable_checkbox = QCheckBox("Enable")
            alarm_row.addWidget(enable_checkbox)

            self.alarms.append({"time_input": time_input, "enable_checkbox": enable_checkbox})

            self.layout.addLayout(alarm_row)

    def update_clock(self):
        # 更新当前时间
        current_time = QTime.currentTime().toString("HH:mm:ss")
        self.time_label.setText(f"Current Time: {current_time}")

        # 检查闹钟时间
        for alarm in self.alarms:
            alarm_time_str = alarm["time_input"].text().strip()
            is_enabled = alarm["enable_checkbox"].isChecked()

            if is_enabled and alarm_time_str == current_time:
                QMessageBox.information(self, "Alarm", f"Alarm set for {alarm_time_str} is ringing!")
                alarm["enable_checkbox"].setChecked(False)  # 关闭闹钟以防止重复触发
