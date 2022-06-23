from django.db import models


class ToDo(models.Model):

    
    title=models.CharField( max_length=50)
    body=models.TextField()
    

    
    def __str__(self):
        return self.title


class Product(models.Model):

    
    name=models.CharField( max_length=50)
    price =models.IntegerField((""))
    discp=models.TextField((""))
    image=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    
    

    
    def __str__(self):
        return self.name



        

  
