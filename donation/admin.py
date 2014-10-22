from django.contrib import admin
from models import donation_detail,Charity,Invoice
# Register your models here.
admin.site.register(donation_detail)
admin.site.register(Charity)
admin.site.register(Invoice)