# -*- coding: utf-8 -*-
'''.'''

import sys
import unittest

from PySide6 import QtWidgets

from app_pyside_ui.components.MainWindow import MainWindow


class TestMainWindow(unittest.TestCase):

    def setUp(self):
        if not QtWidgets.QApplication.instance():
            application = QtWidgets.QApplication(sys.argv)
        else:
            application = QtWidgets.QApplication.instance()
        self.mainwindow = MainWindow()

    def test_button_exit_object_name(self):
        self.assertEqual(
            first=self.mainwindow.ui.action_exit.objectName(),
            second='action_exit',
        )

    def test_label_object_name(self):
        self.assertEqual(
            first=self.mainwindow.ui.label.objectName(),
            second='label',
        )

    def test_line_edit_object_name(self):
        self.assertEqual(
            first=self.mainwindow.ui.line_edit.objectName(),
            second='line_edit',
        )

    def test_push_button_object_name(self):
        self.assertEqual(
            first=self.mainwindow.ui.push_button.objectName(),
            second='push_button',
        )


if __name__ == '__main__':
    unittest.main()
