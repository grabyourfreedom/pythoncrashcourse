import unittest
from city_country import display_city


class CityTestCase(unittest.TestCase):
    def test_city_with_camel_case(self):
        input_city = "Chennai"
        input_country = "India"
        expected_output = "Chennai, India"
        actual_output = display_city(input_city, input_country)
        self.assertEqual(actual_output, expected_output)

    def test_city_with_all_caps(self):
        input_city = "CHENNAI"
        input_country = "INDIA"
        expected_output = "Chennai, India"
        actual_output = display_city(input_city, input_country)
        self.assertEqual(actual_output, expected_output)

    def test_city_with_lower_case(self):
        input_city = "chennai"
        input_country = "india"
        expected_output = "Chennai, India"
        actual_output = display_city(input_city, input_country)
        self.assertEqual(actual_output, expected_output)

    def test_city_with_mixed_case(self):
        input_city = "cHEnnai"
        input_country = "iNDia"
        expected_output = "Chennai, India"
        actual_output = display_city(input_city, input_country)
        self.assertEqual(actual_output, expected_output)

    def test_city_with_leading_trailing_whitespace(self):
        input_city = "Chennai "
        input_country = " India"
        expected_output = "Chennai, India"
        actual_output = display_city(input_city, input_country)
        self.assertEqual(actual_output, expected_output)

    def test_city_with_camel_case_population(self):
        input_city = "Chennai"
        input_country = "India"
        input_population = 1000000
        expected_output = "Chennai, India - population=1000000"
        actual_output = display_city(input_city, input_country, input_population)
        self.assertEqual(actual_output, expected_output)

    def test_city_with_all_caps_population(self):
        input_city = "CHENNAI"
        input_country = "INDIA"
        expected_output = "Chennai, India - population=1000000"
        input_population = 1000000
        actual_output = display_city(input_city, input_country, input_population)
        self.assertEqual(actual_output, expected_output)

    def test_city_with_lower_case_population(self):
        input_city = "chennai"
        input_country = "india"
        input_population = 1000000
        expected_output = "Chennai, India - population=1000000"
        actual_output = display_city(input_city, input_country, input_population)
        self.assertEqual(actual_output, expected_output)

    def test_city_with_mixed_case_population(self):
        input_city = "cHEnnai"
        input_country = "iNDia"
        expected_output = "Chennai, India - population=1000000"
        input_population = 1000000
        actual_output = display_city(input_city, input_country, input_population)
        self.assertEqual(actual_output, expected_output)

    def test_city_with_leading_trailing_whitespace_population(self):
        input_city = "Chennai "
        input_country = " India"
        expected_output = "Chennai, India - population=1000000"
        input_population = 1000000
        actual_output = display_city(input_city, input_country, input_population)
        self.assertEqual(actual_output, expected_output)


unittest.main()