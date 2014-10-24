from django.contrib import admin
from models import Donation_detail,Charity,Invoice
# Register your models here.
admin.site.register(Donation_detail)
admin.site.register(Charity)
admin.site.register(Invoice)