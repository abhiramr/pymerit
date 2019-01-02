"""
Utils
-----

Helper functions 
"""
import json

def all_subclasses(cls):
    """
    Find all subclasses of a class 

    :rtype: object
    :return: "Set of subclasses" 

    :param object cls: Baseclass 
    """
    return set(cls.__subclasses__()).union(
        [s for c in cls.__subclasses__() for s in all_subclasses(c)])

def get_metadata_attribute(name):
    
    @property
    def prop(self):
        return self.metadata[name] 
    
    @prop.setter
    def prop(self, value):
        self.metadata[name] = value 

    return prop 

def new(metadata):
    """
    Create Merit object from dictionary
    """

    from pymerit import MeritBase
    
    cls = MeritBase.find_handler_for_dict(metadata)
    obj = cls() 
    obj.load(metadata)
    return obj 
    
def news(metadatastr):
    """
    Create Merit object from JSON string 
    """
    metadata = json.loads(metadatastr)
    return new(metadata) 
