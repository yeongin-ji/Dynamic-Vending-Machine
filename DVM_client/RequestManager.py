import requests
import json

class RequestManager:
    baseUrl = 'http://127.0.0.1:8000/'

    def getProductList(self):
        try:
            response = requests.get(self.baseUrl+'products/')
            if response.status_code == 200:
                data = json.loads(response.text)
                return data
            else:
                print('request failed: code ', response.status_code)
                return response.status_code
        except requests.RequestException as e:
            print('error occured: ', e)
            return e

    def getUserList(self):
        try:
            response = requests.get(self.baseUrl+'users/')
            if response.status_code == 200:
                data = json.loads(response.text)
                return data
            else:
                print('request failed: code ', response.status_code)
                return response.status_code
        except requests.RequestException as e:
            print('error occured: ', e)
            return e

    def getRecommendList(self, user_id):
        try:
            response = requests.get(self.baseUrl+f'my/?user_id={user_id}')
            if response.status_code == 200:
                data = json.loads(response.text)
                return data
            else:
                print('request failed: code ', response.status_code)
                return response.status_code
        except requests.RequestException as e:
            print('error occured: ', e)
            return e

    def requestPayment(self):
        pass

    def updateStocks(self):
        pass

    def addUser(self):
        pass

    def addOrder(self):
        pass

