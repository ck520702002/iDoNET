from django.conf.urls import patterns, url
from posts.views import *

urlpatterns = patterns('',
	
	url(r'^query/$', DonationView.as_view()),
 )