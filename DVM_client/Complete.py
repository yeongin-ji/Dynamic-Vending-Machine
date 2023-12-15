from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import Qt

class CompleteWindow(QMainWindow):
    def __init__(self, paymentWindow, requestManager, resultStr):
        super().__init__()
        self.payment = paymentWindow
        self.RM = requestManager
        self.resultStr = resultStr
        self.init_ui()

    def init_ui(self):
        # Create a button to switch back to the main window
        wid = QWidget()
        
        completeLabel = QLabel('--------Enjoy Drink!--------')
        completeLabel.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()

        for res in self.resultStr:
            tmpLabel = QLabel(res)
            layout.addWidget(tmpLabel)

        returnBtn = QPushButton('Exit')
        returnBtn.clicked.connect(self.return_menu)

        layout.addWidget(returnBtn)
        
        wid.setLayout(layout)
        self.setCentralWidget(wid)
        self.setWindowTitle('Complete')    
        self.move(610, 300)             
        self.setFixedSize(700, 200)  
        self.show()

    def switch_to_main_window(self):
        self.hide()
        self.main.show()
        self.close()
    
    def return_menu(self):
        # self.hide()
        # dvm = DVM()
        # dvm.show()
        self.close()