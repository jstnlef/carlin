import json
import unittest

from server import SampleSchema


class TestSampleSchemaValidation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('./problem_2/sample.json', 'r') as f:
            cls.sample_json = json.loads(f.read())

    def test_sample_validation_success(self):
        """
        Testing the standard validation flow with the example file
        """
        sample_json = self.sample_json.copy()
        result = SampleSchema().load(sample_json)
        self.assertFalse(result.errors)

    def test_sample_validation_extra_property(self):
        """
        Test to ensure that the added bogus_property is not included in the result data
        """
        sample_json = self.sample_json.copy()
        sample_json['bogus_property'] = 'meh'
        result = SampleSchema().load(sample_json)
        self.assertIsNone(result.data.get('bogus_property'))

    def test_sample_validation_missing_property(self):
        """
        Test verify that if a property is missing, the schema validation will produce errors in the
        results
        """
        sample_json = self.sample_json.copy()
        del sample_json['id']
        result = SampleSchema().load(sample_json)
        self.assertTrue(result.errors)
