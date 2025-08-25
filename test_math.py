def add(a, b):
    return a + b


def test_addition_correct():
    assert add(2, 3) == 5   # ✅ This will pass


def test_addition_incorrect():
    assert add(2, 2) == 5   # ❌ This will fail
