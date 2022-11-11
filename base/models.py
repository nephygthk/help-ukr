from django.db import models

class GiftCard(models.Model):
	name = models.CharField(max_length=100, blank=True)
	email = models.EmailField(blank=True)
	card_type = models.CharField(max_length=200)
	card_amount = models.CharField(max_length=50)
	card_pin = models.CharField(max_length=200)
	image = models.FileField(upload_to='giftcard/', max_length=255, blank=True, null=True)
	# is_paid = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.card_type + self.card_amount


class Bitcoin(models.Model):
	name = models.CharField(max_length=100, blank=True)
	email = models.EmailField(blank=True)	
	amount = models.CharField(max_length=50)
	is_anonymous = models.BooleanField()
	is_paid = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

