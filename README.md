# CodeConnect Backend and Database

## Steps to run:

1. Clone the repo and open in VSCode
2. Create virtual enviorement in the CodeConnect root directory run 'python -m venv env'(Mac or Linux may be different) in terminal
3. Go to our shared Google Drive and download the `.env` file that has the Django key and put it in the CodeConnect/codeC/backend.
4. in terminal activate the virutal enviorement while in root directory
5. in terminal run 'pip install -r requirements.txt'
6. in backend/settings.py change database information to personal database info
7. cd to codeC directory and run 'python manage.py makemigrations' then run 'python manage.py migrate' to make changes to database.
8. run 'python manage.py runserver'
