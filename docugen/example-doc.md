# Documentation for `example/example_code.py`

### `add(add1, add2)`
# The add function takes two inputs, adds them together, and returns the result.
# Input: add1 (any number), add2 (any number)
# Output: the sum of add1 and add2

def test_add():
    assert add(0, 0) == 0
    assert add(5, 7) == 12
    assert add(-3, 9) == 6
    assert add(2.5, 1.75) == 4.25
    assert add(10, -10) == 0


