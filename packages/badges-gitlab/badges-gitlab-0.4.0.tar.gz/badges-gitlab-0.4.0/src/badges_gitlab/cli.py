"""Main Package File, parses CLI arguments and calls functions"""
import argparse
import os
import sys

from . import __version__ as version
from .badges_api import create_api_badges
from .badges_svg import print_badges
from .badges_test import create_badges_test


def parse_args(args):
    """Create arguments and parse them returning already parsed arguments"""
    parser = argparse.ArgumentParser(prog='badges-gitlab',
                                     description='Generate Gitlab Badges using JSON files and API requests. '
                                                 'Program version v{0}.'.format(version))
    parser.add_argument('-p', '--path', type=str, metavar='TEXT', default=os.path.join(os.getcwd(), "public", "badges"),
                        help='path where json and badges files will be generated/located (default: ''./public/badges/)')
    parser.add_argument('-t', '--token', type=str, metavar='TEXT', default='',
                        help='specify the private-token in command line (default: ${PRIVATE_TOKEN})')
    parser.add_argument('--junit-xml', type=str, metavar='TEXT', default='', dest='junit',
                        help='specifies the path of a JUnit XML file for parsing the test results')
    parser.add_argument('-V', '--version', action='store_true', help='returns the package version')
    return parser.parse_args(args)


def main() -> None:
    """Main Function for calling arg parser and executing functions"""
    args = parse_args(sys.argv[1:])
    if args.version:
        print('badges-gitlab v{0}'.format(version))
        sys.exit()

    # Assign a environment variable if token was not provided
    if args.token == '':
        if not os.environ.get('PRIVATE_TOKEN') is None:
            args.token = os.environ['PRIVATE_TOKEN']

    # If a Junit File was pointed, executed the junit parser
    if not args.junit == '':
        create_badges_test(args.path, args.junit)
    # Call the API Badges Creator
    create_api_badges(args.path, args.token)
    print("Creating badges for files in directory", args.path)
    # Call the SVG Renderer
    print_badges(args.path)


if __name__ == "__main__":
    main()
