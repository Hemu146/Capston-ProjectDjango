from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

# Create your models here.
class ServiceProvider(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=10,unique=True,validators=[
            RegexValidator(
                regex=r'^\d{10}$',
       
                message="Phone number must be exactly 10 digits."
            )
        ],
        help_text="Enter 10 digit mobile number.")
    password=models.CharField(max_length=16,validators=[MinLengthValidator(6,message="Password must be at least 8 characters.")])
    pincode=models.CharField(max_length=6)
    address=models.TextField()

class Services(models.Model):
    id=models.AutoField(primary_key=True)
    service_name=models.CharField(unique=True,max_length=40,null=False)
    providers = models.ManyToManyField(
        ServiceProvider,
        related_name="services",
        blank=True,
    )

class Users(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=10,unique=True,validators=[
            RegexValidator(
                regex=r'^\d{10}$',
       
                message="Phone number must be exactly 10 digits."
            )
        ],
        help_text="Enter 10 digit mobile number.")
    password=models.CharField(max_length=16,validators=[MinLengthValidator(6,message="Password must be at least 8 characters.")])
    adress=models.TextField()
    STATUS_CHOICES = [
        ('student', 'Student'),
        ('working', 'Working'),
        ('family', 'Family'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    REFERENCE_CHOICES = [
        ('poster', 'Poster'),
        ('social_media', 'Social Media'),
        ('friends', 'Friends'),
        ('other', 'Other'),
    ]
    reference = models.CharField(max_length=20, choices=REFERENCE_CHOICES)
