from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import OfferSlider, homeBlockOffers, Products, Category, Collection, Offers
from .serializers import SliderOfferSerializer, HomeBlockOfferSerializer, ProductSerializer, CollectionSerializer, UserSerializer,OffersSerializer
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        token['email'] = user.email
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(('GET',))
def home(request):
    data = {
        'api-overview': '/',
        'register': 'register/',
        'token': 'token/',
        'refresh token': 'token/refresh/',
        'slider-offers': 'sliderOffers/',
        'home-offers': 'homeOffers/',
        'new-arrivals': 'newArrivals/',
        'collections': 'collections/',
        'products': 'products/<category-name>',
    }
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(('GET',))
def sliderOffers(request):
    offers = OfferSlider.objects.all()
    data = SliderOfferSerializer(offers, many=True).data
    return Response(data, status=status.HTTP_200_OK)


@api_view(('GET',))
def homeOffers(request):
    offers = homeBlockOffers.objects.all()
    data = HomeBlockOfferSerializer(offers, many=True).data
    print(offers)
    return Response(data, status=status.HTTP_200_OK)


@api_view(('GET',))
def products(request, cat):
    category = Category.objects.filter(categoryName__iexact=cat)
    category = category[0].id
    allProds = Products.objects.filter(category_id=category)
    data = ProductSerializer(allProds, many=True).data
    return Response(data, status=status.HTTP_200_OK)


@api_view(('GET',))
def newArrivals(request):
    allProds = Products.objects.all()
    new_arrivals = allProds.order_by('-dateAdded')
    data = ProductSerializer(new_arrivals, many=True).data
    return Response(data, status=status.HTTP_200_OK)


@api_view(('GET',))
def collections(request):
    allCollection = Collection.objects.all()
    allCollection = allCollection.filter(is_published=True)
    data = CollectionSerializer(allCollection, many=True).data
    return Response(data, status=status.HTTP_200_OK)


@api_view(('POST',))
def registerView(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = {
            'name': request.data['name']
        }
        return Response(data, status=status.HTTP_201_CREATED)
    return Response('data', status=status.HTTP_100_CONTINUE)


@api_view(('GET',))
def specificCollections(request, col):
    print(col)
    collection = Collection.objects.filter(collectionName__iexact=col)
    collection = collection[0].id
    allProds = Products.objects.all()
    allProds = allProds.filter(is_published=True)
    allProds = allProds.filter(collection=collection)
    data = ProductSerializer(allProds, many=True).data
    return Response(data, status=status.HTTP_200_OK)


@api_view(('GET',))
def allProducts(request):
    allProds = Products.objects.all()
    allProds = allProds.filter(is_published=True)
    data = ProductSerializer(allProds, many=True).data
    return Response(data, status=status.HTTP_200_OK)


@api_view(('GET',))
def product(request, id):
    allProds = Products.objects.all()
    allProds = allProds.filter(id=id)
    data = ProductSerializer(allProds, many=True).data
    return Response(data, status=status.HTTP_200_OK)


@api_view(('GET',))
def prodSearch(request, slug):
    allProds = Products.objects.all()
    allProds = allProds.filter(prodcutName__icontains=slug)
    data = ProductSerializer(allProds, many=True).data
    return Response(data, status=status.HTTP_200_OK)

@api_view(('GET',))
def homeProds(request):
    allProds = Products.objects.all()
    allProds = allProds.order_by('-dateAdded')[:13]
    data = ProductSerializer(allProds, many=True).data
    return Response(data, status=status.HTTP_200_OK)

@api_view(('GET',))
def offerProds(request):
    allProds = Products.objects.all()
    allProds = allProds.filter(is_in_offer=True)
    data = ProductSerializer(allProds, many=True).data
    return Response(data, status=status.HTTP_200_OK)



