import time
from functools import wraps
from evaluator import SimpleEvaluator


def get_time(method):
    """
    Decorator for checking function execution time.
    :param method: function to be tested
    :return: tuple containing function result and time (in seconds) float value
    """

    @wraps(method)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = method(*args, **kwargs)
        end = time.time()
        return result, (end - start)

    return wrapper


class Benchmark:
    """
    Takes care of evaluating provided set of methods.
    """

    def __init__(self, test_cases, result_evaluator=SimpleEvaluator()):
        """
        Initializes benchmark instance.
        Benchmark uses provided set of test cases for evaluating algorithms.
        :param test_cases: set of two-element tuples. Each tuple is in form of with (input, answer) where input refers
        to the arguments passed to the tested method and the answer is expected result of tested algorithm.
        :param result_evaluator: instance of an object used to assign scores to individual answers. Uses SimpleEvaluator
        by default.
        """
        self.test_cases = test_cases
        self.evaluator = result_evaluator

    def evaluate_method(self, method):
        """
        Runs method on test cases and returns overall score.
        :param method: function to test. Function should accept one argument, an input from test case tuple.
        :return: float value, score achieved by method
        """

        @get_time
        def test_method_on_input(test_case):
            return method(test_case)

        results = [test_method_on_input(test) for (test, _) in self.test_cases]
        return sum(self.evaluator.get_score(proper_answer, *result)
                   for (_, proper_answer), result in zip(self.test_cases, results))
