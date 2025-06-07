from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVariety(models.Model):
    # Models can be completely modified here which refected on the admin page.
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
    description = models.TextField(max_length=255,default='')
    price = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name
    
    
# One to many 
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.user.username} Review for {self.chai.name}'

    
# Many to Many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVariety,related_name='stores')

    def __str__(self):
        return self.name
    
    
# One to One 
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety,on_delete=models.CASCADE,related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(timezone.now)
    valid_until = models.DateTimeField()
    
    def __str__(self):
        return f'Certificate for {self.name.chai}'    