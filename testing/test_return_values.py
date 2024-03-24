
import pytest
from _pytest.config import Config
from _pytest.nodes import Item

def pytest_addoption(parser):
    parser.addoption("--strict-return-values", action="store_true", help="Enforce no return value from test functions")

def pytest_collection_modifyitems(config, items):
    if config.getoption("--strict-return-values"):
        for item in items:
            def check_item(item=item):
                if hasattr(item.obj, "__wrapped__"):
                    return
                if item._itestrunresult is not None:
                    if item._itestrunresult.ret is not None:
                        pytest.fail("Test function returned non-None value", pytrace=False)

            item.addfinalizer(check_item)

@pytest.fixture
def return_value_testdir(testdir):
    testdir.makepyfile(test_code="""
        import pytest
        
        @pytest.mark.parametrize('value', [123, None, True])
        def test_return_values(value):
            return value
    """)
    return testdir

def test_return_values_cause_failure(return_value_testdir):
    result = return_value_testdir.runpytest("--strict-return-values")
    result.assert_outcomes(failed=1, passed=2)

def test_return_values_pass_without_warning(return_value_testdir):
    result = return_value_testdir.runpytest()
    result.assert_outcomes(passed=3)
