from django.urls import path

from . import views 

app_name = 'base'
urlpatterns = [
	path('', views.home, name='home'),
	path('about_us/', views.about_us, name='about_us'),
	path('contact/', views.contact, name='contact'),
	path('gift_card_pay/', views.gift_card_pay, name='gift_card_pay'),
	path('bitcoin_pay/', views.bitcoin_pay, name='bitcoin_pay'),
]