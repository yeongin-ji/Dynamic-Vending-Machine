import sys
from PyQt5.QtWidgets import *
from RequestManager import RequestManager
from PyQt5.QtGui import QPixmap
from Signup import SignupWindow
from Login import LoginWindow
from Payment import PaymentWindow
from functools import partial

class DVM(QMainWindow):
    #메인 윈도우 생성자
    def __init__(self):
        super().__init__()  
        self.initUI()

        self.user_id = None
        self.name = 'Unknown'
        self.country = 'Korea'
        self.welfare = 'nonwelfare'


    def initUI(self):
        self.RM = RequestManager()
        mainFrame = QFrame()

        signupBtn = QPushButton('sign up')
        loginBtn = QPushButton('membership login')
        loginBtn.clicked.connect(self.loginBtnClicked)
        signupBtn.clicked.connect(self.signupBtnClicked)
        self.userInfoLabel = QLabel(f'Hello Guest  |  your country: Korea  |  isWelfare: Nonewelfare')


        #상단 회원가입/로그인 버튼 레이아웃
        hboxWidget = QWidget()
        hboxLayout = QHBoxLayout()
        hboxLayout.addWidget(signupBtn)      
        hboxLayout.addWidget(loginBtn)   
        hboxLayout.addStretch(3)
        hboxLayout.addWidget(self.userInfoLabel)
        hboxWidget.setLayout(hboxLayout)

        #음료 30개 배치하는 Grid레이아웃
        gridWidget = QWidget()
        grid = QGridLayout()
        self.products = self.RM.getProductList()
        self.juiceGridRenderer(grid, self.products)
        gridWidget.setLayout(grid)

        #Grid 레이아웃을 스크롤 가능하도록 감싸기
        gridScroll = QScrollArea()
        gridScroll.setWidget(gridWidget)

        # 수평 및 그리드 레이아웃을 결합하는 메인 레이아웃
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(hboxWidget)
        mainLayout.addWidget(gridScroll)

        # mainWindow에 mainWidget등록
        # mainWidget에 component가 달리는 구조
        mainFrame.setLayout(mainLayout)  
        self.setCentralWidget(mainFrame)    

        #main window 설정
        self.setWindowTitle('DVM Client')    
        self.move(610, 40)             
        self.setFixedSize(900, 900)    
        self.show()  

    #login 버튼 클릭시 실행되는 함수
    def loginBtnClicked(self):
        self.hide()
        self.loginWin = LoginWindow(self, self.RM)
        self.loginWin.show()
    
    #signup 버튼 클릭시 실행되는 함수
    def signupBtnClicked(self):
        self.hide()
        self.signupWin = SignupWindow(self)
        self.signupWin.show()

    def setUserInfo(self, user_id, name, country, welfare):
        self.user_id = user_id
        self.name = name
        self.country = country
        self.welfare = welfare
        # self.userRerender(name, country, welfare)
    
    def userRerender(self):
        print('user: ', self.user_id)
        print('name: ', self.name)
        print('country: ', self.country)
        print('iswelfare: ', self.welfare)
        self.userInfoLabel.setText(f'Hello {self.name}  |  your country: {self.country}  |  isWelfare: {self.welfare}')
    
    #자판기 각 셀에 대한 위젯을 반환
    #하나의 셀은 상단부터 이미지, title, 재고, 주문버튼으로 구성
    def getJuiceCell(self, item):
        cellFrame = QFrame()
        vbox = QVBoxLayout()

        #음료 이미지 불러오기
        imageUrl = 'images/coffee.png'
        juiceItemImage = QLabel()
        juiceItemImage.setPixmap(QPixmap(imageUrl))

        #제목 텍스트 위젯 만들기
        juiceTitle = item['title']
        juiceTitle = QLabel(juiceTitle)

        #가격 텍스트 위젯 만들기
        juicePrice = item['price_kr']
        juicePrice = QLabel(f'{juicePrice}')

        #재고 텍스트 위젯 만들기
        juiceStocks = item['stock']
        juiceStocks = QLabel(f'{juiceStocks} / 5')

        #주문 버튼 위젯 만들기
        orderBtn = QPushButton('order')
        orderBtn.clicked.connect(partial(self.orderBtnClicked, item['product_id']))

        #레이아웃에 붙이기
        vbox.addWidget(juiceItemImage)
        vbox.addWidget(juiceTitle)
        vbox.addWidget(juicePrice)
        vbox.addWidget(juiceStocks)
        vbox.addWidget(orderBtn)

        cellFrame.setLayout(vbox)
        cellFrame.setFixedSize(160, 220)
        cellFrame.setObjectName('Cell')     #styleSheet에서 사용할 이름 설정
        
        print('')
        #Cell이라는 이름을 가진 QFrame클래스만 스타일을 적용
        # cellFrame.setStyleSheet('''
        #     QFrame#Cell {
        #         color: blue;
        #         background-color: #87CEFA;
        #         border-style: dashed;
        #         border-width: 3px;
        #         border-color: #1E90FF
        #     }
        # ''')

        return cellFrame

    #30개의 자판기 셀을 메인 윈도우에 그리드를 통해 배치
    def juiceGridRenderer(self, grid, products):
        self.juiceCells = {}
        for i in range(6):
            for j in range(5):
                #print(f'i: {i}, j: {j}')
                #음료 순서대로 item에 할당
                juiceItem = products[i*5 + j]
                #해당 음료 정보에 맞게 셀 객체를 생성
                self.getJuiceCell(juiceItem)
                juiceCell = self.getJuiceCell(juiceItem)

                #각각의 셀 객체를 juiceCells 변수에 보관
                self.juiceCells[str(i*5+j+1)] = juiceCell
                grid.addWidget(juiceCell, i, j)
    
    def orderBtnClicked(self, id):
        print(f'clicked order: product id {id}')
        self.payment = PaymentWindow(self, self.RM, self.products[id-1])
        self.hide()
        self.payment.show()
                       

if __name__ == '__main__':          #이 모듈이 단독으로 실행되었을 때 발동
    app = QApplication(sys.argv)
    ex = DVM()                      #메인 윈도우 생성
    sys.exit(app.exec_())
