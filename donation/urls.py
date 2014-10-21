from django.conf.urls import patterns, url
from donation.views import *

urlpatterns = patterns('',
	url(r'^query/$', DonationView.as_view()),
 )