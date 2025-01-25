def function_with_uncommon_error(x, y):
    if x == 0:
        return y / x  # ZeroDivisionError if x is 0, but this is a common error
    elif x == 1:
        return y // 0 # Uncommon error - integer division by zero, only possible when using //
    else:
        return x + y