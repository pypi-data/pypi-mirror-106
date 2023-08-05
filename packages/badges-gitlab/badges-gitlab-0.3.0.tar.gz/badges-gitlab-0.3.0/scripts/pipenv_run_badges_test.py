"""Parse Report File to obtain tests information and generate a badge file"""
import os.path
import re
import anybadge

# Report File and Badge Destination.
filename = "tests/report.xml"
directory = "public/badges/"
badge_name = "test_summary.svg"


def main():
    total_tests = 0
    total_failures = 0
    total_errors_skipped = 0
    if not os.path.isfile(filename):
        print('File does not exist.')
    else:
        with open(filename) as f:
            content = f.read().splitlines()
        for line in content:
            try:
                re_match = re.match(r'^.*?<testsuite.*?tests="(\d{1,3})".*?failures="(\d{1,3})".*?'
                                    r'errors="(\d{1,3})".*?skipped="(\d{1,3})"', line)
                total = int(re_match.group(1))
                total_tests = total_tests + total
                failures = int(re_match.group(2))
                skipped_errors = int(re_match.group(3)) + int(re_match.group(4))
                total_errors_skipped = total_errors_skipped + skipped_errors
                total_failures = total_failures + failures
            except AttributeError:
                pass
    total_passed = total_tests - total_failures - total_errors_skipped
    print("Total Tests = {0}, Passed = {1}, Failed = {2}".format(total_tests, total_passed, total_failures))
    if total_failures > 0:
        color = 'red'
        badge_value = '{0} Passed, {1} Failed'.format(total_passed, total_failures)
    else:
        color = 'green'
        badge_value = '{0} Passed'.format(total_passed)
    if not os.path.isdir(directory):
        try:
            # Create  Directory MyDirectory
            os.makedirs(directory)
        except FileExistsError:
            pass
    test_summary = os.path.join(directory, badge_name)
    anybadge.Badge(label='tests', value=badge_value,
                   default_color=color).write_badge(test_summary, overwrite=True)


if __name__ == "__main__":
    main()
