#!/usr/bin/env python3
"""Secure Encryption and Transfer Tool."""

import logging
import sys

from sett.gui.component import is_macos, MACOS_TOOLTIP_BG_COLOR
from . import main_window
from .pyside import QtWidgets, QtGui
from .resources import rc_icons
from ..utils.log import log_to_rotating_file


def run():
    application = QtWidgets.QApplication(sys.argv)
    if is_macos():
        palette = application.palette()
        palette.setColor(QtGui.QPalette.ColorRole.ToolTipBase, MACOS_TOOLTIP_BG_COLOR)
        application.setPalette(palette)
    window = main_window.MainWindow()
    log_to_rotating_file(
        log_dir=window.app_data.config.log_dir,
        file_max_number=window.app_data.config.log_max_file_number,
    )
    window.show()
    return application.exec_()


if __name__ == "__main__":
    run()
