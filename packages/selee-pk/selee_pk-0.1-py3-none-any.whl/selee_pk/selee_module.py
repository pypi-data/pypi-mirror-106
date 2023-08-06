def fizz_buzz(x): 
    """
    Parameters
    ----------
    x: any type
      The input that user check

    Returns
    ----------
    string or same type of the input

    """
    #check if x is postive integer. If not, return x
    while (x > 0 and isinstance(x,int)):

        #divisible by both 3 and 5, return the string 'FizzBuzz'
        if x % 3 == 0 and x % 5 == 0:
            return 'FizzBuzz'

        #divisible by 3, return the string 'Fizz'
        elif x % 3 == 0:
            return 'Fizz'

        #divisible by 5, return the string 'Buzz'
        elif x % 5 == 0:
            return 'Buzz'
        else:
            return x
    return x
