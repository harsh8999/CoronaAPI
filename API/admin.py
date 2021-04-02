from django.contrib import admin
from . models import User, Hospital, DocumentRegistration
# Register your models here.

admin.site.register(Hospital)
admin.site.register(DocumentRegistration)