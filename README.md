[<picture><source media="(prefers-color-scheme: dark)" srcset="https://github.com/vppelli/Vppelli/blob/main/img/RECIPEAPP.png"><source media="(prefers-color-scheme: light)" srcset="https://github.com/vppelli/Vppelli/blob/main/img/LRECIPEAPP.png"><img alt="RecipeApp link" src="https://github.com/vppelli/Vppelli/blob/main/img/RECIPEAPP.png">
</picture>](https://github.com/vppelli/recipe-app)

# Description
 A Python, Django-based web application that allows users to log in, add, edit, delete, or view recipes stored using a PostgreSQL database and hosted through Heroku. Users can store all recipes in one application allowing them to view them anytime they want.
 
## Objective
To deploy my Django web application on a web server, Enhance user experience and look and feel of your web application using CSS and JS, and implement search and visualization (reports/charts) features. Use QuerySet API, DataFrames (with pandas), and plotting libraries (with matplotlib). Create authentication for your web application, password protect your web application’s views.

## Table of Content
- [Project Setup](#setup)
- [Used](#used)
- [Host](#host-used)

# [Recipe App](https://recipe-mikes-8a1f7a74a98b.herokuapp.com) Live
- Test Login Account:
> username: Preview  password: Testuser123

## Future Features
- The app will allow users to Update and Delete recipes
- Making the app have more search features, e.g. by ingredients, cooking time, and difficulty.
 
## Setup
Easy to start, Django project!

Uses python-3.8.7

1. Clone the repository:
> git clone [repository URL] cd recipe-app

2. Install dependencies:
> pip install -r requirements.txt

3. Setup Database:
> Configure DATABASES in settings.py for your development and production environments.

4. Run Migrations:
> python manage.py migrate

5. Create Superuser for Admin Access:
> python manage.py createsuperuser

6. Run the Development Server:
> python manage.py runserver

7. Visit the address provided in your terminal to view the app.

## Used
- HTML
- JavaScript
- CSS
- Python
- Django

### Requirements
[Requirements.txt](https://github.com/vppelli/recipe-app/blob/150225ac7de15e28c56f94dbedc48ea870ab6f54/requirements.txt#L1C1-L25C13)

- ﻿asgiref==3.8.1
- backports.zoneinfo==0.2.1
- contourpy==1.1.1
- cycler==0.12.1
- dj-database-url==2.2.0
- Django==4.2.15
- fonttools==4.53.1
- gunicorn==23.0.0
- importlib_resources==6.4.4
- kiwisolver==1.4.5
- matplotlib==3.7.5
- numpy==1.24.4
- packaging==24.1
- pandas==2.0.3
- pillow==10.4.0
- psycopg2-binary==2.9.9
- pyparsing==3.1.4
- python-dateutil==2.9.0.post0
- pytz==2024.1
- six==1.16.0
- sqlparse==0.5.1
- typing_extensions==4.12.2
- tzdata==2024.1
- whitenoise==6.7.0
- zipp==3.20.1


## Host Used
Heroku: [https://heroku.com](https://heroku.com)

