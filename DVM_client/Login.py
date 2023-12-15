from PyQt5.QtWidgets import *
import sys

class LoginWindow(QMainWindow):
    def __init__(self, mainWindow, requestManager):
        super().__init__()
        self.main = mainWindow
        self.RM = requestManager
        self.init_ui()

    def init_ui(self):
        # Create a button to switch back to the main window
        self.wid = QWidget()
        
        # 사용자 회원가입 폼 요소
        account_label = QLabel('Type your ID:')
        self.account_edit = QLineEdit(self)

        passwd_label = QLabel('Type your passwd:')
        self.passwd_edit = QLineEdit(self)
        self.passwd_edit.setEchoMode(QLineEdit.Password)

        # 제출 버튼을 추가
        submit_button = QPushButton('submit', self)
        submit_button.clicked.connect(self.submit)

        # 이전 창으로 돌아가는 버튼 추가
        back_button = QPushButton('go back', self)
        back_button.clicked.connect(self.back_to_prev_window)

        # 회원가입 폼을 위한 레이아웃
        form_layout = QVBoxLayout()
        form_layout.addWidget(account_label)
        form_layout.addWidget(self.account_edit)
        form_layout.addWidget(passwd_label)
        form_layout.addWidget(self.passwd_edit)

        # 하단의 버튼을 위한 레이아웃
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(back_button)
        btn_layout.addWidget(submit_button)

        # 메인 레이아웃 설정
        main_layout = QVBoxLayout()
        main_layout.addStretch(1)
        main_layout.addLayout(form_layout)
        main_layout.addStretch(1)
        main_layout.addLayout(btn_layout)
        self.wid.setLayout(main_layout)

        self.setCentralWidget(self.wid)
        self.setWindowTitle('User Login')    
        self.move(810, 300)             
        self.setFixedSize(300, 300)  
        self.show()

    def back_to_prev_window(self):
        self.hide()
        self.main.show()
        self.close()

    def submit(self):
        input_account = int(self.account_edit.text())
        input_passwd = self.passwd_edit.text()
        users = self.RM.getUserList()
        
        #로그인 성공 여부 판단
        user_correct_flag = 0
        pw_correct_flag = 0
        for each_user in users:
            if input_account == each_user['user_id']:
                user_correct_flag += 1
                if input_passwd == each_user['passwd']:
                    pw_correct_flag += 1
                    self.main.setUserInfo(each_user['user_id'], each_user['name'], each_user['country'], each_user['welfare'])
                    self.user_id = each_user['user_id']
        
        #로그인 성공 여부에 따른 알림창 띄우기
        if user_correct_flag == 1:
            if pw_correct_flag == 0:
                QMessageBox.warning(self, 'Warning', 'Password Incorrect', QMessageBox.Ok)  
            else:
                QMessageBox.information(self, 'success!', 'user login success', QMessageBox.Ok)
                self.hide()
                self.main.userRerender()

                recommendList = self.RM.getRecommendList(self.user_id)
                print('recommend: ', recommendList)
                print('recommend_each: ', recommendList['0'], recommendList[str(0)]['product_id'])
                new_recommendList = []
                for i in range(len(recommendList)):
                    new_recommendList.append(recommendList[str(i)]['product_id'])
                print('new_recommend list: ', new_recommendList)
                print('juice cells: ', self.main.juiceCells)

                for i in range(len(self.main.juiceCells)):
                    if (i+1) in new_recommendList:
                        self.main.juiceCells[str(i+1)].setStyleSheet('''
                                QFrame#Cell {
                                color: blue;
                                background-color: #87CEFA;
                                border-style: dashed;
                                border-width: 3px;
                                border-color: #1E90FF
                            }
                        ''')
                    # childrens = self.main.juiceCells[str(i+1)].children()
                    # childrens[3].setText('hello')

                self.main.show()
                self.close()
        else:
            QMessageBox.warning(self, 'Warning', 'User not found', QMessageBox.Ok)

    def getUserInfo(self):
        return self.user_info