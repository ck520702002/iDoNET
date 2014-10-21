from django.conf.urls import patterns, url
from donation.views import *

urlpatterns = patterns('',
	url(r'^query/$', QueryView.as_view()),
	url(r'^invoice1/$', DonateInvoiceView.as_view()),
	url(r'^coin1/$', DonateCoinView.as_view()),
 )