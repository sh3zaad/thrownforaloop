def sum_array(array):

    '''
    Return sum of all items in array

    Args:
        array (array): list or array-like object containing numerical values.

    Returns:
        int: sum of all items in array.

    Examples:
        >>> sum_array([8, 3, 2, 7, 4])
        24

    '''

    # initialize variable.
    summed = 0

    # check if item in array is a list (row) or just a value.
    for x in array:
        if isinstance(x, int):
            summed += x
        elif isinstance(x, list):
            summed += sum_array(x) # if x is a list recursively run the function.
    return summed


def fibonacci(n):

    '''
    Return nth term in fibonacci sequence

    Args:
        n (int): interger value starting from 0.

    Returns:
        int: interger that is the nth number in the fibonacci sequence.

    Examples:
        >>> fibonacci(8)
        21

    '''

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def factorial(n):

    '''
    Return a factorial

    Args:
        n (int): interger value starting from 0.

    Returns:
        int: interger that is the factorial of the interger n.

    Examples:
        >>> factorial(5)
        120

    '''

    if n == 0:
        return 1 # factorial of 0 is 1.
    else:
        return n*factorial(n-1)


def reverse(word):

    '''
    Return a string that is reversed

    Args:
        word (str): string value.

    Returns:
        str: string that is the reverse of the inputed string.

    Examples:
        >>> reverse('cows')
        swoc

    '''

    if len(word) == 0:
        return word
    else:
        return word[-1] + reverse(word[0:-1])
