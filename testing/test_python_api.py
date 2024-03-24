
import pytest
from _pytest.python_api import approx
import numpy as np

class TestApprox:

    def test_error_messages_scalars_lists(self):
        # Test cases for scalars and lists
        with pytest.raises(AssertionError) as excinfo:
            assert 0 == approx(1)
        assert "not within the tolerance" in str(excinfo.value)

        with pytest.raises(AssertionError):
            assert [0.1, 0.2, 0.3] == approx([0.1, 0.2, 0.4])
    
    def test_error_messages_numpy(self):
        # Skip test if numpy is not available
        pytest.importorskip("numpy")

        # Test cases for numpy array comparisons
        with pytest.raises(AssertionError):
            assert np.array([1, 2, 3]) == approx(np.array([1, 2, 4]))

        with pytest.raises(AssertionError):
            assert np.array([np.nan, 2, 3]) == approx(np.array([1, 2, 3]))

        with pytest.raises(AssertionError):
            assert np.array([np.inf, 2, 3]) == approx(np.array([1, 2, 3]))

        with pytest.raises(AssertionError):
            assert np.array([1+1j, 2, 3]) == approx(np.array([1, 2, 3]))
