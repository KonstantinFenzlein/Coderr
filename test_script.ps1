$process = Start-Process python -ArgumentList "manage.py", "runserver" -PassThru -NoNewWindow -WorkingDirectory "C:\Users\kfenz\Desktop\Coderr-Backend"
Start-Sleep -Seconds 3

# Now run the test
python -c @"
import os
import django
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

BASE_URL = 'http://localhost:8000'

# Get first user
user = User.objects.first()
if not user:
    print('No users found')
    exit(1)

# Get or create token
token, _ = Token.objects.get_or_create(user=user)

headers = {
    'Authorization': f'Token {token.key}',
    'Content-Type': 'application/json'
}

# Test GET Profile
print('Testing GET /api/profiles/{0}/'.format(user.profile.id))
response = requests.get(f'{{BASE_URL}}/api/profiles/{{user.profile.id}}/', headers=headers)
print(f'Status: {{response.status_code}}')
print(f'Response: {{response.json()}}')
"@

Stop-Process -Id $process.Id -Force
