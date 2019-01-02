class X:
    var = [1,2]

    def __init_subclass__(cls):
        attr_name = 'var'
        if not attr_name in cls.__dict__:
            raise NotImplementedError(
                "Attribute '{}' has not been overriden in class '{}'" \
                .format(attr_name, cls.__name__)
            )
