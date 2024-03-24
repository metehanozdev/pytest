rst
.. _approx:

Floating point numbers comparison with approx
============================================

When dealing with floating point numbers in tests, direct equality comparisons can be problematic due to the way these numbers are represented in memory. As a solution, pytest offers the `approx` function which allows you to compare floating point numbers in a way that is tolerant of their inherent imprecision.

Using `approx`, you can assert that two numbers are approximately equal with a default relative tolerance of 1e-6.

Examples of `approx` usage:

.. code-block:: python

    def test_approx():
        assert 0.1 + 0.2 == pytest.approx(0.3)

You can specify the precision of the approximation by providing a tolerance:

.. code-block:: python

    def test_approx_with_tolerance():
        assert 0.1 + 0.2 == pytest.approx(0.3, rel=1e-9)

`approx` also supports comparisons of sequences like lists and tuples, as long as their elements are of numeric types:

.. code-block:: python

    def test_approx_sequences():
        assert [0.1 + 0.2] == pytest.approx([0.3])
        assert (0.1, 0.2) == pytest.approx((0.1, 0.2))

Unsupported Types
-----------------

As of the current version, `approx` no longer supports sets since they are not ordered and cannot meaningfully be used for approximate comparisons. Passing a set to `approx` will result in a `TypeError`.

An example of a type error with sets:

.. code-block:: python

    def test_approx_with_set():
        with pytest.raises(TypeError):
            assert {0.1, 0.2, 0.3} == pytest.approx({0.1, 0.2, 0.3})

Please ensure that you use only ordered collections like lists and tuples with `approx` for comparing sequences of numbers.

Note that `approx` is not intended to be used with non-numeric types such as strings or dictionaries.
