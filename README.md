## Running the application
To run this application, clone the repository on your local machine and execute the following command.
```sh
    $ virtualenv -p python3 venv_drf
    $ cd venv_drf
    $ source bin/activate
    $ git clone https://github.com/shrikant-accion/tutorial.git
    $ cd tutorial
    $ pip install -r requirements.txt
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver
```