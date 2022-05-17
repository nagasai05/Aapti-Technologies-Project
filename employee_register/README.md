Employee Registry project

Start with opening environment

cd employee_env/Scripts/activate

After the environment is established, migrations should be made -

python manage.py makemigrations python manage.py migrate

After the migrations happened

python manage.py runserver

After the server is established - Use username - nagasai, password - 12345678

If it is to create new superuser -

python manage.py createsuperuser -

give username and password to create admin credentials