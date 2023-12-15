from PyQt5.QtWidgets import *
import sys

class SignupWindow(QMainWindow):
    def __init__(self, mainWindow):
        super().__init__()
        self.main = mainWindow
        self.init_ui()

    def init_ui(self):
        # Create a button to switch back to the main window
        self.wid = QWidget()

        # 사용자 회원가입 폼 요소
        account_label = QLabel('Type your ID:')
        account_edit = QLineEdit(self)

        passwd_label = QLabel('Type your passwd:')
        passwd_edit = QLineEdit(self)
        passwd_edit.setEchoMode(QLineEdit.Password)

        passwd_confirm_label = QLabel('Passwd confirm:')
        passwd_confirm_edit = QLineEdit(self)
        passwd_confirm_edit.setEchoMode(QLineEdit.Password)

        # 제출 버튼을 추가
        submit_button = QPushButton('submit', self)
        submit_button.clicked.connect(self.submit)

        # 이전 창으로 돌아가는 버튼 추가
        back_button = QPushButton('go back', self)
        back_button.clicked.connect(self.back_to_prev_window)

        # 회원가입 폼을 위한 레이아웃
        form_layout = QVBoxLayout()
        form_layout.addWidget(account_label)
        form_layout.addWidget(account_edit)
        form_layout.addWidget(passwd_label)
        form_layout.addWidget(passwd_edit)
        form_layout.addWidget(passwd_confirm_label)
        form_layout.addWidget(passwd_confirm_edit)

        # 하단의 버튼을 위한 레이아웃
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(back_button)
        btn_layout.addWidget(submit_button)

        # 메인 레이아웃 설정
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(btn_layout)

        self.wid.setLayout(main_layout)

        self.setCentralWidget(self.wid)
        self.setWindowTitle('User Signup')    
        self.move(810, 300)             
        self.setFixedSize(300, 300)  
        self.show()

    def back_to_prev_window(self):
        self.hide()
        self.main.show()

    def submit():
        pass