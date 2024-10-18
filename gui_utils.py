# gui_utils.py
from PyQt5.QtWidgets import QMenuBar, QAction

def create_menu(main_window, show_alarm_clock, show_stopwatch, show_timer):
    # 创建菜单栏
    menu_bar = QMenuBar(main_window)
    main_window.setMenuBar(menu_bar)

    # 创建功能菜单
    function_menu = menu_bar.addMenu("Functions")

    # 添加菜单项
    alarm_action = QAction("Alarm Clock", main_window)
    alarm_action.triggered.connect(show_alarm_clock)
    function_menu.addAction(alarm_action)

    stopwatch_action = QAction("Stopwatch", main_window)
    stopwatch_action.triggered.connect(show_stopwatch)
    function_menu.addAction(stopwatch_action)

    timer_action = QAction("Timer", main_window)
    timer_action.triggered.connect(show_timer)
    function_menu.addAction(timer_action)
