from PyQt5.QtWidgets import QApplication, QMessageBox


class ErrorUI(QMessageBox):
    def __init__(self, message, detail):
        super().__init__()
        self.setWindowTitle("Error")
        self.setText(message)
        self.setDetailedText(detail)
        self.setIcon(QMessageBox.Critical)
        self.setStandardButtons(QMessageBox.Ok)


if __name__ == "__main__":
    app = QApplication([])
    ErrorUI("P").exec_()
