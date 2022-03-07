from django.db import models

# Create your models here.
class Customer(models.Model):
    image=models.ImageField(upload_to="uploads",default="a.png")
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    address=models.TextField()
    joining_date=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.name