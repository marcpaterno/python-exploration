def transform(func):
    """Takes a callable 'func'. Returns a function that creates a generator
    to wrap an iterable, and which applies the callable 'func' to each item
    in the iteration stream. The callable 'func' must be callable with one
    argument.

    Example:
        gen_sqr = generator_function(lambda x : x*x)
        for x in gen_sqr(range(10)):
            print(x)
    """

    def generator_function(iterable):
        """Create a generator that iterates through 'iterable' and yields
        the result of applying the bound callable to each item in the
        iteration stream.
        """
        for item in iterable:
            yield func(item)

    return generator_function
