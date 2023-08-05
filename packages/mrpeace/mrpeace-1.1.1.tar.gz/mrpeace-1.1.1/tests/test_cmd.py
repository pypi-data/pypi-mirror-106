#!/usr/bin/env python3

import unittest
from click.testing import CliRunner
from mrpeace import cli


class TestCommand(unittest.TestCase):
    def test_callback(self):
        runner = CliRunner()
        result = runner.invoke(cli.hi, ["hi"])
        assert result.exit_code == 2


if __name__ == "__main__":
    unittest.main()
