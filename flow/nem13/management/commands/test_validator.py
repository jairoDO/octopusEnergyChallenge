import unittest
from validators import HeaderValidator, NEM13Validator
from io import StringIO
from csvvalidator import write_problems

class ValidatorTestCase(unittest.TestCase):
    def test_csv_valid(self):
        data = [['100', 'NEM13', '200401101030', 'MDA1', 'Ret1']]
        self.head_validation = HeaderValidator(data)
        self.assertEqual([], self.head_validation.validate())  # add assertion here

    def test_csv_not_valid(self):
        data = [['100', 'NEM13', '200401101030', 'MDA1', 'Ret1']]
        self.head_validation = HeaderValidator(data)
        self.assertEqual([], self.head_validation.validate())  # add assertion here

    def test_valid_flow(self):
        data = [
            ['100', 'NEM13', '200401101030', 'MDA1', 'Ret1'],
            "250	2291137510	11	1	11	11	R4ZFLS6ZY1UV	E	55893.0	20031015100333	A			56311.0	20040107100333	A			418.0	kWh	20040331	20040108100333	20040108090333 250	7142747824".split("	"),
            ["900"]
        ]
        validator = NEM13Validator(data)
        problems = validator.validate()
        self.assertEqual([], problems)

    def test_invalid_flow(self):
        data = [
            ['100', 'NEM13', '200401101030', 'MDA1', 'Ret1'],
            "251 2291137510c11 1 11 11 R4ZFLS6ZY1UV E 55893.0 20031015100333 A     56311.0 20040107100333 A     418.0 kWh 20040331 20040108100333 20040108090333 250 7142747824".split(" "),
            ["900"]
        ]
        validator = NEM13Validator(data)
        problems = validator.validate()
        self.assertEqual(1, len(problems), "the flow is not correct and should be show 1 error in the second RecordItendifu")

if __name__ == '__main__':
    unittest.main()
