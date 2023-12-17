def mySqrt(x):
    if x == 0 or x == 1:
        return x

    left, right = 1, x
    result = 0

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == x:
            return mid
        elif mid * mid < x:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    print(f"The square root is (around): {result}")

mySqrt(int(input("Enter a number: ")))
