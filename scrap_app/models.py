from django.db import models




class Proxy_data(models.Model):
    ip= models.GenericIPAddressField()
    port= models.IntegerField()
    protocol= models.CharField(max_length=100)
    country= models.CharField(max_length=150)
    uptime= models.FloatField()
    

    def __str__(self):
        return self.country