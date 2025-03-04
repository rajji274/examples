import weakref
from django.contrib import admin
from application.models import Register,Weatherdetails
# Register your models here.
admin.site.register(Register)
admin.site.register(Weatherdetails)
