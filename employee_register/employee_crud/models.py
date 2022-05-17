from django.db import models

# Create your models here.
TITLE_CHOICES = (
    ('mr','Mr'),
    ('mrs',"Mrs")
)
ROLE_CHOICES = (
    ('user','USER'),
    ('admin','ADMIN')

)
class Employee(models.Model):
    title = models.CharField(max_length=10,choices=TITLE_CHOICES,default = "mr")
    firstname = models.CharField(primary_key='true',max_length=50,unique='true')
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    role = models.CharField(max_length=10,choices=ROLE_CHOICES,default="user")
    password = models.CharField(max_length=50,default="********")
    class Meta:
        db_table = "employee"