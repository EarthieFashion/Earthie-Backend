from rest_framework import serializers
from .models import OfferSlider, homeBlockOffers, Products, Category, Collection, User

class SliderOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferSlider
        fields = '__all__'

class HomeBlockOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = homeBlockOffers
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Products
        fields = '__all__'
        # exclude = 'category'

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','email','phone','password']

    def save(self):
        account = User(
            email = self.validated_data['email'],
            name = self.validated_data['name'],
            phone = self.validated_data['phone']
        )
        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        return account