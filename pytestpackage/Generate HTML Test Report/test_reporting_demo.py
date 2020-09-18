import pytest
from pytestpackage.class_to_test import SomeClassToTest

# py.test -s -v test_reporting_demo.py --browser firefox --html=htmlreport.html

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestReportingDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.abc = SomeClassToTest(10)

    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("Running method A")

    def test_methodB(self):
        result = self.abc.sumNumbers(2, 8)
        assert result > 20
        print("Running method B")