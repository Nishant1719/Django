from django.db import models
from django.utils import timezone

# Create your models here.
class chaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML','masala'),
        ('GR','ginger'),
        ('KL','kivi'),
        ('EL','elaichi'),
        ('PL','plain'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)