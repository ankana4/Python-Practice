#7. Reverse Integer


#Brute force approach
def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1

    x = abs(x)
    result = int(str(x)[::-1])
    result = result * sign

    if result < -2**31 or result > 2**31 - 1:
        return 0

    return result

x = -123
print(reverse(x))

#Optimal approach
def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        result = 0

        while x > 0:
            digit = x % 10
            result = result * 10 + digit
            x = x // 10

        result = result * sign

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result