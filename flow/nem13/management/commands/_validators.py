from functools import partial
from csvvalidator import *
from operator import eq
import pandas as pd


class Validator:
    """
    Class created for validate the data with the css validator
    """

    def __init__(self, data: list[list], field_names: list[str]):
        self.field_names = field_names
        self.validator = CSVValidator(self.field_names)
        self.data = data

    def validate(self):
        if self.field_names:
            return self.validator.validate([self.field_names] + self.data)
        else:
            return self.validator.validate(self.data, expect_header_row=False)


class HeaderValidator(Validator):
    def __init__(self, data):
        field_names = [
            'RecordIndicator',
            'VersionHeader',
            'DateTime',
            'ToParticipant'
        ]
        super(HeaderValidator, self).__init__(data, field_names)
        self.validator.add_value_check('RecordIndicator', partial(eq, 100))
        self.validator.add_value_check('VersionHeader', check_length(5))
        self.validator.add_value_check('DateTime', check_datetime('%Y%m%d%H%M%S'))
        self.validator.add_value_check('ToParticipant', check_length(10))


class AccumulationMeterDataValidator(Validator):
    def __init__(self, data):
        field_names = [
            'RecordIndicator',
            'NMI',
            'NMIConfiguration',
            'RegisterID',
            'NMISuffix',
            'MDMDataStreamIdentifier',
            'MeterSerialNumber',
            'DirectionIndicator',
            'PreviousRegisterRead',
            'PreviousRegisterReadDateTime',
            'PreviousQualityMethod',
            'PreviousReasonCode',
            'PreviousReasonDescription',
            'CurrentRegisterRead',
            'CurrentRegisterReadDateTime',
            'CurrentQualityMethod',
            'CurrentReasonCode',
            'CurrentReasonDescription',
            'Quantity',
            'UOM',
            'NextScheduledReadDate',
            'UpdateDateTime',
            'MSATSLoadDateTime']

        super(AccumulationMeterDataValidator, self).__init__(data, field_names)
        self.validator.add_record_check(check_length(23))
        self.validator.add_value_check('RecordIndicator', partial(eq, 250))
        self.validator.add_value_check('PreviousRegisterReadDateTime', check_datetime())
        self.validator.add_value_check('CurrentRegisterReadDateTime', check_datetime())
        self.validator.add_value_check('NextScheduledReadDate', check_datetime("%Y%m%d"))
        self.validator.add_value_check('UpdateDateTime', check_datetime())
        self.validator.add_value_check('MSATSLoadDateTime', check_datetime())


class B2BDetailsValidator(Validator):

    def __init__(self, data):
        field_names = [
            'RecordIndicator',
            'PreviousTransCode',
            'PreviousRetServiceOrder',
            'CurrentTransCode',
            'CurrentRetServiceOrder'
        ]
        super(B2BDetailsValidator, self).__init__(data, field_names)
        self.validator.add_value_check('RecordIndicator', partial(eq, 500))


class EndValidator(Validator):
    def __init__(self, data):
        field_names = ['RecordIndicator']
        super(EndValidator, self).__init__(data, field_names)
        self.validator.add_value_check('RecordIndicator', partial(eq,900))


class NEM13Validator(Validator):
    def __init__(self, data):
        self.data = data

    def validate(self):
        return check_blocking_cycle(self.data)


def check_blocking_cycle(data):
    """
    This function validate that  structure of the file
    :param data: data_frame from pandas library
    :return:
    """
    problems = []
    if len(data) < 3:
           problems.append("The flow does have the requirement flow")

    first_column = data[0].astype(int).values

    if first_column[0] != 100:
        problems.append(f'The flow should start with code of Header Record but found{first_column[0]}')

    if first_column[-1] != 900:
        problems.append(f"The flow should end with code of End but found{data[-1]}")
    record_identifier_unknown = list(filter(lambda x: x[1] not in [100, 250, 500, 900], enumerate(first_column)))
    if record_identifier_unknown:

        problems.append(f"RecordIndicator unknown"
                        f" {','.join([ f'row:{index} value:{value}' for index, value in record_identifier_unknown])}")

    if len(list(filter(partial(eq, 900), first_column))) > 1:
        problems.append(f'The flow should had one End Record')
    return problems


def check_length(limit):
    def checker(value):
        if len(value) > limit:
            raise ValueError(value)
    return checker


def check_datetime(format="%Y%m%d%H%M%S"):
    def checker(value):
        pd.to_datetime(value, format=format)
    return checker
