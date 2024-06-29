# -*- coding: utf-8 -*-
"""."""

import locale
import sys
from ctypes import windll

from PySide6 import QtCore, QtGui, QtWidgets

try:
    from components.MainWindow import MainWindow
except ModuleNotFoundError:
    from app_pyside_ui.components.MainWindow import MainWindow


def main() -> None:
    APPLICATION_NAME = 'br.com.justcode.Qt'
    ORGANIZATION_NAME = APPLICATION_NAME.split('.')[2]
    ORGANIZATION_DOMAIN = '.'.join(APPLICATION_NAME.split('.')[0:3])

    application = QtWidgets.QApplication(sys.argv)
    application.setOrganizationName(ORGANIZATION_NAME)
    application.setOrganizationDomain(ORGANIZATION_DOMAIN)
    application.setApplicationName(APPLICATION_NAME)
    application.setDesktopFileName(APPLICATION_NAME)
    application.setWindowIcon(QtGui.QIcon(':/icons/br.com.justcode.Qt'))

    loc, _ = locale.getlocale()
    translator = QtCore.QTranslator(application)
    if translator.load(QtCore.QLocale(loc), APPLICATION_NAME, '.', ':/i18n'):
        application.installTranslator(translator)

    if QtCore.QSysInfo.productType() == 'windows':
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            APPLICATION_NAME,
        )

    window = MainWindow(application=application)
    window.show()

    sys.exit(application.exec())


if __name__ == '__main__':
    main()
