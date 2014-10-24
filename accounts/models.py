from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from donation.models import Charity
class UserProfile(models.Model):  
    user = models.OneToOneField(User)  
    #other fields here
    name = models.CharField(max_length=20,null=True)
    favored_charity = models.ForeignKey("donation.Charity",null=True)
    card = models.CharField(max_length=20,null=True)
    threshold = models.IntegerField(max_length=20,null=True)
    roundup = models.IntegerField(max_length=20,null=True)
    upper_limit = models.IntegerField(max_length=20,null=True)
    last_update = models.DateTimeField(auto_now=True)
    def __unicode__(self):  
          return "%s's profile" % self.user  

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User)
admin.site.register(UserProfile)