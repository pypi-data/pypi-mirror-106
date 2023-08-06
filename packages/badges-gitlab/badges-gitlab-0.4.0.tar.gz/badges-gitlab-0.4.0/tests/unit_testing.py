import os
import re
import shutil
import sys
import unittest
from io import StringIO
from unittest.mock import patch

import xmlrunner

from src.badges_gitlab import __version__ as version
from src.badges_gitlab import (badges_api, badges_json, badges_svg,
                               badges_test, cli)

fixture_directory_not_exists = os.path.join(os.getcwd(), 'tests', 'test_not_exist')
fixture_json = os.path.join(os.getcwd(), 'tests', 'json')
fixture_svg_location = os.path.join(os.getcwd(), 'tests', 'svg')


class TestAPIBadges(unittest.TestCase):

    def test_validate_path(self):
        expected_value = 'Directory  {}  created!\n'.format(fixture_directory_not_exists)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            badges_api.validate_path(fixture_directory_not_exists)
            self.assertEqual(fake_out.getvalue(), expected_value)

    def tearDown(self) -> None:
        shutil.rmtree(fixture_directory_not_exists)


class TestBadgesJSON(unittest.TestCase):

    def test_print_json(self):
        expects = {"schemaVersion": 1, "label": "some", "message": "msg", "color": "different-color"}
        self.assertEqual(badges_json.print_json("some", "msg", "different-color"), expects)

    def test_json_badge(self):
        expects = {"schemaVersion": 1, "label": 'some', "message": 'msg', "color": 'different-color'}
        filename = "test"
        os.makedirs(fixture_json, exist_ok=True)
        with patch('sys.stdout', new=StringIO()):
            badges_json.json_badge(fixture_json, filename, expects)
            path_to_assert = os.path.join(fixture_json, '{0}.json'.format(filename))
            self.assertTrue(os.path.isfile(path_to_assert), 'Path tested was {0}'.format(path_to_assert))
        shutil.rmtree(fixture_json)


class TestBadgesSVG(unittest.TestCase):

    def test_replace_space(self):
        string_with_spaces = 'some string with spaces'
        expected_string = 'some_string_with_spaces'
        self.assertEqual(badges_svg.replace_space(string_with_spaces), expected_string)

    def test_validate_json_path(self):
        os.makedirs(fixture_svg_location, exist_ok=True)
        with open(os.path.join(fixture_svg_location, 'some.json'), 'w'):
            self.assertTrue(badges_svg.validate_json_path(fixture_svg_location))
        shutil.rmtree(fixture_svg_location)


class TestCLI(unittest.TestCase):

    def test_cli_parse_args_version(self):
        parser = cli.parse_args(['-V'])
        self.assertTrue(parser.version)

    def test_cli_main_version(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            try:
                sys.argv = ['prog', '-V']
                cli.main()
            except SystemExit:
                pass
            self.assertEqual(fake_out.getvalue(), 'badges-gitlab v{0}\n'.format(version) )


class TestBadgesTest(unittest.TestCase):

    json_test_directory = 'tests/fixtures'

    def test_create_badges_test(self):
        test_file_does_not_exist = unittest.TestCase.subTest
        with test_file_does_not_exist(self):
            xml_path = 'tests/report_not_exist.xml'
            self.assertEqual(badges_test.create_badges_test(self.json_test_directory, xml_path), 'Junit report file does not exist...skipping!')

        test_wrong_file_type = unittest.TestCase.subTest
        with test_wrong_file_type(self):
            file_path = 'Pipfile'
            self.assertEqual(badges_test.create_badges_test(self.json_test_directory, file_path), 'Error parsing the file. Is it a JUnit XML?')

        test_create_badges = unittest.TestCase.subTest
        with patch('sys.stdout', new=StringIO()):
            with test_create_badges(self):
                xml_path = 'tests/fixtures/report.xml'
                regex = re.search(r'Badges from JUnit XML test report tests created!', badges_test.create_badges_test(self.json_test_directory, xml_path))
                self.assertTrue(regex)

    def test_create_json_test_badges(self):
        with patch('sys.stdout', new=StringIO()):
            fixture_list = [11, 2, 0, 0, 0.014]
            total_passed = fixture_list[0] - sum(fixture_list[1:4])
            regex = re.search(r'Total Tests = {}, Passed = {}, Failed = {}, '
                              r'Errors = {}, Skipped = {}, Time = {:.2f}s.'.format(fixture_list[0], total_passed,
                                                                             fixture_list[1], fixture_list[2],
                                                                             fixture_list[3],fixture_list[4]),
                              badges_test.create_test_json_badges(self.json_test_directory, fixture_list))
            print()
            self.assertTrue(regex)

    def tearDown (self):
        files = os.listdir(self.json_test_directory)
        for file in files:
            if file.endswith('.json'):
                os.remove(os.path.join(self.json_test_directory, file))


if __name__ == '__main__':
    with open('report.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)
