import pandas as pd
import random

random.seed(2021)

aisles = pd.read_csv('datasets/aisles.csv')
departments = pd.read_csv('datasets/departments.csv')
order_product_prior = pd.read_csv('datasets/order_products__prior.csv')
order_product_train = pd.read_csv('datasets/order_products__train.csv')
orders = pd.read_csv('datasets/orders.csv')
products = pd.read_csv('datasets/products.csv')



## ----------<데이터 전처리>----------
#결측치 확인 (null)
#print(orders.isna().sum())

# 결측치 처리('days_since_prior_order':첫 구매인경우 nan값이 입력되어 있음 => 0으로 대체)
orders['days_since_prior_order'] = orders['days_since_prior_order'].fillna(0)
orders = orders.dropna()

# 1만명의 유저만 샘플링
user = random.sample(orders['user_id'][orders['eval_set']=='train'].unique().tolist(), 10000)

# orders에서 test dataset 관련 기록(prior포함) 제외
orders_2 = orders[orders['user_id'].isin(user)]
print("유저 인원:",len(user), "// 주문건수 합:",len(orders_2))

# order_product_prior에서 test dataset 관련 기록 제외
order_product_prior = order_product_prior[order_product_prior['order_id'].isin(orders_2['order_id'])]


## ----------<데이터 조합>----------
# 제품 정보 : product + aisles + department data
product_m = products.merge(aisles).merge(departments)

# product one-hot encoding data
product_enc = pd.get_dummies(product_m, columns=['aisle'], prefix=[None])

#두 데이터셋을 수직으로 결합하기
order_product = pd.concat([order_product_prior,order_product_train])

# 주문 항목 정보 : product_m + order_product
order_detail = order_product.merge(product_m,how='left')

data = orders_2.merge(order_detail)
print(data)