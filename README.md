[![Encarta Logo](http://encartambm.in/static/img/logo_small.png)](http://encartambm.in)

# Encarta 2018 Website

Website for Encarta 2018


## Getting Started

This is a straight forward Django project. A little profeciency in Python is expected. 
Use Python3.

### Prerequisites

You'll need following software to get started.

```
Python3 
Django 
MySQL 
Sublime Text! 
venv | python3-venv | virtualenvwrapper | (or whatever floats your virtual env boat)
```

### Installing

To set up development environment follow these steps. Of course, it is assumed that you have already complied with the above prerequisites.

```
git clone git@github.com:ashishbansalmbm/encarta2k18.git 
cd into/wherever/you/cloned/this/repo
pip install -r requirements.txt
```

And Django stuff!

```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

You should see the website running at http://127.0.0.1:8000

## Deployment

Standards Ubuntu server deployment with nginx and gunicorn. 
For configuration details check the _configurations_ forlder

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Python](https://www.python.org/) - Programming language for the uninitiated
* [pyCharm](https://www.jetbrains.com/pycharm/) - Yes, someone used that too.
* [Sublime Text](https://www.sublimetext.com/) - A sophisticated text editor for code, markup and prose

## Contributing

Please be humane and contact the maintainer.

## Versioning

We don't use any versioning whatsoever in this project!
