from django.db import models

# Create your models here.
class Category(models.Model):
    C_name=models.CharField(max_length=200)
    def __str__(self):
        return self.C_name
class Product(models.Model):
    x=models.ForeignKey(Category,on_delete=models.CASCADE)
    P_name=models.CharField(max_length=200)
    P_price=models.FloatField(default=0)
    P_mrp=models.FloatField(default=0)
    P_des=models.CharField(max_length=500)
    P_img=models.ImageField(upload_to="images")   
    def __str__(self):
        return self.P_name
class carousel(models.Model):
    img1=models.ImageField(upload_to="images") 
    img2=models.ImageField(upload_to="images") 
    img3=models.ImageField(upload_to="images")  
class Query(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.IntegerField(default=0)
    Problem=models.CharField(max_length=500)
    def __str__(self):
        return self.name
class Offer(models.Model):
    offer_type=models.CharField(max_length=200)
    offer=models.CharField(max_length=200)
    def __str__(self):
        return self.offer_type   
          
