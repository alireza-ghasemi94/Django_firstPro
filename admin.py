from django.contrib import admin

# Register your models here.
from .models import infoBook , category ,lang

admin.site.register(infoBook)
admin.site.register(category)
admin.site.register(lang)