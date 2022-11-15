import operator
import os

from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from ._validators import NEM13Validator
from ._processors import HeaderProcessor, AccumulationMeterDataProcessor, B2BDetailProcessor

HEADER = 100
ACCUMULATION_METER_DATA = 250
B2B_DETAILS = 500
END = 900

pd.options.mode.chained_assignment = None


class Command(BaseCommand):
    help = 'Process CSV file who represent a flow of the nem13 and upload To database'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.invalid_files = []
        self.not_found_files = []
        self.successful_files = []

    def add_arguments(self, parser):
        parser.add_argument('-f', '--file_path',
                            nargs='+',
                            help='the path or paths file of the csv who represent the nem13.',
                            required=True)
        parser.add_argument('-d', '--delimiter',
                            help='The delimiter ("," default) of csv',
                            default=',',

                            required=False)

    def handle(self, *args, **options):
        for file_path in options['file_path']:
            try:
                data_frame = self.get_data_frame_from_file_path(file_path, options['delimiter'])
                if data_frame is None:
                    continue
                self.process_file(data_frame, file_path)

            except CommandError:
                raise CommandError('One error happen when the command it was running')
        self.print_resume()

    def print_resume(self):
        """
         Print the resume of the file processes

        """
        str_total = lambda x: f'{len(x)}: {",".join(x)}'
        self.stdout.write(self.style.SUCCESS(f"Total bad path files {str_total(self.not_found_files)}"))
        self.stdout.write(self.style.SUCCESS(f"Total invalid files {str_total(self.invalid_files)}"))
        self.stdout.write(self.style.SUCCESS(f"Total process successful {str_total(self.successful_files)}"))

    def process_file(self, data_frame, file_path):
        """
        Process the file with the processors

        :param data_frame:
        :param file_path:
        :return:
        """
        processors = [HeaderProcessor, AccumulationMeterDataProcessor, B2BDetailProcessor]
        file_name = os.path.split(file_path)[1]
        for processor in processors:
            invalid_rows, duplicated, new_instances = processor(dataframe=data_frame, file_name=file_name).process()
            if invalid_rows:
                self.stdout.write(self.style.ERROR(
                    f'Invalid rows found when try to process {processor.model.__name__}: problems:{invalid_rows}'))
            if duplicated:
                self.stdout.write(f'Warning: rows who were uploaded found:{duplicated}')
            if new_instances:
                self.stdout.write(self.style.SUCCESS(f'Upload {len(new_instances)} {processor.model.__name__} '
                                                     f'new instances '))
        if file_name not in self.invalid_files:
            self.successful_files.append(file_name)

    def get_data_frame_from_file_path(self, file_path, delimiter):
        """
        Valid the file path if is valid return the date_frame created with the content of the csv file

        :param file_path: the file path of the csv
        :param delimiter:  the delimiter used to open the csv
        :return: pd.DataFrame if is valid else None
        """
        valid = True
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f'The file path {file_path} is not a path valid'))
            self.not_found_files.append(file_path)
            valid = False
        if file_path[-len('csv'):].lower() != 'csv':
            self.stdout.write(self.style.ERROR(f'The file should be a CSV file but found {file_path[-len("csv"):]}'))
            self.invalid_files.append(os.path.split(file_path)[1])
            valid = False
        if valid:
            data_frame = pd.read_csv(file_path, header=None, delimiter=delimiter)
            file_name = os.path.split(file_path)[1]
            problems = NEM13Validator(data=data_frame).validate()
            if problems:
                self.stdout.write(f'We could not process this flow because we found the following'
                                  f' errors : {problems}')
                self.invalid_files.append(file_name)
        else:
            return None

        return data_frame
