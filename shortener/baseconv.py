import numbers
import string


class EncodingError(ValueError):
    """
    Error in encoding from base 10 to base X
    """
    pass


class DecodingError(ValueError):
    """
    Error in decoding from base X to base 10
    """
    pass


class BaseConverter(object):
    """
    Convert numbers from base 10 integers to base X strings and back again.

    Original: http://www.djangosnippets.org/snippets/1431/

    Sample usage:

    >>> base20 = BaseConverter('0123456789abcdefghij')
    >>> base20.from_decimal(1234)
    '31e'
    >>> base20.to_decimal('31e')
    1234
    """
    decimal_digits = string.digits

    def __init__(self, digits):
        self.digits = digits

    def from_decimal(self, i):
        if not isinstance(i, numbers.Real):
            raise EncodingError('%s is not an int()' % i)
        return self.convert(i, self.decimal_digits, self.digits)

    def to_decimal(self, s):
        if not isinstance(s, str):
            raise DecodingError('%s is not a basestring()' % s)
        for index, char in enumerate(s):
            if char not in self.digits and not char == '-' and not index == 0:
                raise DecodingError('Invalid character for encoding: %s' % char)
        return int(self.convert(s, self.digits, self.decimal_digits))

    @staticmethod
    def convert(number, fromdigits, todigits):
        # Based on http://code.activestate.com/recipes/111286/
        if str(number)[0] == '-':
            number = str(number)[1:]
            neg = 1
        else:
            neg = 0

        # make an integer out of the number
        x = 0
        for digit in str(number):
            x = x * len(fromdigits) + fromdigits.index(digit)

        # create the result in base 'len(todigits)'
        if x == 0:
            res = todigits[0]
        else:
            res = ''
            while x > 0:
                digit = x % len(todigits)
                res = todigits[digit] + res
                x = int(x / len(todigits))
            if neg:
                res = '-' + res
        return res


base62 = BaseConverter(string.digits + string.ascii_letters)
