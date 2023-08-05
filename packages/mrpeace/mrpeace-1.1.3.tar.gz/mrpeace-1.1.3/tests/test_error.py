#!/usr/bin/env python3

import unittest
from click.testing import CliRunner
from mrpeace import cli


class TestError(unittest.TestCase):
    def test_notification(self):
        runner = CliRunner()
        result = runner.invoke(cli.hi, ["hi"])
        assert result.exception

    def test_email(self):
        runner = CliRunner()
        result = runner.invoke(cli.automail, ["user, password"])
        assert result.exception


if __name__ == "__main__":
    unittest.main()
