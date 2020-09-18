import pytest
from pytestpackage.class_to_test import SomeClassToTest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClassDemo():

    @pytest.fixture(autouse=True) #autouse=True makes fixture available to complete scope it's present in
    def classSetup(self):
        self.abc = SomeClassToTest(10)

    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("Running method A")

    def test_methodB(self):
        print("Running method B")