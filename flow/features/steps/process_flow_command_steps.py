import os.path
from functools import partial
from io import StringIO
from django.core.management import call_command
from behave import *
use_step_matcher("parse")
DATA_DIRECTORY = os.path.join(os.path.split(__file__)[0], 'data')


@step(u'I call command process_nem13 with parameters "-f {file_path}"')
@step(u'I call command process_nem13 with parameter "-f {file_path}"')
def call_command_step(context, file_path):
    context.out = StringIO()
    file_paths = list(map(partial(os.path.join, DATA_DIRECTORY), file_path.split()))
    call_command("process_nem13",
                  '-f',
                  *file_paths,
                  stdout=context.out,
                  stderr=StringIO())
    context.command_result = context.out.getvalue()


@step(u'I should see the message')
def should_see_step(context):
    if not context.text:
        raise Exception('This step required text wrapped in triple "')
    context.test.assertTrue(context.command_result.find(context.text) != -1, "The message was not found")

@step(u'I pause for debug')
def pause_for_debug(context):
    import pdb, sys;
    pdb.Pdb(stdout=sys.__stdout__).set_trace()