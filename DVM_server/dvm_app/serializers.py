from rest_framework import serializers
from .models import Product, Orders, User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product #모델 설정
        fields = ('product_id', 'title', 'stock', 'price_kr', 'price_us', 'price_jp') #필드 설정

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User #모델 설정
        fields = ('user_id', 'passwd', 'name', 'age', 'country', 'welfare') #필드 설정

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders #모델 설정
        fields = ('user', 'product', 'rating') #필드 설정