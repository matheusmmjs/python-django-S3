from django.db import models

class Order(models.Model):  
  obs_text  = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

class OrderedItem(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  description_text = models.CharField(max_length=200)
  amount = models.IntegerField()
  price = models.IntegerField()