from enum import unique
from django.db import models
import uuid
from django.db.models.base import Model

from django.db.models.deletion import CASCADE





# Create your models here.
class infoBook(models.Model):
    Id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    NameBook = models.CharField(max_length=100)
    Writer = models.CharField(max_length=100,null=True,blank=True)
    BookISBN = models.IntegerField(default=0,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    lang = models.ManyToManyField('lang',blank=True)
    # lang = models.ForeignKey('lang',on_delete=models.CASCADE,default=0000)
    Create_Book = models.DateTimeField(auto_now_add=True)
    category_book = models.ManyToManyField('category',blank=True)
    

    def __str__(self) -> str:
        return self.NameBook


class category(models.Model):
    Id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    Category = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    Create_category = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.Category

class lang(models.Model):
    Id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    lang_name = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return self.lang_name