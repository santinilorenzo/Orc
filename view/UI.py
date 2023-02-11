from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMainWindow, QHeaderView


class UI:

    def render(self, headers):
        x = headers.values()
        rows = 0
        for i, v in enumerate(x):
            rows += len(v)

        app = QApplication([])

        window = QMainWindow()
        window.setWindowTitle('Orc')
        window.setWindowIcon(QIcon('../logo/orc.png'))
        window.setGeometry(100, 100, 2000, 1500)
        window.setWindowIcon(QIcon('../logo/orc.png'))
        table_widget = QTableWidget(window)
        window.setCentralWidget(table_widget)

        table_widget.setColumnCount(2)
        table_widget.setRowCount(rows)
        horizontal_header = table_widget.horizontalHeader()
        vertical_header = table_widget.verticalHeader()
        horizontal_header.setVisible(False)
        horizontal_header.setSectionResizeMode(QHeaderView.ResizeToContents)
        vertical_header.setVisible(False)

        r = 0
        for horizontal_header, values in headers.items():
            table_widget.setItem(r, 0, QTableWidgetItem(horizontal_header))
            for value in values:
                table_widget.setItem(r, 1, QTableWidgetItem(value))
                r += 1

        window.show()
        app.exec()
