from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):  
    user = models.OneToOneField(User)  
    #other fields here
    name = models.CharField(max_length=20)
    card = models.CharField(max_length=20)
    threshold = models.IntegerField(max_length=20)
    roundup = models.IntegerField(max_length=20)

    def __str__(self):  
          return "%s's profile" % self.user  

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User)

admin.site.register(UserProfile)