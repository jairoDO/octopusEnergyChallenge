from nem13.models import Header, AccumulationMeterData, AccumulationMeterData, B2BDetails, End
from ._validators import NEM13Validator, HeaderValidator, AccumulationMeterDataValidator, B2BDetailsValidator
from django.db import IntegrityError
import pandas as pd

HEADER = 100
ACCUMULATION_METER_DATA = 250
B2B_DETAILS = 500
END = 900
HEADER_ROW_LENGTH = 3
ACCUMULATION_METER_DATA_ROW_LENGTH = 23
B2B_DETAILS_ROW_LENGTH = 5

class Processor:
    record_indicator = None
    validator = None
    model = None
    row_length = None
    date_fields = None
    datetime_fields = None
    integer_fields = None
    fill_na_value = 0

    def __init__(self, dataframe, file_name):
        self.dataframe = dataframe[dataframe[0] == self.record_indicator]
        self.file_name = file_name

    def process(self):
        """
        Process the row to model
        :return: problems: list with error if there are any of them
                 duplicated: list of self.Model with duplicated instances if there are any of them
                 new_instances: list with the new instances of model created
        """
        problems, to_process = self.validate_rows()
        self.convert_types()
        duplicated = []
        new_instances = []
        for row in to_process.iloc:
            row = row[range(self.row_length)]
            row = row.fillna(self.fill_na_value)
            new_instance = self.model(None, *row)
            new_instance.file_path = self.file_name
            try:
                new_instance.save()
            except IntegrityError:
                duplicated.append(new_instance)
                continue
            except Exception:
                problems.append(new_instance)
                continue
            new_instances.append(new_instance)
        return problems, duplicated, new_instances

    def validate_rows(self):
        """
        Valid the content of the dataframe with the check defined in the validator
        :return: problems, dataframe
        """
        problems = self.validator(list(self.dataframe[:].values)).validate()
        valid = [problem['row'] - 2 for problem in problems]
        self.dataframe = self.dataframe[~self.dataframe.index.isin(valid)]
        return problems, self.dataframe

    def convert_types(self):
        """
        casts the values of the dataframe

        :return:
        """
        # cast to date type
        if self.date_fields:
            self.dataframe[self.date_fields] = self.dataframe[self.date_fields].apply(pd.to_datetime, format="%Y%m%d")
        # cast to datetime type
        if self.datetime_fields:
            self.dataframe[self.datetime_fields] = self.dataframe[self.datetime_fields].apply(pd.to_datetime,
                                                                                              format="%Y%m%d%H%M%S")
        # cast to numerical type
        if self.integer_fields:
            self.dataframe[self.integer_fields] = self.dataframe[self.integer_fields].apply(pd.to_numeric)


class AccumulationMeterDataProcessor(Processor):
    """
    This class config the processor for AccumulationMeterData
    """
    record_indicator = ACCUMULATION_METER_DATA
    validator = AccumulationMeterDataValidator
    model = AccumulationMeterData
    row_length = ACCUMULATION_METER_DATA_ROW_LENGTH
    date_fields = [20]
    datetime_fields = [9, 14, 21, 22]
    integer_fields = [0, 11, 16, 18]


class HeaderProcessor(Processor):
    """
    This class config the processor for Header
    """

    record_indicator = HEADER
    validator = HeaderValidator
    model = Header
    row_length = HEADER_ROW_LENGTH
    datetime_fields = [2]
    integer_fields = [0]


class B2BDetailProcessor(Processor):
    """
    This class config the processor for B2BDetail
    """
    record_indicator = B2B_DETAILS
    validator = B2BDetailsValidator
    model = B2BDetails
    row_length = B2B_DETAILS_ROW_LENGTH
    integer_fields = [0]
    fill_na_value = ''
