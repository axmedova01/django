from django.contrib import admin
from .models import main, nam, surname, patronymic, street

admin.site.register(main)
admin.site.register(nam)
admin.site.register(surname)
admin.site.register(patronymic)
admin.site.register(street)