from PySide6.QtWidgets import (
    QWidget,
    QGridLayout,
    QLabel
)


class MainView(QWidget):
    def __init__(self, parent=None) -> None:
        super(MainView, self).__init__(parent)

        grid = QGridLayout()
        self.text = QLabel()
        grid.addChildWidget(self.text)

        self.setLayout(grid)
