import pytest

# py.test -s -v test_command_line_args.py --browser firefox

def test_command_line_methodA(oneTimeSetUp, setUp):
    print("Running method A")

def test_command_line_methodB(oneTimeSetUp, setUp):
    print("Running method B")