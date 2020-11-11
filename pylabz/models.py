from django.db import models

# Create your models here.


# class example(models.Model):
# 	pass



class Contact(models.Model):
    firstname = models.CharField(max_length=30, unique= False)
    # lastname= models.TextField()
    email = models.EmailField(default="")
    # remarks = models.TextField(default="")


# html 
# firstname and email as input  we are going to save it  in our model