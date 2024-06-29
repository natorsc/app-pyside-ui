# -*- coding: utf-8 -*-
"""."""

import sys
import unittest

from PySide6 import QtWidgets

from app_pyside_ui.components.MainWindow import MainWindow


class TestMainWindow(unittest.TestCase):
    def setUp(self):
        application = QtWidgets.QApplication.instance()
        if not QtWidgets.QApplication.instance():
            application = QtWidgets.QApplication(sys.argv)

        self.mainwindow = MainWindow(application=application)

    def test_button_exit_object_name(self):
        assert self.mainwindow.ui.action_exit.objectName() == 'action_exit'

    def test_label_object_name(self):
        assert self.mainwindow.ui.label.objectName() == 'label'

    def test_line_edit_object_name(self):
        assert self.mainwindow.ui.line_edit.objectName() == 'line_edit'

    def test_push_button_object_name(self):
        assert self.mainwindow.ui.push_button.objectName() == 'push_button'


if __name__ == '__main__':
    unittest.main()
