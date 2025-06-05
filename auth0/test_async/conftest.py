import pytest
import random

@pytest.fixture(autouse=True)
def set_random_seed():
    random.seed(42)
    print("Random seeded to 42")