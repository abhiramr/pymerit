import pytest
import pymerit

def test_noschema():
    """
    Test without schema 
    """
    with pytest.raises(pymerit.MeritInvalidSchema) as exc:
        class HelloMerit(pymerit.MeritBase):
            pass        
        h = HelloMerit()


def test_invalid_schema():
    """
    Test without schema 
    """
    with pytest.raises(pymerit.MeritInvalidSchema) as exc:
        class HelloMerit(pymerit.MeritBase):
            schema = {}
            def initialize(self):
                pass
            
            pass        
        h = HelloMerit()
        

def test_no_initialize():
    """
    Test without initialize
    """
    with pytest.raises(TypeError) as exc:
        class HelloMerit(pymerit.MeritBase):
            schema = 'hello' 

        h = HelloMerit()
        
        
