need to install pillow for image related things
Our site can protect against cross site scripting attacks, due to the csrf_token used in django

references:-
https://realpython.com/django-hosting-on-heroku/

install the dependencies before running by
python -m pip install -r requirements.txt

proper way to initialize a new Django project
python3 -m venv ./venv --prompt "project-name"

source venv/bin/activate

which python

python -m pip install django==3.2.5

// For upgrading pip 
python -m pip install --upgrade pip

python -m pip list

It outputs roughly the same set of dependencies with their sub-dependencies in a special format
python -m pip freeze 

python -m pip freeze > requirements.txt

when runnning the project install dependencies by
python -m pip install -r requirements.txt
