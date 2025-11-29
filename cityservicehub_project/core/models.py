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
    photo = models.ImageField(upload_to="photos/", blank=True, null=False)
    
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
        ('provider', 'Provider'),
        ('user', 'USER'),
        
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]
    gender =  models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default="male"
    )
