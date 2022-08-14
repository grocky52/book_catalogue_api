from django.db import models

# Create your models here.



class Books(models.Model):
    title = models.CharField(max_length=100)
    num_pages = models.IntegerField()
    quantity = models.IntegerField()





"""{
"title" : "flutter",
"num_pages": 200,
"quantity": 30
}"""