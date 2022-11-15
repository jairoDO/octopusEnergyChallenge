import os
from io import StringIO


BEHAVE_DEBUG_ON_ERROR = False
os.environ["DJANGO_SETTINGS_MODULE"] = "flow.settings"

def before_scenario(context, scenario):
    context.out = StringIO()

def after_scenario(context, scenario):
    context.out.close()


def django_ready(context):
    context.django = True