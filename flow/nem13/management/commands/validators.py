import sys
from functools import partial
from datetime import datetime
from csvvalidator import *
from operator import eq, itemgetter

class Validator:

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
        self.validator.add_value_check('RecordIndicator', partial(eq,100))
        self.validator.add_value_check('VersionHeader', check_length(2))
        self.add_value_check('DateTime', check_datetime_not_future)
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


        super(HeaderValidator, self).__init__(data, field_names)

class  B2BDetailsValidator(Validator):

    def __init__(self, data):
        field_names = [
            'RecordIndicator',
            'PreviousTransCode',
            'PreviousRetServiceOrder',
            'CurrentTransCode',
            'CurrentRetServiceOrder'
        ]
        super(B2BDetailsValidator, self).__init__(data, field_names)

class EndValidator(Validator):
    def __init__(self, data):
        field_names = ['RecordIndicator']
        super(EndValidator, self).__init__(data, field_names)
        self.validator.add_value_check('RecordIndicator', partial(eq(900)))



class NEM13Validator(Validator):
    def __init__(self, data):
       self.data = data

    def validate(self):
        return check_blocking_cycle(self.data)


def check_blocking_cycle(data):
    problems = []
    if len(data) < 3:
           problems.append("The flow does have the requirement flow")

    column = [row[0] for row in data]

    if column[0] != '100':
        problems.append(f'The flow should start with code of Header Record but found{column[0]}')

    if column[-1] != '900':
        problems.append(f"The flow should end with code of End but found{data[-1]}")
    record_identifier_unknown = list(filter(lambda value: value[1] not in ['100', '250', '500', '900'],
                                            enumerate(map(itemgetter(0), data), 1)))

    if record_identifier_unknown:

        problems.append(f"RecordIndicator unknown {','.join([ f'row:{index} value:{value}' for index, value in record_identifier_unknown])}")

    if len(list(filter(partial(eq, '900'), column))) > 1:
        problems.append(f'The flow should had one End Record')
    return problems



def check_length(limit):
    def checker(value):
        if len(value) > limit:
            raise ValueError(value)
    return checker

def check_datetime_not_future(value):
    try:
        datetime_value = datetime.strptime(value, '%Y%m%d%H%M')
    except Exception:
        raise ValueError
    if datetime_value > datetime.now():
        raise ValueError


class AccumulationMeterDataValidator:
    pass


class FlowException(RecordError):
    def __init__(self, code, message, detail):
        super(FlowException, self).__init__(code, message, detail)