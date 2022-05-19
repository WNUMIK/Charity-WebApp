
# Charity-Donation App

# Demo:
[https://charitymw.herokuapp.com/](https://charitymw.herokuapp.com/)

## Skąd pomysł na projekt

-  Użytkownik ma w domu rzeczy, których chce się pozbyć, ale nie wie jak.
- Jest wiele dostępnych rozwiązań, ale wiele z nich wymaga dodatkowego wysiłku lub nie ma do nich zaufania. W zweryfikowane miejsca trzeba pojechać, a nie ma na to czasu/ nie ma jak tam pojechać, a kontenery pod domem lub lokalne zbiórki są niezweryfikowane i nie wiadomo czy te rzeczy faktycznie trafią do potrzebujących. 

# Demo:
[https://charitymw.herokuapp.com/](https://charitymw.herokuapp.com/)

## Installation

Clone charity with git:

```bash
    git clone git@github.com:k1wsatz/charity.git
    cd charity
```
Setup a local development environment:

`pipenv shell`

Install development dependencies:

`pipenv install -r requirements.txt`

Migrate Database:

`python manage.py migrate`

Run the web application locally:

`python manage.py runserver`

## Environment Variables
To run this project, you will need to add the following environment variables to your .env file. You can also use file `.env-default`, put there your own data and rename it to `.env` than run command `source env/.env` in terminal to activate.

`POSTGRES_USER=`

`POSTGRES_PASSWORD=`

`POSTGRES_DB=`

`DATABASE_URL=`

`DEBUG=`

`SECRET_KEY=`

`DJANGO_ALLOWED_HOSTS=`

`DJANGO_SU_NAME=`

`DJANGO_SU_EMAIL=`

`DJANGO_SU_PASSWORD=`