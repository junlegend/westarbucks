from django.db import models

# Create your models here.

# table 명: menus => Class 명
# columns: id -> INT, name -> VARCHAR(20)

class Menu(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

# 1. migration 파일을 생성한다.
# 2. migrate (실제 db로 입력)