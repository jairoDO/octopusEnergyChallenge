Octopus Energy technical challenge
=======
This document describes a solution for the technical challenge that forms part of the Octopus
Energy (OE) recruitment process for back-end engineers.

Requirements
----------
- python >= 3.8
- pip
- pipenv
- octopus_energy_technical.zip
- allure (https://docs.qameta.io/allure/#_installing_a_commandline)

Install
-------
- extract octopus_energy_technical.zip
- cd to the folder extracted
- pip install pipenv
- pipenv shell
- pip install -r requirements.txt

Started
--------
- cd flow
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser (follow the steps)


Problems
----------
- It should have a management command that can be called with the path to a
NEM13 file (or files). The specification for these files is included below.

  - For this requirement I create a command called process_nem13. Example of the execution:
      - python manage.py process_nem13 -f path_file_of_csv
      - python manage.py process_nem13 -f path_file_of_csv path_file2_of_csv
- It should provide a version of the Django admin site that allows a user to search
for the reading values and dates associated with either:
  - For this you require to run the command process_nem13 and make sure the models was upload successful
  - run python manage.py runserver
  - go to http://127.0.0.1:8000/admin/
  - login with the superuser before created
  - go to http://127.0.0.1:8000/admin/nem13/accumulationmeterdata/
- Search for NMI, meter serial number
- <img src="/img.png?raw=true" alt="Search by nmi or meter serial number" title="Search by nmi or meter serial number">

Code
----

The code is a project in django, with the app flow and nem13with a command process_nem13 also have  unittests, and functional tests using django-behave 
```bash
├── README.md
├── Pipfile
├── Pipfile.lock
├── README.md
├── flow
│   ├── __init__.py
│   ├── behave.ini --->'behave config file'
│   ├── features ---> 'folder for django-behave' 
│   │   ├── __init__.py
│   │   ├── environment.py
│   │   ├── flow_processor_command.feature
│   │   └── steps
│   │       ├── __init__.py
│   │       ├── data ---> 'folder for csv files used to test the comand'
│   │       │   ├── file_nm13_with_b2b_details.csv
│   │       │   ├── invalid_nm13.csv
│   │       │   ├── valid_nm13.csv
│   │       │   └── valid_nm13_2.csv
│   │       └── process_flow_command_steps.py --> 'steps implemented for behave'
│   ├── flow
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── help.py
│   ├── manage.py
│   ├── nem13
│   │   ├── __init__.py
│   │   ├─
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── management
│   │   │   ├── __init__.py
│   │   │   └── commands
│   │   │       ├── __init__.py
│   │   │       ├── _processors.py  --> 'contains classes used for process the dataframe to Models'
│   │   │       ├── _validators.py --->'contains classes for validate the data again technical doc '
│   │   │       ├── process_nem13.py --> 'Implementation of the command'
│   │   │       └── tests 
│   │   │           ├── __init__.py
│   │   │           └── test_validators.py --> 'django.test.TesCase for _validators '
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   └── reports
│       └── TESTS-flow_processor_command.xml
├── requirements.txt
  - 
```

Run test
--------
- Run behave tests` python manage.py behave` 
    - (https://behave-django.readthedocs.io/en/stable/)
- Run unittests ` python manage.py test nem13.management.commands.tests.test_validator`  


Run report
----------
- allure required, and run before python manage.py behave
- allure serve reports/








