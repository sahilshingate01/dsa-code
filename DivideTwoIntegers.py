class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # handle overflow case explicitly
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # determine sign of result
        negative = (dividend < 0) ^ (divisor < 0)

        a = abs(dividend)
        b = abs(divisor)
        result = 0

        # subtract largest shifted multiples of b from a
        while a >= b:
            shift = 0
            # find largest shift such that (b << (shift + 1)) <= a
            while (b << (shift + 1)) <= a:
                shift += 1
            # add the multiple (1 << shift) to result
            result += (1 << shift)
            # subtract that chunk from a
            a -= (b << shift)

        if negative:
            result = -result

        # clamp to 32-bit signed range just in case
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result
