from django.contrib import admin

# Register your models here.
from application.account.models import CustomUser

admin.site.register(CustomUser)
