import pytest
from shopping_cart import checkout

# FIXTURE: This creates the data for us.
# scope="function" means every test gets a fresh copy of this list.
@pytest.fixture(scope="function")
def basic_cart():
    return [
        {"price": 10, "quantity": 2},
        {"price": 20, "quantity": 1},
        {"price": 30, "quantity": 3},
    ]

# PARAMETRIZATION: We define the scenarios (data) separately from the logic.
# argnames: "discount_code, expected_price"
# argvalues provided in the list.
@pytest.mark.parametrize("discount_code, expected_price", [
    (None, 60),          # Scenario 1: No discount
    ("HALO20", 48),      # Scenario 2: Valid discount (20% off 60 is 12, 60-12=48)
    ("INVALID", 60),     # Scenario 3: Invalid discount code (price stays same)
])
def test_checkout_scenarios(basic_cart, discount_code, expected_price):
    """
    This ONE function now covers 3 different test cases.
    We inject 'basic_cart' from the fixture, and 'discount_code/expected' from the parameters.
    """
    assert checkout(basic_cart, discount_code) == expected_price

# Edge case specific test
def test_empty_cart():
    assert checkout([]) == 0