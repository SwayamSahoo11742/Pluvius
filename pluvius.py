from PyQt5.QtWidgets import (
    QLabel,
    QListWidget,
    QMenuBar,
    QMainWindow,
    QApplication,
    QFileDialog,
    QListWidgetItem,
    QAbstractItemView,
    QProgressBar,
)
import random
import time
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtGui import QPixmap, QIcon, QPdfWriter, QPainter, QBrush, QColor, QFont
from PyQt5.uic import loadUi
from PyQt5.QtCore import QSize, QSizeF, Qt
from PyUI.editUI import EditUI
from PyUI.errorUI import ErrorUI
import sys
from Scopul import Scopul, config_musescore
from PyPDF2 import PdfWriter, PdfReader
from utils import pdf2jpg
import sqlite3
import os
from music21 import converter, environment, musicxml
import shutil

env = environment.Environment()
env[
    "musicxmlPath"
] = "C:/Users/user/Desktop/Projects/Scopul-Package/MuseScore4/bin/MuseScore4.exe"
env[
    "musescoreDirectPNGPath"
] = "C:/Users/user/Desktop/Projects/Scopul-Package/MuseScore4/bin/MuseScore4.exe"

config_musescore(
    "C:/Users/user/Desktop/Projects/Scopul-Package/MuseScore4/bin/MuseScore4.exe"
)


class EditMenu(QMainWindow):
    def __init__(self):
        super(EditMenu, self).__init__()
        self.ui = EditUI()
        self.ui.setupUi(self)

        # Page list customizations
        self.ui.page_list.setIconSize(QSize(230, 230))
        self.ui.page_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.page_list.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.ui.page_list.itemClicked.connect(self.switch_page)

        page_title = QListWidgetItem("Pages")
        font = QFont()
        font.setPointSize(16)
        page_title.setFont(font)
        page_title.setTextAlignment(Qt.AlignHCenter)
        page_title.setBackground(QBrush(QColor("#19212d")))
        self.ui.page_list.addItem(page_title)

        # New File
        self.ui.actionNew_File.triggered.connect(self.file_add)

    # New file action
    def file_add(self):
        fname, _ = QFileDialog.getOpenFileName(
            self, "Open MIDI", "", "MIDI files (*.mid)"
        )

        if fname:
            # Clearing sheets
            self.ui.page_list.clear()
            self.ui.main_view.clear()

            # Adding page title
            page_title = QListWidgetItem("Pages")
            font = QFont()
            font.setPointSize(16)
            page_title.setFont(font)
            page_title.setTextAlignment(Qt.AlignHCenter)
            page_title.setBackground(QBrush(QColor("#19212d")))
            self.ui.page_list.addItem(page_title)

            # Progress bar
            self.ui.progress_bar.show()
            QApplication.processEvents()

            if self.create_sheets(fname) == 0:
                return
            self.render_page_list()
            self.switch_page(self.ui.page_list.item(0))
            # self.render_main_view(self.get_latest_id())

    def render_page_list(self):
        for i in range(len(os.listdir(f"reports/sheets"))):
            # Adding the image
            sheet = QListWidgetItem(f"{i+1}")
            sheet.setTextAlignment(Qt.AlignCenter)
            font = QFont()
            font.setPointSize(16)
            sheet.setFont(font)
            sheet_icon = QIcon(f"reports/sheets/pluv-{i + 1}.jpg")
            sheet.setIcon(sheet_icon)

            if i % 2:
                sheet.setBackground(QBrush(QColor("#19212d")))

            self.ui.page_list.addItem(sheet)
            self.switch_page(self.ui.page_list.item(1))
        

    def create_sheets(self, f):
        loading_increments = [random.randint(12, 20) for _ in range(5)]
        loading_increments[-1] += 100 - sum(loading_increments)
        # Calculate prefix sum
        load_times = [
            sum(loading_increments[: i + 1]) for i in range(len(loading_increments))
        ]

        try:
            # Update progress bar (1st time)
            self.ui.progress_bar.setValue(load_times[0])

            Scopul(f).generate_pdf(fp=f"reports/pdf/pluv.pdf", overwrite=True)
        except Exception as e:
            # Error box
            error = ErrorUI("Curropted file", repr(e))
            error.exec_()
            return 0

        for filename in os.listdir("reports/sheets"):
            os.remove(os.path.join("reports/sheets", filename))

        # Update progress bar (2nd time)
        self.ui.progress_bar.setValue(load_times[1])

        pdf2jpg(
            f"reports/pdf/pluv.pdf",
            f"reports/sheets",
            "pluv",
            self.ui.progress_bar,
            load_times,
        )
        self.ui.progress_bar.hide()

    def switch_page(self, item: QListWidgetItem):
        # Get the index of the selected item
        index = self.ui.page_list.indexFromItem(item).row()

        # Extract the page number from the corresponding label item
        page_number_item = self.ui.page_list.item(index)
        try:
            page_number = int(page_number_item.text())
        except ValueError:
            return

        # Do something with the page number
        self.ui.main_view.setPixmap(
            QPixmap(f"reports/sheets/pluv-{page_number}.jpg").scaled(
                QSize(680, 880), Qt.KeepAspectRatio
            )
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    edit_window = EditMenu()
    edit_window.show()  # show the main window
    sys.exit(app.exec_())
