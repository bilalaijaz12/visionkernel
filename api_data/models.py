from django.db import models

class UserApiKeys(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    api_name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=200)

class FinancialData(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    api_name = models.CharField(max_length=100)
    data = models.JSONField()
    fetched_at = models.DateTimeField(auto_now_add=True)
