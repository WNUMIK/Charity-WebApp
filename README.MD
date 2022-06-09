[![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://pl.python.org/)
[![](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)](https://www.heroku.com/)
[![](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

[![GitHub Clones](https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count&url=https://gist.githubusercontent.com/k1wsatz/28960bd0b83191249b4689b609c3745d/raw/clone.json&logo=github)](https://github.com/MShawon/github-clone-count-badge)
# ![](static/images/favicon-32x32.png)Charity-Donation App

# Demo:
[https://charitymw.herokuapp.com/](https://charitymw.herokuapp.com/)

## APP

Fronted was made by CodersLab.

## Idea

- User has miscellaneous things in home which he wants to donate
- There are available solutions but many of them require additional effort or are not veryfied.

## Pros of this App

- Admin Panel with CRUD options
- Possibility to register and make a donation through form
- Dynamic list of institutions and quantity of donated things
- Dynamic filtering of institutions on based on choosen category
- Individual profile with statistics and possibility to mark donation as taken

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

## Author
- [@k1wsatz](https://www.github.com/k1wsatz)
