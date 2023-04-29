from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class service(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField (null=True, blank=True)

    def __str__(self):
	    return self.title
    
class work(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField( null=True, blank=True)
    picture = models.ImageField (null=True, blank=True)
    demolink = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
	    return self.title    

class blog(models.Model):
    image = models.ImageField( null=True, blank=True)
    date = models.DateTimeField(null=True,blank=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    

    def __str__(self):
	    return self.title    
    
class contact(models.Model):
   name = models.CharField(max_length=200, null=True)
   email = models.CharField(max_length=200, null=True)
   subject = models.CharField(max_length=200, null=True)
   message=models.TextField( null=True, blank=True)

   def __str__(self):
	    return self.name  
        
class education(models.Model):
    Faculty= models.CharField(max_length=200, null=True)
    Collegename = models.CharField(max_length=200, null=True)
    description = models.TextField( null=True, blank=True)
    def __str__(self):
	    return self.Collegename  
        

class experience(models.Model):
    jobtitle= models.CharField(max_length=200, null=True)
    company = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
	    return self.jobtitle  
        

