from django.db import models

# Create your models here.
class Blog(models.Model):

    #title
        stat = models.CharField(max_length=10)
    #Publishdate
        Publishdate = models.DateTimeField()
    #images
        image =models.ImageField(upload_to='images/')
    #body
        body =models.TextField()
