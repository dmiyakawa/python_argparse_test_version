from contextlib import contextmanager
from io import StringIO
import unittest
import sys

from main import prepare_parser, __version__


@contextmanager
def capture_stdout(command, *args, **kwargs):
    out, sys.stdout = sys.stdout, StringIO()
    try:
        command(*args, **kwargs)
    finally:
        sys.stdout.seek(0)
        yield sys.stdout.read()
        sys.stdout = out


class MyTest(unittest.TestCase):
    def test_version(self):
        parser = prepare_parser()
        with self.assertRaises(SystemExit):
            with capture_stdout(parser.parse_args, ['-v']) as output:
                self.assertIsNotNone(output)
                self.assertEqual(__version__, output.rstrip())

        with self.assertRaises(SystemExit):
            with capture_stdout(parser.parse_args,
                                ['--version']) as output:
                self.assertIsNotNone(output)
                self.assertEqual(__version__, output.rstrip())


if __name__ == '__main__':
    unittest.main()
