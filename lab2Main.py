from PyQt6.QtWidgets import QApplication
from lab2Logic import *

def main():
    '''
    main function, pulls up the Lab 2 (Grading) GUI
    '''
    application = QApplication([])
    window = Lab2Logic()
    window.show()
    application.exec()

if __name__ == '__main__':
    main()