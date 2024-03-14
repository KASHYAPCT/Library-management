from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    admission_number=models.BigAutoField(   
    primary_key=True,
        
    )
    

class Add_Book(models.Model):
    Book_id=models.DecimalField(max_digits=10,null=False,blank=True,decimal_places=2)
    Book_name=models.CharField(max_length=250,null=True,blank=True)
    Author_name=models.CharField(max_length=230,null=True,blank=True)
    Quantity=models.IntegerField(null=True)
def __str__(self):
   return self.Book_name

class Student_Book(models.Model): 
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    stud_name=models.CharField(null=True,blank=True,max_length=230)
    book_name=models.CharField(null=True,blank=True,max_length=230)
    book_id=models.IntegerField(null=False,blank=False,default=0)
    author_name=models.CharField(max_length=100,null=True,blank=True)
    issue_date=models.DateField(auto_now=True)
    expiry_date=models.DateField(auto_now=True)
    fine=models.IntegerField(null=False,blank=False,default=0)
    confirm=models.BooleanField(null=False,blank=False,default=0)
def __str__(self):
        return self.stud_name
