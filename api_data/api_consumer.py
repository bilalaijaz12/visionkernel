from fredapi import Fred
from .models import UserApiKeys, FinancialData
from django.contrib.auth.models import User

def fetch_data(api_name, user_id, series_id):
    user = User.objects.get(id=user_id)
    api_key_entry = UserApiKeys.objects.get(user=user, api_name=api_name)
    api_key = api_key_entry.api_key

    if api_name == 'FRED':
        fred = Fred(api_key=api_key)
        data = fred.get_series(series_id)

        # Store the data in the database
        FinancialData.objects.create(user=user, api_name=api_name, data=data.to_json())

    # Add else if conditions for other API names as necessary
