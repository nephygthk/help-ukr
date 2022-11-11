from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .models import GiftCard, CoinPay

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

	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		amount = request.POST['amount']
		is_anony = request.POST.get('anony')

		print(is_anony)


		coinpay = CoinPay.objects.create(name=name, email=email, amount=amount,
										 is_anonymous=False, coin_type='Bitcoin')

		if is_anony == 'one':
			coinpay.is_anonymous=True
			coinpay.save()

		context = {'amount':amount, 'name':name, 'email':email}
		return render(request, 'base/bitcoin_pay.html', context )

		

	context = {'bitcon':bitcoin_address}
	return render(request, 'base/bitcoin_pay.html', context )

def etherium_pay(request):
	etherium_address = '0xd91d307d27b3144a9fb590098053291c71e17fb4'

	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		amount = request.POST['amount']
		is_anony = request.POST.get('anony')

		print(is_anony)


		coinpay = CoinPay.objects.create(name=name, email=email, amount=amount,
										 is_anonymous=False, coin_type='Etherium')

		if is_anony == 'one':
			coinpay.is_anonymous=True
			coinpay.save()

		context = {'amount':amount, 'name':name, 'email':email}
		return render(request, 'base/bitcoin_pay.html', context )

	context = {'etherium':etherium_address}
	return render(request, 'base/etherium_pay.html', context )