# This code is a simple calculator GUI using PyQt5.
# It creates a window with the title "Calculator" and a size of 256x256 pixels.

import sys
from ui import View
from ctrl import Control
from PyQt5.QtWidgets import QApplication # type: ignore

def main():
#    calc = QApplication(sys.argv)
    app= QApplication(sys.argv)  # QApplication 객체 생성
    view = View()
    Control(view=view)  # Control 객체 생성
    sys.exit(app.exec_())
   
if __name__ == '__main__':  #   This is the main entry point of the program.
    main()  # Call the main function to run the application.

