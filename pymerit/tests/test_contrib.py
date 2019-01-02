import pytest
import pymerit

def test_platform():
    """
    Test whether platform context object can be created
    """

    h = pymerit.MeritContextPlatform()
    h.validate() 
