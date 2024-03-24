
from _pytest.warning_types import PytestWarning

class ReturnTestWarning(PytestWarning):
    """
    A warning raised when a test function returns a value other than None,
    and strict return value checking is enabled.
    """
