# encoding: utf-8
# module _decimal calls itself decimal
# from /usr/local/lib/python3.4/lib-dynload/_decimal.cpython-34m.so
# by generator 1.135
""" C decimal arithmetic module """

# imports
import decimal as __decimal


# Variables with simple values

HAVE_THREADS = True

MAX_EMAX = 999999999999999999
MAX_PREC = 999999999999999999

MIN_EMIN = -999999999999999999
MIN_ETINY = -1999999999999999997

ROUND_05UP = 'ROUND_05UP'
ROUND_CEILING = 'ROUND_CEILING'
ROUND_DOWN = 'ROUND_DOWN'
ROUND_FLOOR = 'ROUND_FLOOR'

ROUND_HALF_DOWN = 'ROUND_HALF_DOWN'
ROUND_HALF_EVEN = 'ROUND_HALF_EVEN'
ROUND_HALF_UP = 'ROUND_HALF_UP'

ROUND_UP = 'ROUND_UP'

__libmpdec_version__ = '2.4.1'

__version__ = '1.70'

# functions

def getcontext(): # real signature unknown; restored from __doc__
    """ getcontext() - Get the current default context. """
    pass

def localcontext(ctx=None): # real signature unknown; restored from __doc__
    """
    localcontext(ctx=None) - Return a context manager that will set the default
    context to a copy of ctx on entry to the with-statement and restore the
    previous default context when exiting the with-statement. If no context is
    specified, a copy of the current default context is used.
    """
    pass

def setcontext(c): # real signature unknown; restored from __doc__
    """ setcontext(c) - Set a new default context. """
    pass

# classes

from .ArithmeticError import ArithmeticError

class DecimalException(ArithmeticError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Clamped(__decimal.DecimalException):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


from .object import object

class Context(object):
    """
    The context affects almost all operations and controls rounding,
    Over/Underflow, raising of exceptions and much more. A new context
    can be constructed as follows:
    
        >>> c = Context(prec=28, Emin=-425000000, Emax=425000000,
        ...             rounding=ROUND_HALF_EVEN, capitals=1, clamp=1,
        ...             traps=[InvalidOperation, DivisionByZero, Overflow],
        ...             flags=[])
        >>>
    """
    def abs(self, x): # real signature unknown; restored from __doc__
        """ abs(x) - Return the absolute value of x. """
        pass

    def add(self, x, y): # real signature unknown; restored from __doc__
        """ add(x, y) - Return the sum of x and y. """
        pass

    def canonical(self, x): # real signature unknown; restored from __doc__
        """ canonical(x) - Return a new instance of x. """
        pass

    def clear_flags(self): # real signature unknown; restored from __doc__
        """ clear_flags() - Reset all flags to False. """
        pass

    def clear_traps(self): # real signature unknown; restored from __doc__
        """ clear_traps() - Set all traps to False. """
        pass

    def compare(self, x, y): # real signature unknown; restored from __doc__
        """ compare(x, y) - Compare x and y numerically. """
        pass

    def compare_signal(self, x, y): # real signature unknown; restored from __doc__
        """ compare_signal(x, y) - Compare x and y numerically. All NaNs signal. """
        pass

    def compare_total(self, x, y): # real signature unknown; restored from __doc__
        """ compare_total(x, y) - Compare x and y using their abstract representation. """
        pass

    def compare_total_mag(self, x, y): # real signature unknown; restored from __doc__
        """
        compare_total_mag(x, y) - Compare x and y using their abstract representation,
        ignoring sign.
        """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy() - Return a duplicate of the context with all flags cleared. """
        pass

    def copy_abs(self, x): # real signature unknown; restored from __doc__
        """ copy_abs(x) - Return a copy of x with the sign set to 0. """
        pass

    def copy_decimal(self, x): # real signature unknown; restored from __doc__
        """ copy_decimal(x) - Return a copy of Decimal x. """
        pass

    def copy_negate(self, x): # real signature unknown; restored from __doc__
        """ copy_negate(x) - Return a copy of x with the sign inverted. """
        pass

    def copy_sign(self, x, y): # real signature unknown; restored from __doc__
        """ copy_sign(x, y) - Copy the sign from y to x. """
        pass

    def create_decimal(self, x): # real signature unknown; restored from __doc__
        """
        create_decimal(x) - Create a new Decimal instance from x, using self as the
        context. Unlike the Decimal constructor, this function observes the context
        limits.
        """
        pass

    def create_decimal_from_float(self, f): # real signature unknown; restored from __doc__
        """
        create_decimal_from_float(f) - Create a new Decimal instance from float f.
        Unlike the Decimal.from_float() class method, this function observes the
        context limits.
        """
        pass

    def divide(self, x, y): # real signature unknown; restored from __doc__
        """ divide(x, y) - Return x divided by y. """
        pass

    def divide_int(self, x, y): # real signature unknown; restored from __doc__
        """ divide_int(x, y) - Return x divided by y, truncated to an integer. """
        pass

    def divmod(self, x, y): # real signature unknown; restored from __doc__
        """ divmod(x, y) - Return quotient and remainder of the division x / y. """
        pass

    def Etiny(self): # real signature unknown; restored from __doc__
        """
        Etiny() - Return a value equal to Emin - prec + 1, which is the minimum
        exponent value for subnormal results. When underflow occurs, the exponent
        is set to Etiny.
        """
        pass

    def Etop(self): # real signature unknown; restored from __doc__
        """
        Etop() - Return a value equal to Emax - prec + 1. This is the maximum exponent
        if the _clamp field of the context is set to 1 (IEEE clamp mode). Etop() must
        not be negative.
        """
        pass

    def exp(self, x): # real signature unknown; restored from __doc__
        """ exp(x) - Return e ** x. """
        pass

    def fma(self, x, y, z): # real signature unknown; restored from __doc__
        """ fma(x, y, z) - Return x multiplied by y, plus z. """
        pass

    def is_canonical(self, x): # real signature unknown; restored from __doc__
        """ is_canonical(x) - Return True if x is canonical, False otherwise. """
        pass

    def is_finite(self, x): # real signature unknown; restored from __doc__
        """ is_finite(x) - Return True if x is finite, False otherwise. """
        pass

    def is_infinite(self, x): # real signature unknown; restored from __doc__
        """ is_infinite(x) - Return True if x is infinite, False otherwise. """
        pass

    def is_nan(self, x): # real signature unknown; restored from __doc__
        """ is_nan(x) - Return True if x is a qNaN or sNaN, False otherwise. """
        pass

    def is_normal(self, x): # real signature unknown; restored from __doc__
        """ is_normal(x) - Return True if x is a normal number, False otherwise. """
        pass

    def is_qnan(self, x): # real signature unknown; restored from __doc__
        """ is_qnan(x) - Return True if x is a quiet NaN, False otherwise. """
        pass

    def is_signed(self, x): # real signature unknown; restored from __doc__
        """ is_signed(x) - Return True if x is negative, False otherwise. """
        pass

    def is_snan(self): # real signature unknown; restored from __doc__
        """ is_snan() - Return True if x is a signaling NaN, False otherwise. """
        pass

    def is_subnormal(self, x): # real signature unknown; restored from __doc__
        """ is_subnormal(x) - Return True if x is subnormal, False otherwise. """
        pass

    def is_zero(self, x): # real signature unknown; restored from __doc__
        """ is_zero(x) - Return True if x is a zero, False otherwise. """
        pass

    def ln(self, x): # real signature unknown; restored from __doc__
        """ ln(x) - Return the natural (base e) logarithm of x. """
        pass

    def log10(self, x): # real signature unknown; restored from __doc__
        """ log10(x) - Return the base 10 logarithm of x. """
        pass

    def logb(self, x): # real signature unknown; restored from __doc__
        """ logb(x) - Return the exponent of the magnitude of the operand's MSD. """
        pass

    def logical_and(self, x, y): # real signature unknown; restored from __doc__
        """ logical_and(x, y) - Digit-wise and of x and y. """
        pass

    def logical_invert(self, x): # real signature unknown; restored from __doc__
        """ logical_invert(x) - Invert all digits of x. """
        pass

    def logical_or(self, x, y): # real signature unknown; restored from __doc__
        """ logical_or(x, y) - Digit-wise or of x and y. """
        pass

    def logical_xor(self, x, y): # real signature unknown; restored from __doc__
        """ logical_xor(x, y) - Digit-wise xor of x and y. """
        pass

    def max(self, x, y): # real signature unknown; restored from __doc__
        """ max(x, y) - Compare the values numerically and return the maximum. """
        pass

    def max_mag(self, x, y): # real signature unknown; restored from __doc__
        """ max_mag(x, y) - Compare the values numerically with their sign ignored. """
        pass

    def min(self, x, y): # real signature unknown; restored from __doc__
        """ min(x, y) - Compare the values numerically and return the minimum. """
        pass

    def minus(self, x): # real signature unknown; restored from __doc__
        """
        minus(x) - Minus corresponds to the unary prefix minus operator in Python,
        but applies the context to the result.
        """
        pass

    def min_mag(self, x, y): # real signature unknown; restored from __doc__
        """ min_mag(x, y) - Compare the values numerically with their sign ignored. """
        pass

    def multiply(self, x, y): # real signature unknown; restored from __doc__
        """ multiply(x, y) - Return the product of x and y. """
        pass

    def next_minus(self, x): # real signature unknown; restored from __doc__
        """ next_minus(x) - Return the largest representable number smaller than x. """
        pass

    def next_plus(self, x): # real signature unknown; restored from __doc__
        """ next_plus(x) - Return the smallest representable number larger than x. """
        pass

    def next_toward(self, x): # real signature unknown; restored from __doc__
        """ next_toward(x) - Return the number closest to x, in the direction towards y. """
        pass

    def normalize(self, x): # real signature unknown; restored from __doc__
        """ normalize(x) - Reduce x to its simplest form. Alias for reduce(x). """
        pass

    def number_class(self, x): # real signature unknown; restored from __doc__
        """ number_class(x) - Return an indication of the class of x. """
        pass

    def plus(self, x): # real signature unknown; restored from __doc__
        """
        plus(x) - Plus corresponds to the unary prefix plus operator in Python,
        but applies the context to the result.
        """
        pass

    def power(self, x, y): # real signature unknown; restored from __doc__
        """
        power(x, y) - Compute x**y. If x is negative, then y must be integral.
        The result will be inexact unless y is integral and the result is finite
        and can be expressed exactly in 'precision' digits. In the Python version
        the result is always correctly rounded, in the C version the result is
        almost always correctly rounded.
        
        power(x, y, m) - Compute (x**y) % m. The following restrictions hold:
        
            * all three arguments must be integral
            * y must be nonnegative
            * at least one of x or y must be nonzero
            * m must be nonzero and less than 10**prec in absolute value
        """
        pass

    def quantize(self, x, y): # real signature unknown; restored from __doc__
        """ quantize(x, y) - Return a value equal to x (rounded), having the exponent of y. """
        pass

    def radix(self): # real signature unknown; restored from __doc__
        """ radix() - Return 10. """
        pass

    def remainder(self, x, y): # real signature unknown; restored from __doc__
        """
        remainder(x, y) - Return the remainder from integer division. The sign of
        the result, if non-zero, is the same as that of the original dividend.
        """
        pass

    def remainder_near(self, x, y): # real signature unknown; restored from __doc__
        """
        remainder_near(x, y) - Return x - y * n, where n is the integer nearest the
        exact value of x / y (if the result is 0 then its sign will be the sign of x).
        """
        pass

    def rotate(self, x, y): # real signature unknown; restored from __doc__
        """ rotate(x, y) - Return a copy of x, rotated by y places. """
        pass

    def same_quantum(self, x, y): # real signature unknown; restored from __doc__
        """ same_quantum(x, y) - Return True if the two operands have the same exponent. """
        pass

    def scaleb(self, x, y): # real signature unknown; restored from __doc__
        """
        scaleb(x, y) - Return the first operand after adding the second value
        to its exp.
        """
        pass

    def shift(self, x, y): # real signature unknown; restored from __doc__
        """ shift(x, y) - Return a copy of x, shifted by y places. """
        pass

    def sqrt(self, x): # real signature unknown; restored from __doc__
        """ sqrt(x) - Square root of a non-negative number to context precision. """
        pass

    def subtract(self, x, y): # real signature unknown; restored from __doc__
        """ subtract(x, y) - Return the difference between x and y. """
        pass

    def to_eng_string(self, x): # real signature unknown; restored from __doc__
        """ to_eng_string(x) - Convert a number to a string, using engineering notation. """
        pass

    def to_integral(self, x): # real signature unknown; restored from __doc__
        """ to_integral(x) - Identical to to_integral_value(x). """
        pass

    def to_integral_exact(self, x): # real signature unknown; restored from __doc__
        """
        to_integral_exact(x) - Round to an integer. Signal if the result is
        rounded or inexact.
        """
        pass

    def to_integral_value(self, x): # real signature unknown; restored from __doc__
        """ to_integral_value(x) - Round to an integer. """
        pass

    def to_sci_string(self, x): # real signature unknown; restored from __doc__
        """ to_sci_string(x) - Convert a number to a string using scientific notation. """
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, prec=28, Emin=-425000000, Emax=425000000, *more, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
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

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    capitals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    clamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Emax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Emin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class InvalidOperation(__decimal.DecimalException):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ConversionSyntax(__decimal.InvalidOperation):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


from .object import object

class Decimal(object):
    """
    Decimal(value="0", context=None): Construct a new Decimal object.
    value can be an integer, string, tuple, or another Decimal object.
    If no value is given, return Decimal('0'). The context does not affect
    the conversion and is only passed to determine if the InvalidOperation
    trap is active.
    """
    def adjusted(self): # real signature unknown; restored from __doc__
        """
        adjusted() - Return the adjusted exponent of the number.
        
        Defined as exp + digits - 1.
        """
        pass

    def as_tuple(self): # real signature unknown; restored from __doc__
        """ as_tuple() - Return a tuple representation of the number. """
        pass

    def canonical(self): # real signature unknown; restored from __doc__
        """
        canonical() - Return the canonical encoding of the argument. Currently,
        the encoding of a Decimal instance is always canonical, so this operation
        returns its argument unchanged.
        """
        pass

    def compare(self, other, context=None): # real signature unknown; restored from __doc__
        """
        compare(other, context=None) - Compare self to other. Return a decimal value:
        
            a or b is a NaN ==> Decimal('NaN')
            a < b           ==> Decimal('-1')
            a == b          ==> Decimal('0')
            a > b           ==> Decimal('1')
        """
        pass

    def compare_signal(self, other, context=None): # real signature unknown; restored from __doc__
        """
        compare_signal(other, context=None) - Identical to compare, except that
        all NaNs signal.
        """
        pass

    def compare_total(self, other, context=None): # real signature unknown; restored from __doc__
        """
        compare_total(other, context=None) - Compare two operands using their
        abstract representation rather than their numerical value. Similar to the
        compare() method, but the result gives a total ordering on Decimal instances.
        Two Decimal instances with the same numeric value but different representations
        compare unequal in this ordering:
        
            >>> Decimal('12.0').compare_total(Decimal('12'))
            Decimal('-1')
        
        Quiet and signaling NaNs are also included in the total ordering. The result
        of this function is Decimal('0') if both operands have the same representation,
        Decimal('-1') if the first operand is lower in the total order than the second,
        and Decimal('1') if the first operand is higher in the total order than the
        second operand. See the specification for details of the total order.
        
        This operation is unaffected by context and is quiet: no flags are changed
        and no rounding is performed. As an exception, the C version may raise
        InvalidOperation if the second operand cannot be converted exactly.
        """
        pass

    def compare_total_mag(self, other, context=None): # real signature unknown; restored from __doc__
        """
        compare_total_mag(other, context=None) - Compare two operands using their
        abstract representation rather than their value as in compare_total(), but
        ignoring the sign of each operand. x.compare_total_mag(y) is equivalent to
        x.copy_abs().compare_total(y.copy_abs()).
        
        This operation is unaffected by context and is quiet: no flags are changed
        and no rounding is performed. As an exception, the C version may raise
        InvalidOperation if the second operand cannot be converted exactly.
        """
        pass

    def conjugate(self): # real signature unknown; restored from __doc__
        """ conjugate() - Return self. """
        pass

    def copy_abs(self): # real signature unknown; restored from __doc__
        """
        copy_abs() - Return the absolute value of the argument. This operation
        is unaffected by context and is quiet: no flags are changed and no rounding
        is performed.
        """
        pass

    def copy_negate(self): # real signature unknown; restored from __doc__
        """
        copy_negate() - Return the negation of the argument. This operation is
        unaffected by context and is quiet: no flags are changed and no rounding
        is performed.
        """
        pass

    def copy_sign(self, other, context=None): # real signature unknown; restored from __doc__
        """
        copy_sign(other, context=None) - Return a copy of the first operand with
        the sign set to be the same as the sign of the second operand. For example:
        
            >>> Decimal('2.3').copy_sign(Decimal('-1.5'))
            Decimal('-2.3')
        
        This operation is unaffected by context and is quiet: no flags are changed
        and no rounding is performed. As an exception, the C version may raise
        InvalidOperation if the second operand cannot be converted exactly.
        """
        pass

    def exp(self, context=None): # real signature unknown; restored from __doc__
        """
        exp(context=None) - Return the value of the (natural) exponential function
        e**x at the given number. The function always uses the ROUND_HALF_EVEN mode
        and the result is correctly rounded.
        """
        pass

    def fma(self, other, third, context=None): # real signature unknown; restored from __doc__
        """
        fma(other, third, context=None) - Fused multiply-add. Return self*other+third
        with no rounding of the intermediate product self*other.
        
            >>> Decimal(2).fma(3, 5)
            Decimal('11')
        """
        pass

    @classmethod
    def from_float(cls, f): # real signature unknown; restored from __doc__
        """
        from_float(f) - Class method that converts a float to a decimal number, exactly.
        Since 0.1 is not exactly representable in binary floating point,
        Decimal.from_float(0.1) is not the same as Decimal('0.1').
        
            >>> Decimal.from_float(0.1)
            Decimal('0.1000000000000000055511151231257827021181583404541015625')
            >>> Decimal.from_float(float('nan'))
            Decimal('NaN')
            >>> Decimal.from_float(float('inf'))
            Decimal('Infinity')
            >>> Decimal.from_float(float('-inf'))
            Decimal('-Infinity')
        """
        pass

    def is_canonical(self): # real signature unknown; restored from __doc__
        """
        is_canonical() - Return True if the argument is canonical and False otherwise.
        Currently, a Decimal instance is always canonical, so this operation always
        returns True.
        """
        pass

    def is_finite(self): # real signature unknown; restored from __doc__
        """
        is_finite() - Return True if the argument is a finite number, and False if the
        argument is infinite or a NaN.
        """
        pass

    def is_infinite(self): # real signature unknown; restored from __doc__
        """
        is_infinite() - Return True if the argument is either positive or negative
        infinity and False otherwise.
        """
        pass

    def is_nan(self): # real signature unknown; restored from __doc__
        """
        is_nan() - Return True if the argument is a (quiet or signaling) NaN and
        False otherwise.
        """
        pass

    def is_normal(self, context=None): # real signature unknown; restored from __doc__
        """
        is_normal(context=None) - Return True if the argument is a normal finite
        non-zero number with an adjusted exponent greater than or equal to Emin.
        Return False if the argument is zero, subnormal, infinite or a NaN.
        """
        pass

    def is_qnan(self): # real signature unknown; restored from __doc__
        """ is_qnan() - Return True if the argument is a quiet NaN, and False otherwise. """
        pass

    def is_signed(self): # real signature unknown; restored from __doc__
        """
        is_signed() - Return True if the argument has a negative sign and
        False otherwise. Note that both zeros and NaNs can carry signs.
        """
        pass

    def is_snan(self): # real signature unknown; restored from __doc__
        """ is_snan() - Return True if the argument is a signaling NaN and False otherwise. """
        pass

    def is_subnormal(self, context=None): # real signature unknown; restored from __doc__
        """
        is_subnormal(context=None) - Return True if the argument is subnormal, and
        False otherwise. A number is subnormal if it is non-zero, finite, and has an
        adjusted exponent less than Emin.
        """
        pass

    def is_zero(self): # real signature unknown; restored from __doc__
        """
        is_zero() - Return True if the argument is a (positive or negative) zero and
        False otherwise.
        """
        pass

    def ln(self, context=None): # real signature unknown; restored from __doc__
        """
        ln(context=None) - Return the natural (base e) logarithm of the operand.
        The function always uses the ROUND_HALF_EVEN mode and the result is
        correctly rounded.
        """
        pass

    def log10(self, context=None): # real signature unknown; restored from __doc__
        """
        log10(context=None) - Return the base ten logarithm of the operand.
        The function always uses the ROUND_HALF_EVEN mode and the result is
        correctly rounded.
        """
        pass

    def logb(self, context=None): # real signature unknown; restored from __doc__
        """
        logb(context=None) - For a non-zero number, return the adjusted exponent
        of the operand as a Decimal instance. If the operand is a zero, then
        Decimal('-Infinity') is returned and the DivisionByZero condition is
        raised. If the operand is an infinity then Decimal('Infinity') is returned.
        """
        pass

    def logical_and(self, other, context=None): # real signature unknown; restored from __doc__
        """
        logical_and(other, context=None) - Return the digit-wise and of the two
        (logical) operands.
        """
        pass

    def logical_invert(self, context=None): # real signature unknown; restored from __doc__
        """
        logical_invert(context=None) - Return the digit-wise inversion of the
        (logical) operand.
        """
        pass

    def logical_or(self, other, context=None): # real signature unknown; restored from __doc__
        """
        logical_or(other, context=None) - Return the digit-wise or of the two
        (logical) operands.
        """
        pass

    def logical_xor(self, other, context=None): # real signature unknown; restored from __doc__
        """
        logical_xor(other, context=None) - Return the digit-wise exclusive or of the
        two (logical) operands.
        """
        pass

    def max(self, other, context=None): # real signature unknown; restored from __doc__
        """
        max(other, context=None) - Maximum of self and other. If one operand is a
        quiet NaN and the other is numeric, the numeric operand is returned.
        """
        pass

    def max_mag(self, other, context=None): # real signature unknown; restored from __doc__
        """
        max_mag(other, context=None) - Similar to the max() method, but the
        comparison is done using the absolute values of the operands.
        """
        pass

    def min(self, other, context=None): # real signature unknown; restored from __doc__
        """
        min(other, context=None) - Minimum of self and other. If one operand is a
        quiet NaN and the other is numeric, the numeric operand is returned.
        """
        pass

    def min_mag(self, other, context=None): # real signature unknown; restored from __doc__
        """
        min_mag(other, context=None) - Similar to the min() method, but the
        comparison is done using the absolute values of the operands.
        """
        pass

    def next_minus(self, context=None): # real signature unknown; restored from __doc__
        """
        next_minus(context=None) - Return the largest number representable in the
        given context (or in the current default context if no context is given) that
        is smaller than the given operand.
        """
        pass

    def next_plus(self, context=None): # real signature unknown; restored from __doc__
        """
        next_plus(context=None) - Return the smallest number representable in the
        given context (or in the current default context if no context is given) that
        is larger than the given operand.
        """
        pass

    def next_toward(self, other, context=None): # real signature unknown; restored from __doc__
        """
        next_toward(other, context=None) - If the two operands are unequal, return
        the number closest to the first operand in the direction of the second operand.
        If both operands are numerically equal, return a copy of the first operand
        with the sign set to be the same as the sign of the second operand.
        """
        pass

    def normalize(self, context=None): # real signature unknown; restored from __doc__
        """
        normalize(context=None) - Normalize the number by stripping the rightmost
        trailing zeros and converting any result equal to Decimal('0') to Decimal('0e0').
        Used for producing canonical values for members of an equivalence class. For
        example, Decimal('32.100') and Decimal('0.321000e+2') both normalize to the
        equivalent value Decimal('32.1').
        """
        pass

    def number_class(self, context=None): # real signature unknown; restored from __doc__
        """
        number_class(context=None) - Return a string describing the class of the
        operand. The returned value is one of the following ten strings:
        
            * '-Infinity', indicating that the operand is negative infinity.
            * '-Normal', indicating that the operand is a negative normal number.
            * '-Subnormal', indicating that the operand is negative and subnormal.
            * '-Zero', indicating that the operand is a negative zero.
            * '+Zero', indicating that the operand is a positive zero.
            * '+Subnormal', indicating that the operand is positive and subnormal.
            * '+Normal', indicating that the operand is a positive normal number.
            * '+Infinity', indicating that the operand is positive infinity.
            * 'NaN', indicating that the operand is a quiet NaN (Not a Number).
            * 'sNaN', indicating that the operand is a signaling NaN.
        """
        pass

    def quantize(self, exp, rounding=None, context=None): # real signature unknown; restored from __doc__
        """
        quantize(exp, rounding=None, context=None) - Return a value equal to the
        first operand after rounding and having the exponent of the second operand.
        
            >>> Decimal('1.41421356').quantize(Decimal('1.000'))
            Decimal('1.414')
        
        Unlike other operations, if the length of the coefficient after the quantize
        operation would be greater than precision, then an InvalidOperation is signaled.
        This guarantees that, unless there is an error condition, the quantized exponent
        is always equal to that of the right-hand operand.
        
        Also unlike other operations, quantize never signals Underflow, even if the
        result is subnormal and inexact.
        
        If the exponent of the second operand is larger than that of the first, then
        rounding may be necessary. In this case, the rounding mode is determined by the
        rounding argument if given, else by the given context argument; if neither
        argument is given, the rounding mode of the current thread's context is used.
        """
        pass

    def radix(self): # real signature unknown; restored from __doc__
        """
        radix() - Return Decimal(10), the radix (base) in which the Decimal class does
        all its arithmetic. Included for compatibility with the specification.
        """
        pass

    def remainder_near(self, other, context=None): # real signature unknown; restored from __doc__
        """
        remainder_near(other, context=None) - Return the remainder from dividing
        self by other. This differs from self % other in that the sign of the
        remainder is chosen so as to minimize its absolute value. More precisely, the
        return value is self - n * other where n is the integer nearest to the exact
        value of self / other, and if two integers are equally near then the even one
        is chosen.
        
        If the result is zero then its sign will be the sign of self.
        """
        pass

    def rotate(self, other, context=None): # real signature unknown; restored from __doc__
        """
        rotate(other, context=None) - Return the result of rotating the digits of the
        first operand by an amount specified by the second operand. The second operand
        must be an integer in the range -precision through precision. The absolute
        value of the second operand gives the number of places to rotate. If the second
        operand is positive then rotation is to the left; otherwise rotation is to the
        right. The coefficient of the first operand is padded on the left with zeros to
        length precision if necessary. The sign and exponent of the first operand are
        unchanged.
        """
        pass

    def same_quantum(self, other, context=None): # real signature unknown; restored from __doc__
        """
        same_quantum(other, context=None) - Test whether self and other have the
        same exponent or whether both are NaN.
        
        This operation is unaffected by context and is quiet: no flags are changed
        and no rounding is performed. As an exception, the C version may raise
        InvalidOperation if the second operand cannot be converted exactly.
        """
        pass

    def scaleb(self, other, context=None): # real signature unknown; restored from __doc__
        """
        scaleb(other, context=None) - Return the first operand with the exponent
        adjusted the second. Equivalently, return the first operand multiplied by
        10**other. The second operand must be an integer.
        """
        pass

    def shift(self, other, context=None): # real signature unknown; restored from __doc__
        """
        shift(other, context=None) - Return the result of shifting the digits of
        the first operand by an amount specified by the second operand. The second
        operand must be an integer in the range -precision through precision. The
        absolute value of the second operand gives the number of places to shift.
        If the second operand is positive, then the shift is to the left; otherwise
        the shift is to the right. Digits shifted into the coefficient are zeros.
        The sign and exponent of the first operand are unchanged.
        """
        pass

    def sqrt(self, context=None): # real signature unknown; restored from __doc__
        """
        sqrt(context=None) - Return the square root of the argument to full precision.
        The result is correctly rounded using the ROUND_HALF_EVEN rounding mode.
        """
        pass

    def to_eng_string(self, context=None): # real signature unknown; restored from __doc__
        """
        to_eng_string(context=None) - Convert to an engineering-type string.
        Engineering notation has an exponent which is a multiple of 3, so there
        are up to 3 digits left of the decimal place. For example, Decimal('123E+1')
        is converted to Decimal('1.23E+3').
        
        The value of context.capitals determines whether the exponent sign is lower
        or upper case. Otherwise, the context does not affect the operation.
        """
        pass

    def to_integral(self, rounding=None, context=None): # real signature unknown; restored from __doc__
        """
        to_integral(rounding=None, context=None) - Identical to the
        to_integral_value() method. The to_integral() name has been kept
        for compatibility with older versions.
        """
        pass

    def to_integral_exact(self, rounding=None, context=None): # real signature unknown; restored from __doc__
        """
        to_integral_exact(rounding=None, context=None) - Round to the nearest
        integer, signaling Inexact or Rounded as appropriate if rounding occurs.
        The rounding mode is determined by the rounding parameter if given, else
        by the given context. If neither parameter is given, then the rounding mode
        of the current default context is used.
        """
        pass

    def to_integral_value(self, rounding=None, context=None): # real signature unknown; restored from __doc__
        """
        to_integral_value(rounding=None, context=None) - Round to the nearest
        integer without signaling Inexact or Rounded. The rounding mode is determined
        by the rounding parameter if given, else by the given context. If neither
        parameter is given, then the rounding mode of the current default context is
        used.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        pass

    def __complex__(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, value="0", context=None): # real signature unknown; restored from __doc__
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        pass

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



from .tuple import tuple

class DecimalTuple(tuple):
    """ DecimalTuple(sign, digits, exponent) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new OrderedDict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new DecimalTuple object from a sequence or iterable """
        pass

    def _replace(_self, **kwds): # reliably restored by inspect
        """ Return a new DecimalTuple object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, sign, digits, exponent): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, sign, digits, exponent): # reliably restored by inspect
        """ Create new instance of DecimalTuple(sign, digits, exponent) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    digits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 1"""

    exponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 2"""

    sign = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 0"""


    _fields = (
        'sign',
        'digits',
        'exponent',
    )
    _source = "from builtins import property as _property, tuple as _tuple\nfrom operator import itemgetter as _itemgetter\nfrom collections import OrderedDict\n\nclass DecimalTuple(tuple):\n    'DecimalTuple(sign, digits, exponent)'\n\n    __slots__ = ()\n\n    _fields = ('sign', 'digits', 'exponent')\n\n    def __new__(_cls, sign, digits, exponent):\n        'Create new instance of DecimalTuple(sign, digits, exponent)'\n        return _tuple.__new__(_cls, (sign, digits, exponent))\n\n    @classmethod\n    def _make(cls, iterable, new=tuple.__new__, len=len):\n        'Make a new DecimalTuple object from a sequence or iterable'\n        result = new(cls, iterable)\n        if len(result) != 3:\n            raise TypeError('Expected 3 arguments, got %d' % len(result))\n        return result\n\n    def _replace(_self, **kwds):\n        'Return a new DecimalTuple object replacing specified fields with new values'\n        result = _self._make(map(kwds.pop, ('sign', 'digits', 'exponent'), _self))\n        if kwds:\n            raise ValueError('Got unexpected field names: %r' % list(kwds))\n        return result\n\n    def __repr__(self):\n        'Return a nicely formatted representation string'\n        return self.__class__.__name__ + '(sign=%r, digits=%r, exponent=%r)' % self\n\n    def _asdict(self):\n        'Return a new OrderedDict which maps field names to their values.'\n        return OrderedDict(zip(self._fields, self))\n\n    def __getnewargs__(self):\n        'Return self as a plain tuple.  Used by copy and pickle.'\n        return tuple(self)\n\n    sign = _property(_itemgetter(0), doc='Alias for field number 0')\n\n    digits = _property(_itemgetter(1), doc='Alias for field number 1')\n\n    exponent = _property(_itemgetter(2), doc='Alias for field number 2')\n\n"
    __slots__ = ()


from .ZeroDivisionError import ZeroDivisionError

class DivisionByZero(__decimal.DecimalException, ZeroDivisionError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DivisionImpossible(__decimal.InvalidOperation):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


from .ZeroDivisionError import ZeroDivisionError

class DivisionUndefined(__decimal.InvalidOperation, ZeroDivisionError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


from .TypeError import TypeError

class FloatOperation(__decimal.DecimalException, TypeError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Inexact(__decimal.DecimalException):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class InvalidContext(__decimal.InvalidOperation):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Rounded(__decimal.DecimalException):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Overflow(__decimal.Inexact, __decimal.Rounded):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Subnormal(__decimal.DecimalException):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Underflow(__decimal.Inexact, __decimal.Rounded, __decimal.Subnormal):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

BasicContext = None # (!) real value is ''

DefaultContext = None # (!) real value is ''

ExtendedContext = None # (!) real value is ''

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

