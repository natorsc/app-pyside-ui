# -*- coding: utf-8 -*-
"""."""

from PySide6 import QtWidgets

try:
    from uic.Ui_MainWindow import Ui_MainWindow
except ModuleNotFoundError:
    from app_pyside_ui.uic.Ui_MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent=parent)
        self.application = kwargs.get('application')

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action_exit.triggered.connect(self.on_action_exit_clicked)
        self.ui.push_button.clicked.connect(self.on_push_button_clicked)

    def on_push_button_clicked(self, widget):
        text = self.ui.line_edit.text()
        if text.split():
            self.ui.label.setText(text)
        else:
            self.ui.label.setText(self.tr('Digite algo no campo de texto ;).'))

    def on_action_exit_clicked(self):
        self.application.quit()


if __name__ == '__main__':
    pass
