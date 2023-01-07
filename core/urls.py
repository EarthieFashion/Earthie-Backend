from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('', views.home, name="home"),
    path('sliderOffers/', views.sliderOffers, name="sliderOffers"),
    path('homeOffers/', views.homeOffers, name="homeOffers"),
    path('homeProds/', views.homeProds, name="homeProds"),
    path('newArrivals/', views.newArrivals, name="newArrivals"),
    path('collections/', views.collections, name="collections"),
    path('collections/<str:col>/',views.specificCollections, name="products"),
    path('products/<str:cat>/',views.products, name="products"),
    path('product/<str:id>/',views.product, name="products"),
    path('products/',views.allProducts, name="products"),
    path('productSearch/<str:slug>/',views.prodSearch, name="products"),
    path('register/', views.registerView, name="register" ),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
