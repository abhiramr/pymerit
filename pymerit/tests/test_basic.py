import pytest
import pymerit 

def test_non_existent():
    """
    Test non-existent schema handler
    """
    with pytest.raises(pymerit.MeritNoHandler) as exc:
        pymerit.MeritBase.find_handler("hello")

def test_existent():
    """
    Testing default metadata
    """
        
    assert pymerit.MeritBase.find_handler("global:default:v1") is not None
    assert pymerit.MeritBase.find_handler("global:default:v1") == pymerit.MeritDefault


            
