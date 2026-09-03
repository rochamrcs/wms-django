# WMS Django

Warehouse Management System (WMS) developed with Django to organize products and
warehouse locations. The project is currently evolving as the foundation for the
main operational processes of a WMS.

## Implemented Features

- User authentication with login and logout.
- Product registration and listing.
- Product search by name or code.
- Product filtering by active or inactive status.
- Product status updates.
- Warehouse location listing.
- Location filtering by name, plant, warehouse, and status.

## Planned Features

- Inbound receiving and stock entry control.
- Outbound picking and stock dispatch control.
- Inventory adjustments and change history.
- Warehouse location occupancy control.
- Operational and management reports.
- Role-based access control for users, profiles, and permissions.

## Technology Stack
- Python
- Django

## Getting Started

**1. Create and activate a virtual environment**
```bash
# Create
python -m venv .venv

# Activate (Windows)
.venv\Scripts\Activate.ps1

# Activate (Linux/macOS)
source .venv/bin/activate
```

**2. Install the dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure environment variables**
Create a `.env` file in the project root with the following values:

```dotenv
SECRET_KEY=your-local-development-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

Use a unique secret key and set `DEBUG=False` in production. Do not commit
credentials or secret keys to the repository.

**4. Apply database migrations**
```bash
python manage.py migrate
```

**5. Start the development server**
```bash
python manage.py runserver
```