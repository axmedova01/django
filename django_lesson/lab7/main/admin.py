from django.contrib import admin
from .models import Good
from .models import Token

admin.site.register(Good)
admin.site.register(Token)