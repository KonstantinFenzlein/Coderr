# Coderr Backend

Django REST Framework backend for the Coderr frontend (Developer Akademie project).

## Setup

1. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```
   python manage.py migrate
   ```
4. Create a superuser (for the Django admin):
   ```
   python manage.py createsuperuser
   ```
5. Start the development server (must run on port 8000, the frontend expects this):
   ```
   python manage.py runserver
   ```

## Notes

- The frontend expects the API at `http://127.0.0.1:8000/api/`.
- Authentication uses DRF Token Authentication (`Authorization: Token <token>` header).
- CORS is configured for the frontend running on Live Server (`http://127.0.0.1:5500`).
