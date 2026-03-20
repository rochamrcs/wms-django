# WMS Django
Warehouse Management System built with Django.

## Features
- Product registration and listing
- Stock control

## Tech Stack
- Python
- Django

## How to Run

**1. Create and activate your virtual environment**
```bash
# Create
python -m venv .venv

# Activate (Windows)
.venv\Scripts\Activate.ps1

# Activate (Linux/macOS)
source .venv/bin/activate
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure environment variables**
```bash
cp .env-example .env
# Edit .env and set your SECRET_KEY
```

**4. Run migrations**
```bash
python manage.py migrate
```

**5. Start the server**
```bash
python manage.py runserver
```