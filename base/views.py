from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .models import GiftCard

# Create your views here.
def home(request):
	return render(request, 'base/index.html', {})


def about_us(request):
	return render(request, 'base/about_us.html', {})


def contact(request):
	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']
		print(name,email,message)

		send_mail(
			name + ' ' + '['+email+']',
			message,
			'okoke@u.com',
			['okafor@a.com'],
			fail_silently=False)

		return redirect('/')
	else:		
		return render(request, 'base/index.html', {})

def gift_card_pay(request):
	if request.method == "POST" or request.method == 'FILES':
		name = request.POST['name']
		email = request.POST['email']
		card_type = request.POST['type']
		amount = request.POST['amount']
		card_pin = request.POST['pin']
		img = request.FILES.get('image', False)

		GiftCard.objects.create(name=name, email=email,card_type=card_type,
								card_amount=amount, card_pin=card_pin, image=img)
		# return redirect('/')

		context = {'name':name, 'amount':amount, 'email':email, 'card_pin':card_pin}
		return render(request, 'base/gift_card_pay.html', context)
		
		# message = request.POST['message']
	return render(request, 'base/gift_card_pay.html')

def bitcoin_pay(request):
	bitcoin_address = '325e9UjdJehojDKSKusVNopi97BJYhNkfE'

	context = {'bitcon':bitcoin_address}
	return render(request, 'base/bitcoin_pay.html', context )