# encoding: utf-8
# module spwd
# from /usr/local/lib/python3.4/lib-dynload/spwd.cpython-34m.so
# by generator 1.135
"""
This module provides access to the Unix shadow password database.
It is available on various Unix versions.

Shadow password database entries are reported as 9-tuples of type struct_spwd,
containing the following items from the password database (see `<shadow.h>'):
sp_namp, sp_pwdp, sp_lstchg, sp_min, sp_max, sp_warn, sp_inact, sp_expire, sp_flag.
The sp_namp and sp_pwdp are strings, the rest are integers.
An exception is raised if the entry asked for cannot be found.
You have to be root to be able to use this module.
"""
# no imports

# functions

def getspall(): # real signature unknown; restored from __doc__
    """
    getspall() -> list_of_entries
    Return a list of all available shadow password database entries, in arbitrary order.
    See spwd.__doc__ for more on shadow password database entries.
    """
    pass

def getspnam(name): # real signature unknown; restored from __doc__
    """
    getspnam(name) -> (sp_namp, sp_pwdp, sp_lstchg, sp_min, sp_max,
                        sp_warn, sp_inact, sp_expire, sp_flag)
    Return the shadow password database entry for the given user name.
    See spwd.__doc__ for more on shadow password database entries.
    """
    pass

# classes

from .tuple import tuple

class struct_spwd(tuple):
    """
    spwd.struct_spwd: Results from getsp*() routines.
    
    This object may be accessed either as a 9-tuple of
      (sp_namp,sp_pwdp,sp_lstchg,sp_min,sp_max,sp_warn,sp_inact,sp_expire,sp_flag)
    or via the object attributes as named in the above tuple.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    sp_expire = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """#days since 1970-01-01 when account expires"""

    sp_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """reserved"""

    sp_inact = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """#days after pw expires until account is disabled"""

    sp_lstchg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """date of last change"""

    sp_max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """max #days between changes"""

    sp_min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """min #days between changes"""

    sp_nam = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """login name; deprecated"""

    sp_namp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """login name"""

    sp_pwd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """encrypted password; deprecated"""

    sp_pwdp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """encrypted password"""

    sp_warn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """#days before pw expires to warn user about it"""


    n_fields = 11
    n_sequence_fields = 9
    n_unnamed_fields = 0


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

