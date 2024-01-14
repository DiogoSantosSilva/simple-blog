# Simple Django Blog

This project is a simple blog created for the purpose of learning Django, a powerful web framework for Python.

## Project Setup

Follow the steps below to set up the project on your local environment.

```bash
# 1. Create a Virtual Environment
virtualenv -p python3 venv

# 2. Activate the Virtual Environment
source venv/bin/activate

# 3. Install Requirements
pip install -r requirements.txt

# 4. Run the Initial Migrations
python manage.py migrate

# 4. Run the Initial Migrations
python manage.py runserver
