import os
import sys
import shutil
import unittest
from io import StringIO
from unittest.mock import patch

import xmlrunner

from src.badges_gitlab import __version__ as version
from src.badges_gitlab import badges_api, badges_json, badges_svg, cli

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


if __name__ == '__main__':
    with open('report.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)
