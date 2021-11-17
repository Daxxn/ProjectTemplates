from PySide6.QtWidgets import QApplication
from views.mainView import MainView
import sys


def main() -> None:
    print('Template App')
    app = QApplication(sys.argv)

    try:
        mainView = MainView()
        mainView.show()
        status = app.exec()
        sys.exit(status)
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
else:
    print('File is not a module.')
