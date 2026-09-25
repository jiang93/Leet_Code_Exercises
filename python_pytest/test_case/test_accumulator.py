import pytest
from counter.accumulator import Accumulator

# unit test structure 
# - Arrange => prepare inputs, object, and any required steps
# - Act => call the function to perfrom the test case 
# - Assert => check that the actual result matches the expected result
# unit test design
# independent => each unit test should be run alone without depending on another test, and each test should focus one one behaviour or test outcome

@pytest.fixture()
def accum():
    return Accumulator() 

# intial count check
@pytest.mark.accumulator
def test_accumulator_init(accum):
    assert accum.count == 0 

# add count by 1 
@pytest.mark.accumulator
def test_accumulator_add_one(accum):
    accum.add() # Act
    assert accum.count == 1 # Assert

# add count by 3
@pytest.mark.accumulator
def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3
    
@pytest.mark.accumulator
def test_accumulator_error(accum):
    with pytest.raises (AttributeError, match = "property 'count' of 'Accumulator' object has no setter"): # Assert
        accum.count = 5 # Act


    

