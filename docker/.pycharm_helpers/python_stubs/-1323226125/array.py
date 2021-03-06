# encoding: utf-8
# module array
# from /usr/local/lib/python3.4/lib-dynload/array.cpython-34m.so
# by generator 1.135
"""
This module defines an object type which can efficiently represent
an array of basic values: characters, integers, floating point
numbers.  Arrays are sequence types and behave very much like lists,
except that the type of objects stored in them is constrained.
"""
# no imports

# Variables with simple values

typecodes = 'bBuhHiIlLqQfd'

# functions

def _array_reconstructor(*args, **kwargs): # real signature unknown
    """ Internal. Used for pickling support. """
    pass

# classes

from .object import object

class ArrayType(object):
    """
    array(typecode [, initializer]) -> array
    
    Return a new array whose items are restricted by typecode, and
    initialized from the optional initializer value, which must be a list,
    string or iterable over elements of the appropriate type.
    
    Arrays represent basic values and behave very much like lists, except
    the type of objects stored in them is constrained. The type is specified
    at object creation time by using a type code, which is a single character.
    The following type codes are defined:
    
        Type code   C Type             Minimum size in bytes 
        'b'         signed integer     1 
        'B'         unsigned integer   1 
        'u'         Unicode character  2 (see note) 
        'h'         signed integer     2 
        'H'         unsigned integer   2 
        'i'         signed integer     2 
        'I'         unsigned integer   2 
        'l'         signed integer     4 
        'L'         unsigned integer   4 
        'q'         signed integer     8 (see note) 
        'Q'         unsigned integer   8 (see note) 
        'f'         floating point     4 
        'd'         floating point     8 
    
    NOTE: The 'u' typecode corresponds to Python's unicode character. On 
    narrow builds this is 2-bytes on wide builds this is 4-bytes.
    
    NOTE: The 'q' and 'Q' type codes are only available if the platform 
    C compiler used to build Python supports 'long long', or, on Windows, 
    '__int64'.
    
    Methods:
    
    append() -- append a new item to the end of the array
    buffer_info() -- return information giving the current memory info
    byteswap() -- byteswap all the items of the array
    count() -- return number of occurrences of an object
    extend() -- extend array by appending multiple elements from an iterable
    fromfile() -- read items from a file object
    fromlist() -- append items from the list
    frombytes() -- append items from the string
    index() -- return index of first occurrence of an object
    insert() -- insert a new item into the array at a provided position
    pop() -- remove and return item (default last)
    remove() -- remove first occurrence of an object
    reverse() -- reverse the order of the items in the array
    tofile() -- write all items to a file object
    tolist() -- return the array converted to an ordinary list
    tobytes() -- return the array converted to a string
    
    Attributes:
    
    typecode -- the typecode character used to create the array
    itemsize -- the length in bytes of one array item
    """
    def append(self, x): # real signature unknown; restored from __doc__
        """
        append(x)
        
        Append new value x to the end of the array.
        """
        pass

    def buffer_info(self): # real signature unknown; restored from __doc__
        """
        buffer_info() -> (address, length)
        
        Return a tuple (address, length) giving the current memory address and
        the length in items of the buffer used to hold array's contents
        The length should be multiplied by the itemsize attribute to calculate
        the buffer length in bytes.
        """
        pass

    def byteswap(self): # real signature unknown; restored from __doc__
        """
        byteswap()
        
        Byteswap all items of the array.  If the items in the array are not 1, 2,
        4, or 8 bytes in size, RuntimeError is raised.
        """
        pass

    def count(self, x): # real signature unknown; restored from __doc__
        """
        count(x)
        
        Return number of occurrences of x in the array.
        """
        pass

    def extend(self, array_or_iterable): # real signature unknown; restored from __doc__
        """
        extend(array or iterable)
        
         Append items to the end of the array.
        """
        pass

    def frombytes(self, bytestring): # real signature unknown; restored from __doc__
        """
        frombytes(bytestring)
        
        Appends items from the string, interpreting it as an array of machine
        values, as if it had been read from a file using the fromfile() method).
        """
        pass

    def fromfile(self, f, n): # real signature unknown; restored from __doc__
        """
        fromfile(f, n)
        
        Read n objects from the file object f and append them to the end of the
        array.
        """
        pass

    def fromlist(self, p_list): # real signature unknown; restored from __doc__
        """
        fromlist(list)
        
        Append items to array from list.
        """
        pass

    def fromstring(self, string): # real signature unknown; restored from __doc__
        """
        fromstring(string)
        
        Appends items from the string, interpreting it as an array of machine
        values, as if it had been read from a file using the fromfile() method).
        
        This method is deprecated. Use frombytes instead.
        """
        pass

    def fromunicode(self, ustr): # real signature unknown; restored from __doc__
        """
        fromunicode(ustr)
        
        Extends this array with data from the unicode string ustr.
        The array must be a unicode type array; otherwise a ValueError
        is raised.  Use array.frombytes(ustr.encode(...)) to
        append Unicode data to an array of some other type.
        """
        pass

    def index(self, x): # real signature unknown; restored from __doc__
        """
        index(x)
        
        Return index of first occurrence of x in the array.
        """
        pass

    def insert(self, i, x): # real signature unknown; restored from __doc__
        """
        insert(i,x)
        
        Insert a new item x into the array before position i.
        """
        pass

    def pop(self, i=None): # real signature unknown; restored from __doc__
        """
        pop([i])
        
        Return the i-th element and delete it from the array. i defaults to -1.
        """
        pass

    def remove(self, x): # real signature unknown; restored from __doc__
        """
        remove(x)
        
        Remove the first occurrence of x in the array.
        """
        pass

    def reverse(self): # real signature unknown; restored from __doc__
        """
        reverse()
        
        Reverse the order of the items in the array.
        """
        pass

    def tobytes(self): # real signature unknown; restored from __doc__
        """
        tobytes() -> bytes
        
        Convert the array to an array of machine values and return the bytes
        representation.
        """
        return b""

    def tofile(self, f): # real signature unknown; restored from __doc__
        """
        tofile(f)
        
        Write all items (as machine values) to the file object f.
        """
        pass

    def tolist(self): # real signature unknown; restored from __doc__
        """
        tolist() -> list
        
        Convert array to an ordinary list with the same items.
        """
        return []

    def tostring(self): # real signature unknown; restored from __doc__
        """
        tostring() -> bytes
        
        Convert the array to an array of machine values and return the bytes
        representation.
        
        This method is deprecated. Use tobytes instead.
        """
        return b""

    def tounicode(self): # real signature unknown; restored from __doc__
        """
        tounicode() -> unicode
        
        Convert the array to a unicode string.  The array must be
        a unicode type array; otherwise a ValueError is raised.  Use
        array.tobytes().decode() to obtain a unicode string from
        an array of some other type.
        """
        return ""

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        """
        copy(array)
        
         Return a copy of the array.
        """
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        """
        copy(array)
        
         Return a copy of the array.
        """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Implement self+=value. """
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Implement self*=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value.n """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """
        __sizeof__() -> int
        
        Size of the array in memory, in bytes.
        """
        return 0

    itemsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the size, in bytes, of one array item"""

    typecode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the typecode character used to create the array"""


    __hash__ = None


array = ArrayType


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

