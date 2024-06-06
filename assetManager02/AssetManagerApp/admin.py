from django.contrib import admin
from .models import Space, UserLog


# Register your models here.
admin.site.register(UserLog)
admin.site.register(Space)
