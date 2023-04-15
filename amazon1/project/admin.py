from django.contrib import admin

# Register your models here.
from project.models import Category
admin.site.register(Category)
from project.models import Product
admin.site.register(Product)
from project.models import Query
admin.site.register(Query)
from project.models import Offer
admin.site.register(Offer)
from project.models import carousel
admin.site.register(carousel)
