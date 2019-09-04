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

        def summary(self):
            return self.body[:50]

        def Publishdate_pretty(self):
            return self.Publishdate.strftime("%b %e %Y")

        def __str__(self):
            return self.stat
