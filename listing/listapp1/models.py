from django.db import models
# from PIL import Image
# Create your models here.
from rest_framework.fields import FileField

class Employee(models.Model):
    Name=models.CharField(max_length=200)
    Telephone=models.IntegerField()
    Age=models.IntegerField()
    # Profile_pic=models.ImageField(upload_to='images')
    # Profile_pic = models.FileField(blank=False,null=True,default=None)
    Email = models.EmailField(max_length=254)
    Username = models.CharField(max_length=200,unique=True)
    Password = models.CharField(max_length=200)
    isActive=models.BooleanField(default=False)
    isLog = models.BooleanField(default=False)
    def __str__(self):
        return self.Username

class Employee1(models.Model):
    Name=models.CharField(max_length=200)
    Telephone=models.IntegerField()
    Age=models.IntegerField()
    Emptype=models.CharField(choices=
              [('ADMIN', 'ADMIN'), ('EMPLOYER', 'EMPLOYER'), ('EMPLOYEE', 'EMPLOYEE')],
              default='EMPLOYEE', max_length=20)
    # Profile_pic=models.ImageField(upload_to='images')
    # Profile_pic = models.FileField(blank=False,null=True,default=None)
    Email = models.EmailField(max_length=254)
    Username = models.CharField(max_length=200,unique=True)
    Password = models.CharField(max_length=200)
    isActive=models.BooleanField(default=False)
    isLog = models.BooleanField(default=False)
    def __str__(self):
        return self.Username
class pgdtl(models.Model):
    pagename=models.CharField(max_length=200)
    pagecategory=models.CharField(max_length=200)
    pageid=models.IntegerField()
    # Age=models.IntegerField()

    def __str__(self):
        return self.pageid

# class page1(models.Model):
#     pagename=models.CharField(max_length=200)
#     pagecategory=models.CharField(max_length=200)
#     pageid=models.IntegerField()
#     # Age=models.IntegerField()
#
#     def __str__(self):
#         return self.pageid