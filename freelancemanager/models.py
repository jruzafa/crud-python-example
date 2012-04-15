from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=100)

class Client(models.Model):
	name = models.CharField(max_length=100)
	website = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	user = models.ForeignKey(User)

class Work(models.Model):
	name = models.CharField(max_length=100)
	amount = models.FloatField()
	init_date = models.DateTimeField()
	finish_date = models.DateTimeField()
	paid = models.BooleanField()
	client = models.ForeignKey(Client)
	user = models.ForeignKey(User)