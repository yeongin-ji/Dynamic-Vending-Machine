from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer, OrderSerializer, UserSerializer
from .models import Product, User, Orders
from rest_framework.renderers import JSONRenderer
from django_pandas.io import read_frame, is_values_queryset, to_fields
from rest_framework.views import APIView
from rest_framework.decorators import api_view
import pandas as pd
import re
from sklearn.metrics.pairwise import cosine_similarity
import random
import json
# Create your views here.

class ProductAPI(APIView):
    def get(self, request):
        products = Product.objects.all()
        df = read_frame(products)
        print(df)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class OrdersAPI(APIView):
    def get(self, request):
        orders = Orders.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserAPI(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class myAPI(APIView):

    def get(self, request):
        request_user_id = int(request.query_params['user_id'])

        orders = Orders.objects.all()
        products = Product.objects.all()
        orders_df = read_frame(orders)
        products_df = read_frame(products)

        i = 0
        for order in orders:
            orders_df.loc[i, 'product'] = order.product.product_id
            i += 1

        orders_detail = pd.merge(orders_df, products_df, left_on='product', right_on='product_id', how='left')
        orders_detail = orders_detail.drop(['product'], axis=1)
        print(orders_detail)

        data = orders_detail.pivot_table('rating', index='product_id', columns='user')
        data.fillna(0, inplace=True)
        print(data)

        item_based_collabor = cosine_similarity(data)
        print(item_based_collabor)

        item_based_collabor = pd.DataFrame(data= item_based_collabor, index= data.index, columns= data.index)
        print(item_based_collabor)

        user_like_list = self.get_user_like_list(request_user_id, orders_detail)
        print('user like: \n', user_like_list)

        recommend_list = self.get_recommend_list(item_based_collabor, user_like_list)
        print('recommend: ', recommend_list)

        recommend_serialized = self.recommend_serialize(recommend_list, products_df)
        print('recommend json: ', recommend_serialized)

        print('request: ', request_user_id)
        return Response(recommend_serialized)
    
    def get_recommend_list(self, collabor, product_ids):
        recommend_list = []
        for id in product_ids:
            tmps = collabor[id].sort_values(ascending=False)[:5].index.tolist()
            for tmp in tmps:
                recommend_list.append(tmp)
        recommend_distinct = list(set(recommend_list))
        if len(recommend_distinct) >= 5:
            recommend_sampled = random.sample(recommend_distinct, 8)
            return recommend_sampled
        else:
            return recommend_distinct
        
    def get_user_like_list(self, user_id, data):
        user_like_list = data['product_id'][(data['rating'] >= 3.5) & (data['user'] == user_id)].tolist()
        return user_like_list
    
    def recommend_serialize(self, list, products):
        recommend_serialized = []
        for item in list:
            recommend_serialized.append({
                'product_id' : item,
                'title' : products['title'][products['product_id']==item].tolist()[0]
            })
        recommend_serialized = {i : recommend_serialized[i] for i in range(len(recommend_serialized))}
        return recommend_serialized