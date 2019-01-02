"""
Exceptions 
----------

"""
class MeritNoHandler(Exception):
    """
    Not class to handle metadata with a given schema
    """
    pass

class MeritInvalidSchema(Exception):
    """
    Invalid schema definition 
    """
    pass

class MeritMissingSchema(Exception):
    """
    Schema not defined in the given merit subclass 
    """
    pass

class MeritInvalidMetadata(Exception):
    """
    Metadata cannot be loaded due to missing fields 
    """
    pass

class MeritInvalidContext(Exception):
    """
    Invalid class specified while adding context
    """
    pass

class MeritInvalidResource(Exception):
    """
    Invalid class specified while adding resource 
    """    
    pass
