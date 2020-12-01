class IntegerOperations:
    def reverse(self, x: int) -> int:
        is_negative = True if x < 0 else False
        s = str(abs(x))
        reversed_integer =  int("-" + s[::-1]) if is_negative else int(s[::-1])
        print(reversed_integer)
        if pow(-2, 31) <= reversed_integer and reversed_integer <= (pow(2, 31) - 1):
            return reversed_integer
        else:
            return 0
        