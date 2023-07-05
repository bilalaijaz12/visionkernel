from django.contrib import admin
from .models import UserApiKeys, FinancialData

admin.site.register(UserApiKeys)
admin.site.register(FinancialData)
