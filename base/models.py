from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/4.1/ref/models/instances/ # django documentation - models

# for age (minimum 6 and maximum 99)
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth.models import User                                   # Adding Registered User to student model (Django4kids Getting data per user)

class Student(models.Model):
    name = models.CharField(max_length=50, null=False,
                            blank=False, unique=True)
    age = models.IntegerField(default=6, validators=[
                                                    MinValueValidator(6), 
                                                    MaxValueValidator(99)
                                                    ]
                                                    )
    createdTime = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, default='/placeholder.png')     # IMAGE upload - django4kids, note: if we add also: upload_to='Posted_Images' will make it that pictures go to Posted_Images folder instead of static
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)               # Adding Registered User ID to student model (Django4kids Getting data per user)
    def __str__(self):
        return f'{self.name} {self.age}'
