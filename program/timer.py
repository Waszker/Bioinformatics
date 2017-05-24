import time


def gettime(method):
    """
    Decorator for checking function execution time.
    :param method: function to be tested
    :return: tuple containing function result and time (in seconds) float value
    """

    def function_time(*args, **kw):
        start = time.time()
        result = method(*args, **kw)
        end = time.time()
        return result, (end - start)

    return function_time
