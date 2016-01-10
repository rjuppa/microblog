# encoding: utf-8
# module zlib
# from /usr/local/lib/python3.4/lib-dynload/zlib.cpython-34m.so
# by generator 1.135
"""
The functions in this module allow compression and decompression using the
zlib library, which is based on GNU zip.

adler32(string[, start]) -- Compute an Adler-32 checksum.
compress(string[, level]) -- Compress string, with compression level in 0-9.
compressobj([level[, ...]]) -- Return a compressor object.
crc32(string[, start]) -- Compute a CRC-32 checksum.
decompress(string,[wbits],[bufsize]) -- Decompresses a compressed string.
decompressobj([wbits[, zdict]]]) -- Return a decompressor object.

'wbits' is window buffer size.
Compressor objects support compress() and flush() methods; decompressor
objects support decompress() and flush().
"""
# no imports

# Variables with simple values

DEFLATED = 8

DEF_BUF_SIZE = 16384

DEF_MEM_LEVEL = 8

MAX_WBITS = 15

ZLIB_RUNTIME_VERSION = '1.2.8'

ZLIB_VERSION = '1.2.8'

Z_BEST_COMPRESSION = 9
Z_BEST_SPEED = 1

Z_DEFAULT_COMPRESSION = -1
Z_DEFAULT_STRATEGY = 0

Z_FILTERED = 1
Z_FINISH = 4

Z_FULL_FLUSH = 3

Z_HUFFMAN_ONLY = 2

Z_NO_FLUSH = 0

Z_SYNC_FLUSH = 2

__version__ = '1.0'

# functions

def adler32(*args, **kwargs): # real signature unknown
    """
    Compute an Adler-32 checksum of data.
    
      value
        Starting value of the checksum.
    
    The returned checksum is an integer.
    """
    pass

def compress(*args, **kwargs): # real signature unknown
    """
    Returns a bytes object containing compressed data.
    
      bytes
        Binary data to be compressed.
      level
        Compression level, in 0-9.
    """
    pass

def compressobj(*args, **kwargs): # real signature unknown
    """
    Return a compressor object.
    
      level
        The compression level (an integer in the range 0-9; default is 6).
        Higher compression levels are slower, but produce smaller results.
      method
        The compression algorithm.  If given, this must be DEFLATED.
      wbits
        The base two logarithm of the window size (range: 8..15).
      memLevel
        Controls the amount of memory used for internal compression state.
        Valid values range from 1 to 9.  Higher values result in higher memory
        usage, faster compression, and smaller output.
      strategy
        Used to tune the compression algorithm.  Possible values are
        Z_DEFAULT_STRATEGY, Z_FILTERED, and Z_HUFFMAN_ONLY.
      zdict
        The predefined compression dictionary - a sequence of bytes
        containing subsequences that are likely to occur in the input data.
    """
    pass

def crc32(*args, **kwargs): # real signature unknown
    """
    Compute a CRC-32 checksum of data.
    
      value
        Starting value of the checksum.
    
    The returned checksum is an integer.
    """
    pass

def decompress(*args, **kwargs): # real signature unknown
    """
    Returns a bytes object containing the uncompressed data.
    
      data
        Compressed data.
      wbits
        The window buffer size.
      bufsize
        The initial output buffer size.
    """
    pass

def decompressobj(*args, **kwargs): # real signature unknown
    """
    Return a decompressor object.
    
      wbits
        The window buffer size.
      zdict
        The predefined compression dictionary.  This must be the same
        dictionary as used by the compressor that produced the input data.
    """
    pass

# classes

from .Exception import Exception

class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

