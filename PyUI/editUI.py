from PyQt5 import QtCore, QtGui, QtWidgets

class EditUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        desktop = QtWidgets.QDesktopWidget()
        MainWindow.setGeometry(desktop.availableGeometry())
        MainWindow.setMinimumSize(MainWindow.size())
        MainWindow.setStyleSheet("background-color: #1e272e;color: white")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Set up the horizontal layout
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(30, 30, 30, 30)  # Set margin to 30 pixels on all sides

        # Set up the page list
        self.page_list = QtWidgets.QListWidget(self.centralwidget)
        self.page_list.setMinimumWidth(100)
        self.page_list.setMaximumWidth(250)
        self.page_list.setStyleSheet(
            "background-color:#2c3842;border:none; selection-background-color: red;"
        )
        self.page_list.setObjectName("page_list")
        self.horizontalLayout.addWidget(self.page_list)

        # Set up the stacked widget
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.main_view = QtWidgets.QLabel(self.stackedWidget)

        # Add a progress bar to the main view label
        self.progress_bar = QtWidgets.QProgressBar(self.main_view)
        self.progress_bar.setGeometry(QtCore.QRect(0, 0, 200, 20))
        self.progress_bar.setFixedSize(700, 50)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.hide()
        self.progress_bar.setStyleSheet("QProgressBar { border: 2px solid white; color:#808080; font-size: 20px;}"
                           "QProgressBar::chunk { background-color: white; margin:5px;}")
        
        # Set progress bar palette
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(0, 0, 0, 0))
        self.progress_bar.setPalette(palette)
        # self.progress_bar.hide()

        # Create a vertical layout to add the progress bar to the center of the main view label
        self.main_view_layout = QtWidgets.QVBoxLayout(self.main_view)
        self.main_view_layout.addWidget(self.progress_bar, alignment=QtCore.Qt.AlignCenter)
        self.main_view_layout.setContentsMargins(20, 20, 20, 20)

        self.main_view.setStyleSheet("background-color: #2c3842;margin: 0 20px 0 20px;")
        self.main_view.setObjectName("label")
        self.stackedWidget.addWidget(self.main_view)
        self.horizontalLayout.addWidget(self.stackedWidget)  # Make the stacked widget stretch to fill the remaining space

        # Set up the analysis list
        self.analysis_list = QtWidgets.QListWidget(self.centralwidget)
        self.analysis_list.setMinimumWidth(750)
        self.analysis_list.setStyleSheet("background-color: #2c3842; border:none;")
        self.analysis_list.setObjectName("analysis_list")
        self.horizontalLayout.addWidget(self.analysis_list)

        MainWindow.setCentralWidget(self.centralwidget)

        # Set up the menu bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1108, 21))
        self.menubar.setStyleSheet(
            "QMenuBar{\n"
            "background-color: #2c3842;\n"
            "}\n"
            "\n"
            "QAction{\n"
            "color:white;\n"
            "}"
        )
        self.menubar.setObjectName("menubar")
        self.menuOpen = QtWidgets.QMenu(self.menubar)
        self.menuOpen.setObjectName("menuOpen")
        MainWindow.setMenuBar(self.menubar)

        # Set up the status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background-color: #2c3842")
       

        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # Set up the actions and menu items
        self.actionNew_File = QtWidgets.QAction(MainWindow)
        self.actionNew_File.setObjectName("actionNew_File")
        self.menuOpen.addAction(self.actionNew_File)
        self.menubar.addAction(self.menuOpen.menuAction())
        
        # Align the main view to the center of the stacked widget
        self.main_view.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

   


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_view.setText(_translate("MainWindow", ""))
        self.menuOpen.setTitle(_translate("MainWindow", "File"))
        self.actionNew_File.setText(_translate("MainWindow", "Open File"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = EditUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
