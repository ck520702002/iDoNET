from django.conf.urls import patterns, url
from donation.views import *

urlpatterns = patterns('',
	url(r'^query/$', QueryView.as_view()),
	url(r'^donateInvoice/$', DonateInvoiceView.as_view()),
 )