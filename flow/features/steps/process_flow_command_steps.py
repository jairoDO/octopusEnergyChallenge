import os.path
from io import StringIO
from django.core.management import call_command
from behave import step

DATA_DIRECTORY = os.path.join('data', os.path.split(__file__))


@step('I have a file csv with valid data called "{file_name}"')
def have_file(context, file_name):
    file_path = os.path.join(DATA_DIRECTORY, file_name)
    if not os.path.exists(file_path):
        content =



