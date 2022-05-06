# -*- coding: utf-8 -*-

"""
Module implementing ToggleMenu.
"""

from PyQt5.QtCore import pyqtSlot,  QPropertyAnimation,  QEasingCurve
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

from Ui_ToggleMenu import Ui_ToggleMenu


class ToggleMenu(QWidget, Ui_ToggleMenu):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(ToggleMenu, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_toggle_menu_clicked(self):
        """
        Slot documentation goes here.
        """
        width = self.frame_left_mepu.width()
        widthExtended = 155 if width == 70 else 70
        self.animation = QPropertyAnimation(self.frame_left_mepu,  b"minimumWidth")        
        self.animation.setDuration(400)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        # 惯性效果
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)   
        self.animation.start()
    
    @pyqtSlot()
    def on_pushButton_home_clicked(self):
        """
        Slot documentation goes here.
        """
        self.resetChecked()
        self.pushButton_home.setChecked(True)
        self.stackedWidget.setCurrentIndex(0)
    
    @pyqtSlot()
    def on_pushButton_setting_clicked(self):
        """
        Slot documentation goes here.
        """
        self.resetChecked()
        self.pushButton_setting.setChecked(True)
        self.stackedWidget.setCurrentIndex(2)
        
    def resetChecked(self):
        for btn in ['home', 'user', 'setting']:
            getattr(self, 'pushButton_{}'.format(btn)).setChecked(False)
    
    @pyqtSlot()
    def on_pushButton_user_clicked(self):
        """
        Slot documentation goes here.
        """
        self.resetChecked()
        self.pushButton_user.setChecked(True)
        self.stackedWidget.setCurrentIndex(1)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = ToggleMenu()
    ui.show()
    sys.exit(app.exec_())
