# programmers_community

# Local Environment

# Install
1 Create Virtual environment

 virtualenv venv
 
 Or
 
 pipenv shell
 
2 Active Virtualenv

 source venv/bin/active
pipenv shell auto active

3 Clone the repository and install the packages in the virtual enviroment:

 pip install -r requirements.txt

# Run

1. With the venv active it, execute: 
 python manage.py collectstatic

2. Create initial database:
 python manage.py migrate
 
3. Runs server:
 python manage.py runserver
 
