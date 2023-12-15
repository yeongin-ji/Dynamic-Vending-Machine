from PyQt5.QtWidgets import *
import sys
from datetime import datetime
from PyQt5.QtCore import Qt
from Complete import CompleteWindow

class PaymentWindow(QMainWindow):
    def __init__(self, mainWindow, requestManager, product):
        super().__init__()
        self.main = mainWindow
        self.RM = requestManager
        self.product = product
        self.init_ui()

    def init_ui(self):
        # Create a button to switch back to the main window
        wid = QWidget()
        
        baseLabel = QLabel('------------PaymentInfo------------')
        baseLabel.setAlignment(Qt.AlignCenter)
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        timeLabel = QLabel(f'Timestamp: {formatted_time}')

        juiceName = self.product['title']
        nameLabel = QLabel(f'Product name: {juiceName}')

        self.country = self.main.country
        if self.country == 'Korea':
            self.price = self.product['price_kr']
            priceStr = str(self.price) + 'Won'
        elif self.country == 'US':
            self.price = self.product['price_us']
            priceStr = str(self.price) + 'Dollar'  
        elif self.country == 'Japan':
            self.price = self.product['price_jp']
            priceStr = str(self.price) + 'Yen'
        
        priceLabel = QLabel(f'Price: {priceStr}')

        stock = self.product['stock']
        stockLabel = QLabel(f'Remaining stock: {stock} / 5')

        splitLabel = QLabel('--------------UserInfo--------------')
        userNameLabel = QLabel(f'Payer: {self.main.name}')
        countryLabel = QLabel(f'User Country: {self.country}\n')
        welfareLabel = QLabel(f'Welfare status: {self.main.welfare}')

        moneyLabel = QLabel('Put the cash in')
        self.moneyLineEdit = QLineEdit()
        
        payBtn = QPushButton('Put')
        backBtn = QPushButton('Back')
        backBtn.clicked.connect(self.switch_to_main_window)
        payBtn.clicked.connect(self.paymentProcess)

        layout = QVBoxLayout()

        layout.addWidget(baseLabel)
        layout.addWidget(timeLabel)
        layout.addWidget(nameLabel)
        layout.addWidget(priceLabel)
        layout.addWidget(stockLabel)

        layout.addWidget(splitLabel)

        layout.addWidget(userNameLabel)
        layout.addWidget(countryLabel)
        layout.addWidget(welfareLabel)
        layout.addWidget(moneyLabel)
        layout.addWidget(self.moneyLineEdit)
        
        hbox = QHBoxLayout()
        hbox.addWidget(payBtn)
        hbox.addWidget(backBtn)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(layout)
        mainLayout.addLayout(hbox)


        wid.setLayout(mainLayout)
        self.setCentralWidget(wid)
        self.setWindowTitle('Payment view')    
        self.move(810, 300)             
        self.setFixedSize(300, 350)  
        self.show()

    def switch_to_main_window(self):
        self.hide()
        self.main.show()
        self.close()

    def switch_to_complete_window(self):
        self.hide()
        self.complete = CompleteWindow(self, self.RM, self.resultStr)
        self.complete.show()
        self.close()

    def paymentProcess(self):
        received_money = int(self.moneyLineEdit.text())
        product_price = self.price

        if self.country == 'Korea':
            coins = [10, 50, 100, 500]
            bills = [1000, 5000, 10000]
            currency_unit = "원"
            country_name = "한국"
            language = "한국어"
            change_phrase = "거스름돈"
            coins_phrase = "동전 개수"
            bills_phrase = "지폐 개수"
        elif self.country == 'US':
            coins = []  # 센트는 고려하지 않음
            bills = [1, 2, 5, 10, 20, 50, 100]
            currency_unit = "$"
            country_name = "US"
            language = "English"
            change_phrase = "change"
            coins_phrase = "number of coins"
            bills_phrase = "number of bills"
        elif self.country == 'Japan':
            coins = [1, 5, 10, 50, 100, 500]
            bills = [1000, 2000, 5000, 10000]
            currency_unit = "Yen"
            country_name = "Japan"
            language = "Japanese"
            change_phrase = "change"
            coins_phrase = "number of coins"
            bills_phrase = "number of bills"
        
        currency_list = coins + bills  # 동전과 지폐 모두 고려


        #할인 대상인지 체크
        if self.main.welfare == 'welfare':
            product_price *= 0.9  # 10% 할인 적용
            product_price = int(product_price)  # 정수로 변환하여 소수점 제거
        
        
        #Dynamic Programming 적용하여 잔돈 반환 계산
        change = received_money - product_price
        D = [-1] * (change + 1)
        D = [-1] * (change + 1)
        D[0] = 0
        used_currency = [[0] * len(currency_list) for _ in range(change + 1)]

        for d in range(1, change + 1):
            for idx, curr in enumerate(currency_list):
                if curr <= d:
                    if D[d - curr] != -1:
                        if D[d] == -1 or D[d - curr] + 1 < D[d]:
                            D[d] = D[d - curr] + 1
                            used_currency[d] = used_currency[d - curr].copy()
                            used_currency[d][idx] += 1

        min_coins_bills_used = used_currency[change]

        self.resultStr = []
        if self.country == 'Korea':
            self.resultStr.append(f"{country_name}에서 {change_phrase} {change}{currency_unit}을 만들기 위한 최소 {coins_phrase}/{bills_phrase}: {D[change]}")
        elif self.country == 'US':
            self.resultStr.append(f"Minimum {coins_phrase}/{bills_phrase} required to make {change}{currency_unit} as {change_phrase} in {country_name}: {D[change]}")
        elif self.country == 'Japan':
            self.resultStr.append(f"Minimum {coins_phrase}/{bills_phrase} required to make {change}{currency_unit} as {change_phrase} in {country_name}: {D[change]}")

        for idx, count in enumerate(min_coins_bills_used):
            if count > 0:
                if idx < len(coins):
                    if self.country == 'Korea':
                        self.resultStr.append(f"{coins[idx]}{currency_unit} {coins_phrase}: {count}")
                    elif self.country == 'Japan':
                        self.resultStr.append(f"{coins[idx]}{currency_unit} {coins_phrase}: {count}")
                    elif self.country == 'US':
                        self.resultStr.append(f"{coins[idx]}{currency_unit} {coins_phrase}: {count}")
                else:
                    if self.country == 'Korea':
                        self.resultStr.append(f"{bills[idx - len(coins)]}{currency_unit} {bills_phrase}: {count}")
                    elif self.country == 'Japan':
                        self.resultStr.append(f"{bills[idx - len(coins)]}{currency_unit} {bills_phrase}: {count}")
                    elif self.country == 'US':
                        self.resultStr.append(f"{bills[idx - len(coins)]}{currency_unit} {bills_phrase}: {count}")
                
        print(self.resultStr)
        self.switch_to_complete_window()

